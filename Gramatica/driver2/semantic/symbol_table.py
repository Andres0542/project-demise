from .errors import SemanticError 

class Symbol:
    def __init__(self, name, type_, scope, line):
        self.name= name
        self.type_= type_ # 'int' | 'float' | 'bool' | 'string'
        self.scope= scope
        self.line= line 
        self.initialized = False
        self.used = False

    def __repr__(self):
        return f"Symbol({self.name}: {self.type_} @ {self.scope}, line {self.line})"

    
class SymbolTable:
    def __init__(self):
        # { scope_name -> { var_name -> Symbol } }
        self._table: dict[str, dict[str, Symbol]] = {}
        self._scope_stack: list[str] = ['global']

    # -- ámbito
    @property
    def current_scope(self) -> str:
        return self._scope_stack[-1]
        
    def enter_scope(self, name: str):
        self._scope_stack.append(name)
        self._table.setdefault(name, {})
    
    def exit_scope(self):
        self._scope_stack.pop()

    # -- inserción
    def declare(self, name: str, type_: str, line: int) -> Symbol:
        scope = self.current_scope
        if name in self._table.setdefault(scope, {}):
            raise SemanticError(
                f"Variable '{name}' ya declarada en ámbito '{scope}'", line)
        sym = Symbol(name, type_, scope, line)
        self._table[scope][name] = sym
        return sym

    # -- búsqueda (recorre la pila de ámbitos)
    def lookup(self, name: str) -> Symbol | None:
        for scope in reversed(self._scope_stack):
            if name in self._table.get(scope, {}):
                return self._table[scope][name]
        return None
    
    # -- reporte de variables no usadas
    def unused_warnings(self) -> list[str]:
        warns = []
        for scope_syms in self._table.values():
            for sym in scope_syms.values():
                if not sym.used:
                    warns.append(
                    f"ADVERTENCIA: '{sym.name}' declarada en línea {sym.line} nunca fue usada.")
        return warns
        
        
        

