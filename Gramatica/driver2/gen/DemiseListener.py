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


    # Enter a parse tree produced by DemiseParser#filterDeclaration.
    def enterFilterDeclaration(self, ctx:DemiseParser.FilterDeclarationContext):
        pass

    # Exit a parse tree produced by DemiseParser#filterDeclaration.
    def exitFilterDeclaration(self, ctx:DemiseParser.FilterDeclarationContext):
        pass


    # Enter a parse tree produced by DemiseParser#filterName.
    def enterFilterName(self, ctx:DemiseParser.FilterNameContext):
        pass

    # Exit a parse tree produced by DemiseParser#filterName.
    def exitFilterName(self, ctx:DemiseParser.FilterNameContext):
        pass


    # Enter a parse tree produced by DemiseParser#target.
    def enterTarget(self, ctx:DemiseParser.TargetContext):
        pass

    # Exit a parse tree produced by DemiseParser#target.
    def exitTarget(self, ctx:DemiseParser.TargetContext):
        pass


    # Enter a parse tree produced by DemiseParser#testCommand.
    def enterTestCommand(self, ctx:DemiseParser.TestCommandContext):
        pass

    # Exit a parse tree produced by DemiseParser#testCommand.
    def exitTestCommand(self, ctx:DemiseParser.TestCommandContext):
        pass


    # Enter a parse tree produced by DemiseParser#comment.
    def enterComment(self, ctx:DemiseParser.CommentContext):
        pass

    # Exit a parse tree produced by DemiseParser#comment.
    def exitComment(self, ctx:DemiseParser.CommentContext):
        pass



del DemiseParser