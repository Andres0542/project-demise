from .symbol_table import SymbolTable
from .errors import SemanticError
from gen.DemiseVisitor import DemiseVisitor
# tabla de compatibilidad aritmética
ARITH_COMPAT = {
    ('int','int') : 'int',
    ('int','float') : 'float',
    ('float','int') : 'float',
    ('float','float') : 'float',
}

# Analizador semantico que recorre el AST
class SemanticVisitor(DemiseVisitor):
    def __init__(self):
        self.symtab = SymbolTable()
        self.errors: list[SemanticError] = []
    
    def _error(self, msg, ctx):
        e = SemanticError(msg, ctx.start.line)
        self.errors.append(e)
        return 'error'

    # -- varDecl: var id : tipo ;
    def visitVarDecl(self, ctx):
        name = ctx.ID().getText()
        type_ = ctx.typeSpec().getText() # 'int'|'float'|'bool'|'string'
        line = ctx.start.line
        
        try:
            self.symtab.declare(name, type_, line)
        except SemanticError as e:
            self.errors.append(e)

    # -- assignment: id := expr ;
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        sym = self.symtab.lookup(name)
        
        if sym is None:
            self._error(f"Variable '{name}' no declarada", ctx)
            return
        sym.used = True
        
        expr_type = self.visit(ctx.expression())
        # Regla: solo se permite asignar si los tipos coinciden
        # o si se puede convertir de int a float
        if expr_type == 'error': return
        ok = (
            sym.type_ == expr_type or 
            (sym.type_ == 'float' and expr_type == 'int')
        )
        if not ok:
            self._error(
                f"No se puede asignar '{expr_type}' a '{sym.type_}' ", ctx)
        else:
            sym.initialized = True

    # -- ifStmt
    def visitIfStmt(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type != 'bool' and cond_type != 'error':
            self._error('Condición de if debe ser bool', ctx)
        
        for block in ctx.block():
            self.symtab.enter_scope(f'if_L{ctx.start.line}')
            self.visit(block)
            self.symtab.exit_scope()

    # -- whileStmt
    def visitWhileStmt(self, ctx):
        cond_type = self.visit(ctx.expression())
        if cond_type != 'bool' and cond_type != 'error':
            self._error('Condición de while debe ser bool', ctx)
            self.symtab.enter_scope(f'while_L{ctx.start.line}')
            self.visit(ctx.block())
            self.symtab.exit_scope()

    # -- relationalExpr
    def visitRelationalExpr(self, ctx):
        valores_numericos = {'int','float'}
        if ctx.RELOP() is None: # si es una expresion sin operador relacional
            return self.visit(ctx.additiveExpr())
        # verificando que t1 y t2 no tienen errores
        t1 = self.visit(ctx.relationalExpr())
        t2 = self.visit(ctx.additiveExpr())
        if 'error' in (t1, t2): return 'error'

        if (t1 not in valores_numericos and t2 not in valores_numericos):
            if (t1 != t2):
                return self._error(f"No se pueden comparar tipos diferentes de variables", ctx)
        # Se deberia hacer verificaciones de tipos.
        # Números y strings aun pueden compararse con == / !=
        return 'bool' # retorna bool por que visitIfStmt se espera el tipo

    # -- additiveExpr
    def visitAdditiveExpr(self, ctx):
        if ctx.ADDOP() is None: # si es una expresion sin operador aritmetico
            # Note que no se esta implementando la función
            # visitMultiplicativeExpr(), asi que se tiene el comportamiento
            # por defecto definido en la clase base.
            return self.visit(ctx.multiplicativeExpr())
        
        t1 = self.visit(ctx.additiveExpr())
        t2 = self.visit(ctx.multiplicativeExpr())
        if 'error' in (t1, t2): return 'error'
        
        # concatenacion de string es permitido
        op = ctx.ADDOP().getText()
        result = ARITH_COMPAT.get((t1, t2))
        if result is None:
            return self._error(
                f"Operación '{t1} {op} {t2}' no válida", ctx)
        return result
    
    def visitMultiplicativeExpr(self, ctx):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.factor())
        
        t1 = self.visit(ctx.getChild(0)) 
        t2 = self.visit(ctx.getChild(2))
        op = ctx.getChild(1).getText()

        if 'error' in (t1, t2): return 'error'

        if op in ('/', 'DIV', 'MOD'):
            derecha = ctx.getChild(2).getText()
            if derecha == '0' or derecha == '0.0':
                return self._error("Division entre 0", ctx)

        result = ARITH_COMPAT.get((t1, t2))
        if result is None:
            return self._error(f"Operación '{t1} {op} {t2}' no válida", ctx)
        
        return result
    # -- factor
    def visitFactor(self, ctx):
        # Nota, las funciones como INT_LIT() retornan su token asignado,
        # caso contratio retornan None. 
        if ctx.INT_LIT(): return 'int'
        if ctx.FLOAT_LIT(): return 'float'
        if ctx.STRING_LIT(): return 'string'
        if ctx.TRUE() or ctx.FALSE(): return 'bool'
        if ctx.expression(): return self.visit(ctx.expression())
        
        # verifica si ID (variable) fue declarada
        name = ctx.ID().getText()
        sym = self.symtab.lookup(name)
        if sym is None:
            return self._error(f"Variable '{name}' no declarada", ctx)
        #Verificacion sobre inicializacion de las variables
        if not sym.initialized:
            return self._error(f"Variable '{name}' no inicializada", ctx)
        sym.used = True
        return sym.type_
