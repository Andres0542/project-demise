# Generated from Arit.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AritParser import AritParser
else:
    from AritParser import AritParser

# This class defines a complete generic visitor for a parse tree produced by AritParser.

class AritVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AritParser#prog.
    def visitProg(self, ctx:AritParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Asign.
    def visitAsign(self, ctx:AritParser.AsignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Print.
    def visitPrint(self, ctx:AritParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Add.
    def visitAdd(self, ctx:AritParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Sub.
    def visitSub(self, ctx:AritParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#PassTermino.
    def visitPassTermino(self, ctx:AritParser.PassTerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Div.
    def visitDiv(self, ctx:AritParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Mod.
    def visitMod(self, ctx:AritParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Mul.
    def visitMul(self, ctx:AritParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#PassFactor.
    def visitPassFactor(self, ctx:AritParser.PassFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Num.
    def visitNum(self, ctx:AritParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Var.
    def visitVar(self, ctx:AritParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AritParser#Grupo.
    def visitGrupo(self, ctx:AritParser.GrupoContext):
        return self.visitChildren(ctx)



del AritParser