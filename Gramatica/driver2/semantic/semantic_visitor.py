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