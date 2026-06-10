from llvmlite import ir
from gen.DemiseVisitor import DemiseVisitor


class CodeGenVisitor(DemiseVisitor):

    def __init__(self):
        self.i32 = ir.IntType(32)
        self.i8 = ir.IntType(8)
        self.module = ir.Module(name="programa")

        main_tipo = ir.FunctionType(self.i32, [])
        self.main_func = ir.Function(self.module, main_tipo, name="main")
        bloque = self.main_func.append_basic_block("entry")
        self.builder = ir.IRBuilder(bloque)

        self.map_generated = False

    def _string_global(self, name: str, text: str) -> ir.GlobalVariable:
        raw = bytearray(text.encode("utf-8") + b"\0")
        arr_type = ir.ArrayType(self.i8, len(raw))
        global_var = ir.GlobalVariable(self.module, arr_type, name=name)
        global_var.global_constant = True
        global_var.initializer = ir.Constant(arr_type, raw)
        return global_var

    def _i32_global(self, name: str, value: int) -> ir.GlobalVariable:
        global_var = ir.GlobalVariable(self.module, self.i32, name=name)
        global_var.initializer = ir.Constant(self.i32, value)
        global_var.linkage = "internal"
        return global_var

    def visitMapDeclaration(self, ctx):
        grid = []
        for row_ctx in ctx.mapRow():
            row = [int(tok.getText()) for tok in row_ctx.INTEGER()]
            if row:
                grid.append(row)

        if not grid:
            raise Exception("El mapa está vacío o no contiene números válidos")

        filas = len(grid)
        columnas = len(grid[0])
        for fila in grid:
            if len(fila) != columnas:
                raise Exception("Todas las filas del mapa deben tener el mismo tamaño")

        valores = []
        for fila in grid:
            valores.extend(fila)

        total = len(valores)
        array_type = ir.ArrayType(self.i32, total)
        llvm_values = [ir.Constant(self.i32, v) for v in valores]
        initializer = ir.Constant(array_type, llvm_values)

        map_w = ir.GlobalVariable(self.module, array_type, name="mapW")
        map_w.initializer = initializer
        map_w.linkage = "internal"
        map_w.align = 16

        self._i32_global("mapX", columnas)
        self._i32_global("mapY", filas)
        self.map_generated = True

    def visitMusicDeclaration(self, ctx):
        path = ctx.STRING_LITERAL().getText().strip("'")
        self._string_global("music_path", path)

    def visitSpriteDeclaration(self, ctx):
        sprite_type = ctx.SPRITE_TYPE().getText()
        path = ctx.STRING_LITERAL().getText().strip("'")
        self._string_global(f"sprite_{sprite_type}", path)

    def visitNpcDeclaration(self, ctx):
        npc = ctx.ID().getText()
        path = ctx.STRING_LITERAL().getText().strip("'")
        self._string_global(f"npc_{npc}", path)

    def visitNpcPositioning(self, ctx):
        npc = ctx.ID().getText()
        x = int(ctx.INTEGER(0).getText())
        y = int(ctx.INTEGER(1).getText())
        self._i32_global(f"npc_{npc}_x", x)
        self._i32_global(f"npc_{npc}_y", y)

    def visitWeaponDeclaration(self, ctx):
        weapon = ctx.ID().getText()
        path = ctx.STRING_LITERAL().getText().strip("'")
        self._string_global(f"weapon_{weapon}", path)

    def visitUiDeclaration(self, ctx):
        path = ctx.STRING_LITERAL().getText().strip("'")
        self._string_global("ui_path", path)

    def visitLightningDeclaration(self, ctx):
        value = int(ctx.INTEGER().getText())
        self._i32_global("lightning", value)

    def finalizar(self):
        self.builder.ret(ir.Constant(self.i32, 0))

    def emitir(self, archivo="salida.ll"):
        ir_texto = str(self.module)
        with open(archivo, "w") as f:
            f.write(ir_texto)
        return ir_texto
