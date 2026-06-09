from llvmlite import ir, binding
from gen.AritVisitor import AritVisitor

class CodeGenVisitor(AritVisitor):

    def __init__(self):
        # Tipo entero de 32 bits (el único tipo de nuestro lenguaje)
        self.i32 = ir.IntType(32)

        # Módulo: contenedor de todo el IR generado
        self.module = ir.Module(name="programa")

        # Declarar printf (función externa de C para imprimir)
        printf_tipo = ir.FunctionType(
            self.i32,
            [ir.PointerType(ir.IntType(8))],
            var_arg=True
        )
        self.printf = ir.Function(self.module, printf_tipo, name="printf")

        # Cadena de formato "%d\n" como global
        fmt = bytearray(b"%d\n\0")
        fmt_tipo = ir.ArrayType(ir.IntType(8), len(fmt))
        self.fmt_global = ir.GlobalVariable(self.module, fmt_tipo, name="fmt")
        self.fmt_global.global_constant = True
        self.fmt_global.initializer = ir.Constant(fmt_tipo, fmt)

        # Crear la función main
        main_tipo = ir.FunctionType(self.i32, [])
        self.main_func = ir.Function(self.module, main_tipo, name="main")
        bloque = self.main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(bloque)

        # Tabla de símbolos: nombre → puntero alloca
        self.variables = {}

    # ------------------------------------------------------------------
    # Sentencias
    # ------------------------------------------------------------------

    def visitAsign(self, ctx):
        nombre = ctx.ID().getText()
        valor  = self.visit(ctx.expr())

        if nombre not in self.variables:
            ptr = self.builder.alloca(self.i32, name=nombre)
            self.variables[nombre] = ptr

        self.builder.store(valor, self.variables[nombre])

    def visitPrint(self, ctx):
        valor = self.visit(ctx.expr())

        cero    = ir.Constant(self.i32, 0)
        fmt_ptr = self.builder.gep(
            self.fmt_global, [cero, cero], name="fmt_ptr"
        )
        self.builder.call(self.printf, [fmt_ptr, valor])
    
    #Sprite Visitor
    def visitSprite(self, ctx):
        tipo = ctx.SPRITE_TYPE().getText()
        sprite = ctx.ID().getText()
        direccion = ctx.STRING_LITERAL().getText().strip('"')

        if tipo not in self.type:
            raise Exception(f"Tipo de sprite desconocido: {tipo}")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])

    def visitMap(self, ctx):
        mapa = ctx.mapRow().getText()

        if not mapa:
            raise Exception("Mapa vacío")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])
    
    def visitMusic(self, ctx):
        direccion = ctx.STRING_LITERAL().getText().strip('"')

        if not direccion:
            raise Exception("Dirección de música vacía")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])

    def visitNpc(self, ctx):
        npc = ctx.ID().getText()
        direccion = ctx.STRING_LITERAL().getText().strip('"')

        if not npc:
            raise Exception("Nombre de NPC vacío")
        elif not direccion:
            raise Exception("Dirección de NPC vacía")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])

    def visitNpcPositioning(self, ctx):
        npc = ctx.ID().getText()
        x = int(ctx.INTEGER(0).getText())
        y = int(ctx.INTEGER(1).getText())

        if not npc:
            raise Exception("Nombre de NPC vacío")
        elif x < 0 or y < 0:
            raise Exception("Coordenadas de NPC no pueden ser negativas")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])
    
    def visitWeapong(self, ctx):
        weapon = ctx.ID().getText()
        direccion = ctx.STRING_LITERAL().getText().strip('"')

        if not weapon:
            raise Exception("Nombre de arma vacío")
        elif not direccion:
            raise Exception("Dirección de arma vacía")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])

    def visitUI(self, ctx):
        direccion = ctx.STRING_LITERAL().getText().strip('"')

        if not direccion:
            raise Exception("Dirección de UI vacía")
        else:
            #Programar logica aqui
        self.builder.call(self.printf, [fmt_ptr, valor])



    # ------------------------------------------------------------------
    # Reglas de paso: propagan el valor generado hacia arriba
    # ------------------------------------------------------------------

    def visitPassTermino(self, ctx):
        return self.visit(ctx.termino())

    def visitPassFactor(self, ctx):
        return self.visit(ctx.factor())

    # ------------------------------------------------------------------
    # Operaciones binarias — cada una devuelve un ir.Value
    # ------------------------------------------------------------------

    def visitAdd(self, ctx):
        izq = self.visit(ctx.expr())
        der = self.visit(ctx.termino())
        return self.builder.add(izq, der, name="add")

    def visitSub(self, ctx):
        izq = self.visit(ctx.expr())
        der = self.visit(ctx.termino())
        return self.builder.sub(izq, der, name="sub")

    def visitMul(self, ctx):
        izq = self.visit(ctx.termino())
        der = self.visit(ctx.factor())
        return self.builder.mul(izq, der, name="mul")
        
    def visitMod(self, ctx):
        izq = self.visit(ctx.termino())
        der = self.visit(ctx.factor())
        return self.builder.srem(izq, der, name="mod")
        
    def visitDiv(self, ctx):
        izq = self.visit(ctx.termino())
        der = self.visit(ctx.factor())
        return self.builder.sdiv(izq, der, name="div")

    # ------------------------------------------------------------------
    # Átomos — devuelven un ir.Value
    # ------------------------------------------------------------------

    def visitNum(self, ctx):
        valor = int(ctx.INT().getText())
        return ir.Constant(self.i32, valor)

    def visitVar(self, ctx):
        nombre = ctx.ID().getText()
        ptr    = self.variables[nombre]
        return self.builder.load(ptr, name=nombre + "_val")

    def visitGrupo(self, ctx):
        return self.visit(ctx.expr())

    # ------------------------------------------------------------------
    # Finalizar y emitir el IR
    # ------------------------------------------------------------------

    def finalizar(self):
        self.builder.ret(ir.Constant(self.i32, 0))

    def emitir(self, archivo="salida.ll"):
        ir_texto = str(self.module)
        with open(archivo, "w") as f:
            f.write(ir_texto)
        return ir_texto
