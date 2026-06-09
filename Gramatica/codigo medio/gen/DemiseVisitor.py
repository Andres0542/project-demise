# Generated from Demise.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .DemiseParser import DemiseParser
else:
    from DemiseParser import DemiseParser

# This class defines a complete generic visitor for a parse tree produced by DemiseParser.

class DemiseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DemiseParser#program.
    def visitProgram(self, ctx:DemiseParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#statement.
    def visitStatement(self, ctx:DemiseParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#spriteDeclaration.
    def visitSpriteDeclaration(self, ctx:DemiseParser.SpriteDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#filter.
    def visitFilter(self, ctx:DemiseParser.FilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#npcDeclaration.
    def visitNpcDeclaration(self, ctx:DemiseParser.NpcDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#musicDeclaration.
    def visitMusicDeclaration(self, ctx:DemiseParser.MusicDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#mapDeclaration.
    def visitMapDeclaration(self, ctx:DemiseParser.MapDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#mapRow.
    def visitMapRow(self, ctx:DemiseParser.MapRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#lightningDeclaration.
    def visitLightningDeclaration(self, ctx:DemiseParser.LightningDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#uiDeclaration.
    def visitUiDeclaration(self, ctx:DemiseParser.UiDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#npcPositioning.
    def visitNpcPositioning(self, ctx:DemiseParser.NpcPositioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#weaponDeclaration.
    def visitWeaponDeclaration(self, ctx:DemiseParser.WeaponDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#weaponLogic.
    def visitWeaponLogic(self, ctx:DemiseParser.WeaponLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#testCommand.
    def visitTestCommand(self, ctx:DemiseParser.TestCommandContext):
        return self.visitChildren(ctx)



del DemiseParser