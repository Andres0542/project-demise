from .symbol_table import SymbolTable
from .errors import SemanticError
from gen.DemiseVisitor import DemiseVisitor
from gen.DemiseParser import DemiseParser
from .Comportamiento.Floorcasting import Floorcasting
import subprocess
import os

ARITH_COMPAT = {
    ('int','int') : 'int',
    ('int','float') : 'float',
    ('float','int') : 'float',
    ('float','float') : 'float',
}

# Mapeo de cada test command a su archivo en comportamiento/
TEST_FILES = {
    "floorcasting_test"   : "floorcasting_test.py",
    "raycasting_test"     : "raycasting_test.py",
    "raycasting_maze_test": "raycasting_maze_test.py",
    "reflexing_floor"     : "reflexing_floor.py",
}

class SemanticVisitor(DemiseVisitor):
    def __init__(self):
        self.symtab = SymbolTable()
        self.errors: list[SemanticError] = []

    def _error(self, msg, ctx):
        e = SemanticError(msg, ctx.start.line)
        self.errors.append(e)
        return 'error'

    def visitTestCommand(self, ctx: DemiseParser.TestCommandContext):
        #self.visitChildren(ctx)  # Primero visitamos a los hijos para procesar el comando
        if ctx.FLOORCASTING_TEST():
            Floorcasting().main()
            test_name = "floorcasting.py"
        elif ctx.RAYCASTING_TEST():
            test_name = "raycasting_test"
        elif ctx.RAYCASTING_MAZE_TEST():
            test_name = "raycasting_maze_test"
        elif ctx.REFLEXING_FLOOR():
            test_name = "reflexing_floor"
        else:
            test_name = "unknown"

        print(f"hola — test command encontrado: {test_name}")

        return self.visitChildren(ctx)
    
    def visitSpriteDeclaration(self, ctx: DemiseParser.SpriteDeclarationContext):
        # 1. Extraer datos del contexto (asegúrate de que los nombres coincidan con tu .g4)
        sprite_type = ctx.SPRITE_TYPE().getText()
        # Limpiamos las comillas del path (ej: "res://hero.png" -> res://hero.png)
        path = ctx.STRING_LITERAL().getText().strip("'\"")
        line = ctx.start.line # Obtenemos la línea para el reporte de errores

        try:
            # 2. Registrar en la tabla de símbolos
            self.symtab.declare_sprite(sprite_type, path, line)
        
            # 3. Feedback visual (opcional)
            print(f"✅ Sprite registrado exitosamente:")
            print(f"   Nombre: {sprite_type} | Path: {path}")

        except SemanticError as e:
            # 4. Manejo de errores
            return self._error(e.message, ctx)

        return self.visitChildren(ctx)

        