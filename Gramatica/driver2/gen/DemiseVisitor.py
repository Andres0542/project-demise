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


    # Visit a parse tree produced by DemiseParser#filterDeclaration.
    def visitFilterDeclaration(self, ctx:DemiseParser.FilterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#filterName.
    def visitFilterName(self, ctx:DemiseParser.FilterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#target.
    def visitTarget(self, ctx:DemiseParser.TargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#testCommand.
    def visitTestCommand(self, ctx:DemiseParser.TestCommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DemiseParser#comment.
    def visitComment(self, ctx:DemiseParser.CommentContext):
        return self.visitChildren(ctx)



del DemiseParser