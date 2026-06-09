# Generated from Arit.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,13,68,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,0,
        11,0,12,0,13,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,38,8,2,10,2,12,2,41,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,55,8,3,10,
        3,12,3,58,9,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,66,8,4,1,4,0,2,4,6,5,0,
        2,4,6,8,0,0,71,0,11,1,0,0,0,2,26,1,0,0,0,4,28,1,0,0,0,6,42,1,0,0,
        0,8,65,1,0,0,0,10,12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,
        0,0,0,13,14,1,0,0,0,14,15,1,0,0,0,15,16,5,0,0,1,16,1,1,0,0,0,17,
        18,5,11,0,0,18,19,5,2,0,0,19,20,3,4,2,0,20,21,5,3,0,0,21,27,1,0,
        0,0,22,23,5,1,0,0,23,24,3,4,2,0,24,25,5,3,0,0,25,27,1,0,0,0,26,17,
        1,0,0,0,26,22,1,0,0,0,27,3,1,0,0,0,28,29,6,2,-1,0,29,30,3,6,3,0,
        30,39,1,0,0,0,31,32,10,3,0,0,32,33,5,4,0,0,33,38,3,6,3,0,34,35,10,
        2,0,0,35,36,5,5,0,0,36,38,3,6,3,0,37,31,1,0,0,0,37,34,1,0,0,0,38,
        41,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,40,5,1,0,0,0,41,39,1,0,0,
        0,42,43,6,3,-1,0,43,44,3,8,4,0,44,56,1,0,0,0,45,46,10,4,0,0,46,47,
        5,6,0,0,47,55,3,8,4,0,48,49,10,3,0,0,49,50,5,7,0,0,50,55,3,8,4,0,
        51,52,10,2,0,0,52,53,5,10,0,0,53,55,3,8,4,0,54,45,1,0,0,0,54,48,
        1,0,0,0,54,51,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,
        57,7,1,0,0,0,58,56,1,0,0,0,59,66,5,12,0,0,60,66,5,11,0,0,61,62,5,
        8,0,0,62,63,3,4,2,0,63,64,5,9,0,0,64,66,1,0,0,0,65,59,1,0,0,0,65,
        60,1,0,0,0,65,61,1,0,0,0,66,9,1,0,0,0,7,13,26,37,39,54,56,65
    ]

class AritParser ( Parser ):

    grammarFileName = "Arit.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "';'", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'%'" ]

    symbolicNames = [ "<INVALID>", "PRINT", "ASIGN", "SEMI", "ADD", "SUB", 
                      "MUL", "DIV", "LPAREN", "RPAREN", "MOD", "ID", "INT", 
                      "WS" ]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_termino = 3
    RULE_factor = 4

    ruleNames =  [ "prog", "stmt", "expr", "termino", "factor" ]

    EOF = Token.EOF
    PRINT=1
    ASIGN=2
    SEMI=3
    ADD=4
    SUB=5
    MUL=6
    DIV=7
    LPAREN=8
    RPAREN=9
    MOD=10
    ID=11
    INT=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AritParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AritParser.StmtContext)
            else:
                return self.getTypedRuleContext(AritParser.StmtContext,i)


        def getRuleIndex(self):
            return AritParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = AritParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stmt()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==11):
                    break

            self.state = 15
            self.match(AritParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(AritParser.PRINT, 0)
        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(AritParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)


    class AsignContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AritParser.ID, 0)
        def ASIGN(self):
            return self.getToken(AritParser.ASIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SEMI(self):
            return self.getToken(AritParser.SEMI, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsign" ):
                listener.enterAsign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsign" ):
                listener.exitAsign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsign" ):
                return visitor.visitAsign(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = AritParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 26
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = AritParser.AsignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(AritParser.ID)
                self.state = 18
                self.match(AritParser.ASIGN)
                self.state = 19
                self.expr(0)
                self.state = 20
                self.match(AritParser.SEMI)
                pass
            elif token in [1]:
                localctx = AritParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.match(AritParser.PRINT)
                self.state = 23
                self.expr(0)
                self.state = 24
                self.match(AritParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def ADD(self):
            return self.getToken(AritParser.ADD, 0)
        def termino(self):
            return self.getTypedRuleContext(AritParser.TerminoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)


    class SubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def SUB(self):
            return self.getToken(AritParser.SUB, 0)
        def termino(self):
            return self.getTypedRuleContext(AritParser.TerminoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSub" ):
                return visitor.visitSub(self)
            else:
                return visitor.visitChildren(self)


    class PassTerminoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termino(self):
            return self.getTypedRuleContext(AritParser.TerminoContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassTermino" ):
                listener.enterPassTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassTermino" ):
                listener.exitPassTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassTermino" ):
                return visitor.visitPassTermino(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AritParser.PassTerminoContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 29
            self.termino(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 39
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 37
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = AritParser.AddContext(self, AritParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 31
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 32
                        self.match(AritParser.ADD)
                        self.state = 33
                        self.termino(0)
                        pass

                    elif la_ == 2:
                        localctx = AritParser.SubContext(self, AritParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 34
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 35
                        self.match(AritParser.SUB)
                        self.state = 36
                        self.termino(0)
                        pass

             
                self.state = 41
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_termino

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class DivContext(TerminoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.TerminoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termino(self):
            return self.getTypedRuleContext(AritParser.TerminoContext,0)

        def DIV(self):
            return self.getToken(AritParser.DIV, 0)
        def factor(self):
            return self.getTypedRuleContext(AritParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDiv" ):
                return visitor.visitDiv(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(TerminoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.TerminoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termino(self):
            return self.getTypedRuleContext(AritParser.TerminoContext,0)

        def MOD(self):
            return self.getToken(AritParser.MOD, 0)
        def factor(self):
            return self.getTypedRuleContext(AritParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class MulContext(TerminoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.TerminoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def termino(self):
            return self.getTypedRuleContext(AritParser.TerminoContext,0)

        def MUL(self):
            return self.getToken(AritParser.MUL, 0)
        def factor(self):
            return self.getTypedRuleContext(AritParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)


    class PassFactorContext(TerminoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.TerminoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(AritParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassFactor" ):
                listener.enterPassFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassFactor" ):
                listener.exitPassFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPassFactor" ):
                return visitor.visitPassFactor(self)
            else:
                return visitor.visitChildren(self)



    def termino(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AritParser.TerminoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_termino, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = AritParser.PassFactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 43
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = AritParser.MulContext(self, AritParser.TerminoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        self.match(AritParser.MUL)
                        self.state = 47
                        self.factor()
                        pass

                    elif la_ == 2:
                        localctx = AritParser.DivContext(self, AritParser.TerminoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 48
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 49
                        self.match(AritParser.DIV)
                        self.state = 50
                        self.factor()
                        pass

                    elif la_ == 3:
                        localctx = AritParser.ModContext(self, AritParser.TerminoContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_termino)
                        self.state = 51
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 52
                        self.match(AritParser.MOD)
                        self.state = 53
                        self.factor()
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AritParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class VarContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(AritParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class NumContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(AritParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNum" ):
                listener.enterNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNum" ):
                listener.exitNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNum" ):
                return visitor.visitNum(self)
            else:
                return visitor.visitChildren(self)


    class GrupoContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AritParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(AritParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(AritParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(AritParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGrupo" ):
                listener.enterGrupo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGrupo" ):
                listener.exitGrupo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrupo" ):
                return visitor.visitGrupo(self)
            else:
                return visitor.visitChildren(self)



    def factor(self):

        localctx = AritParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_factor)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = AritParser.NumContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(AritParser.INT)
                pass
            elif token in [11]:
                localctx = AritParser.VarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(AritParser.ID)
                pass
            elif token in [8]:
                localctx = AritParser.GrupoContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 61
                self.match(AritParser.LPAREN)
                self.state = 62
                self.expr(0)
                self.state = 63
                self.match(AritParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        self._predicates[3] = self.termino_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def termino_sempred(self, localctx:TerminoContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         




