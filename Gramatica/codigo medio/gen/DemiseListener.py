# Generated from Demise.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DemiseParser import DemiseParser
else:
    from DemiseParser import DemiseParser

# This class defines a complete listener for a parse tree produced by DemiseParser.
class DemiseListener(ParseTreeListener):

    # Enter a parse tree produced by DemiseParser#program.
    def enterProgram(self, ctx:DemiseParser.ProgramContext):
        pass

    # Exit a parse tree produced by DemiseParser#program.
    def exitProgram(self, ctx:DemiseParser.ProgramContext):
        pass


    # Enter a parse tree produced by DemiseParser#statement.
    def enterStatement(self, ctx:DemiseParser.StatementContext):
        pass

    # Exit a parse tree produced by DemiseParser#statement.
    def exitStatement(self, ctx:DemiseParser.StatementContext):
        pass


    # Enter a parse tree produced by DemiseParser#spriteDeclaration.
    def enterSpriteDeclaration(self, ctx:DemiseParser.SpriteDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#spriteDeclaration.
    def exitSpriteDeclaration(self, ctx:DemiseParser.SpriteDeclarationContext):
        pass


    # Enter a parse tree produced by DemiseParser#npcDeclaration.
    def enterNpcDeclaration(self, ctx:DemiseParser.NpcDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#npcDeclaration.
    def exitNpcDeclaration(self, ctx:DemiseParser.NpcDeclarationContext):
        pass


    # Enter a parse tree produced by DemiseParser#musicDeclaration.
    def enterMusicDeclaration(self, ctx:DemiseParser.MusicDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#musicDeclaration.
    def exitMusicDeclaration(self, ctx:DemiseParser.MusicDeclarationContext):
        pass


    # Enter a parse tree produced by DemiseParser#mapDeclaration.
    def enterMapDeclaration(self, ctx:DemiseParser.MapDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#mapDeclaration.
    def exitMapDeclaration(self, ctx:DemiseParser.MapDeclarationContext):
        pass


    # Enter a parse tree produced by DemiseParser#mapRow.
    def enterMapRow(self, ctx:DemiseParser.MapRowContext):
        pass

    # Exit a parse tree produced by DemiseParser#mapRow.
    def exitMapRow(self, ctx:DemiseParser.MapRowContext):
        pass


    # Enter a parse tree produced by DemiseParser#uiDeclaration.
    def enterUiDeclaration(self, ctx:DemiseParser.UiDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#uiDeclaration.
    def exitUiDeclaration(self, ctx:DemiseParser.UiDeclarationContext):
        pass


    # Enter a parse tree produced by DemiseParser#npcPositioning.
    def enterNpcPositioning(self, ctx:DemiseParser.NpcPositioningContext):
        pass

    # Exit a parse tree produced by DemiseParser#npcPositioning.
    def exitNpcPositioning(self, ctx:DemiseParser.NpcPositioningContext):
        pass


    # Enter a parse tree produced by DemiseParser#weaponDeclaration.
    def enterWeaponDeclaration(self, ctx:DemiseParser.WeaponDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#weaponDeclaration.
    def exitWeaponDeclaration(self, ctx:DemiseParser.WeaponDeclarationContext):
        pass



del DemiseParser