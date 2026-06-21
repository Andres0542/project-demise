from gen.DemiseVisitor import DemiseVisitor

class CodeGenVisitor(DemiseVisitor):

    def __init__(self):
        # Listas para almacenar las distintas partes del archivo C
        self.headers = ["#include <stdio.h>", "#include <stdint.h>", "#include <stdlib.h>", "#include <GL/glut.h>", "#include <math.h>", "#include <SDL2/SDL.h>", "#include <SDL2/SDL_mixer.h>"]
        self.global_vars = []
        self.main_body = []

    def _string_global(self, name: str, text: str) -> None:
        # En C, las cadenas de texto se escapan y se guardan como const char* o char[]
        # Usamos doble comilla para C y escapamos posibles comillas internas si fuera necesario
        self.global_vars.append(f'const char* {name} = "{text}";')

    def _i32_global(self, name: str, value: int) -> None:
        # Usamos static int para emular el comportamiento 'internal' de LLVM
        self.global_vars.append(f'static int32_t {name} = {value};')

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

        # Convertimos los valores de la matriz a un formato de inicialización de C: {1, 2, 3, ...}
        valores_c = ", ".join(map(str, valores))
        
        # En C, podemos declarar el array plano directamente con alineación si lo deseas
        # __attribute__((aligned(16))) es la sintaxis estándar en GCC/Clang para alineación
        self.global_vars.append(
            f'int mapW[] = {{ {valores_c} }};'
        )

        self._i32_global("mapX", columnas)
        self._i32_global("mapY", filas)

    def visitMusicDeclaration(self, ctx):
        path = ctx.STRING_LITERAL().getText().strip("'")
        self._string_global("music_path", path)

    def visitSpriteDeclaration(self, ctx):
        # Extraemos la ruta del archivo (ej: "sprites/heroe.h")
        path = ctx.STRING_LITERAL().getText().strip("'\"")
        
        # En C, los include usan comillas dobles: #include "archivo.h"
        self.headers.append(f'#include "{path}"')

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

    def finalizar(self):
        # Añade el retorno final de la función main
        self.main_body.append("    return 0;")

    def emitir(self, archivo="salida.c"):
        # Construimos el código fuente final estructurando las partes de C
        lineas_c = []
        
        # 1. Cabeceras
        lineas_c.extend(self.headers)
        lineas_c.append("") # Línea en blanco
        
        # 2. Variables Globales
        lineas_c.extend(self.global_vars)
        lineas_c.append("")
        
        # 3. Función Main
        lineas_c.append("int main() {")
        if self.main_body:
            # Sangramos el cuerpo del main para que sea legible
            lineas_c.extend(self.main_body)
        else:
            lineas_c.append("    return 0;")
        lineas_c.append("}")

        codigo_final = "\n".join(lineas_c)
        
        # Guardamos en el archivo .c
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(codigo_final)
            
        return codigo_final