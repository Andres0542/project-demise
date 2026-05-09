# Generated from Demise.g4 by ANTLR 4.13.1
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
        4,1,15,52,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,
        1,0,3,6,48,0,19,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,36,1,0,0,0,8,
        43,1,0,0,0,10,45,1,0,0,0,12,47,1,0,0,0,14,49,1,0,0,0,16,18,3,2,1,
        0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,22,
        1,0,0,0,21,19,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,30,3,4,2,0,25,
        30,3,6,3,0,26,30,3,12,6,0,27,30,3,14,7,0,28,30,5,14,0,0,29,24,1,
        0,0,0,29,25,1,0,0,0,29,26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,
        3,1,0,0,0,31,32,5,1,0,0,32,33,5,11,0,0,33,34,5,7,0,0,34,35,5,12,
        0,0,35,5,1,0,0,0,36,37,5,2,0,0,37,38,5,8,0,0,38,39,3,8,4,0,39,40,
        5,10,0,0,40,41,3,10,5,0,41,42,5,9,0,0,42,7,1,0,0,0,43,44,5,11,0,
        0,44,9,1,0,0,0,45,46,5,11,0,0,46,11,1,0,0,0,47,48,7,0,0,0,48,13,
        1,0,0,0,49,50,5,13,0,0,50,15,1,0,0,0,2,19,29
    ]

class DemiseParser ( Parser ):

    grammarFileName = "Demise.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sprite'", "'filter'", "'floorcasting_test'", 
                     "'raycasting_test'", "'raycasting_maze_test'", "'reflexing_floor'", 
                     "'->'", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "SPRITE", "FILTER", "FLOORCASTING_TEST", 
                      "RAYCASTING_TEST", "RAYCASTING_MAZE_TEST", "REFLEXING_FLOOR", 
                      "ARROW", "LPAREN", "RPAREN", "COMMA", "IDENTIFIER", 
                      "STRING_LITERAL", "COMMENT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_spriteDeclaration = 2
    RULE_filterDeclaration = 3
    RULE_filterName = 4
    RULE_target = 5
    RULE_testCommand = 6
    RULE_comment = 7

    ruleNames =  [ "program", "statement", "spriteDeclaration", "filterDeclaration", 
                   "filterName", "target", "testCommand", "comment" ]

    EOF = Token.EOF
    SPRITE=1
    FILTER=2
    FLOORCASTING_TEST=3
    RAYCASTING_TEST=4
    RAYCASTING_MAZE_TEST=5
    REFLEXING_FLOOR=6
    ARROW=7
    LPAREN=8
    RPAREN=9
    COMMA=10
    IDENTIFIER=11
    STRING_LITERAL=12
    COMMENT=13
    NEWLINE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(DemiseParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemiseParser.StatementContext)
            else:
                return self.getTypedRuleContext(DemiseParser.StatementContext,i)


        def getRuleIndex(self):
            return DemiseParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = DemiseParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 24702) != 0):
                self.state = 16
                self.statement()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 22
            self.match(DemiseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def spriteDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.SpriteDeclarationContext,0)


        def filterDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.FilterDeclarationContext,0)


        def testCommand(self):
            return self.getTypedRuleContext(DemiseParser.TestCommandContext,0)


        def comment(self):
            return self.getTypedRuleContext(DemiseParser.CommentContext,0)


        def NEWLINE(self):
            return self.getToken(DemiseParser.NEWLINE, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = DemiseParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.spriteDeclaration()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.filterDeclaration()
                pass
            elif token in [3, 4, 5, 6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 26
                self.testCommand()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 27
                self.comment()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 28
                self.match(DemiseParser.NEWLINE)
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


    class SpriteDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPRITE(self):
            return self.getToken(DemiseParser.SPRITE, 0)

        def IDENTIFIER(self):
            return self.getToken(DemiseParser.IDENTIFIER, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def STRING_LITERAL(self):
            return self.getToken(DemiseParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_spriteDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpriteDeclaration" ):
                listener.enterSpriteDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpriteDeclaration" ):
                listener.exitSpriteDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpriteDeclaration" ):
                return visitor.visitSpriteDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def spriteDeclaration(self):

        localctx = DemiseParser.SpriteDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_spriteDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(DemiseParser.SPRITE)
            self.state = 32
            self.match(DemiseParser.IDENTIFIER)
            self.state = 33
            self.match(DemiseParser.ARROW)
            self.state = 34
            self.match(DemiseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(DemiseParser.FILTER, 0)

        def LPAREN(self):
            return self.getToken(DemiseParser.LPAREN, 0)

        def filterName(self):
            return self.getTypedRuleContext(DemiseParser.FilterNameContext,0)


        def COMMA(self):
            return self.getToken(DemiseParser.COMMA, 0)

        def target(self):
            return self.getTypedRuleContext(DemiseParser.TargetContext,0)


        def RPAREN(self):
            return self.getToken(DemiseParser.RPAREN, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_filterDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterDeclaration" ):
                listener.enterFilterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterDeclaration" ):
                listener.exitFilterDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterDeclaration" ):
                return visitor.visitFilterDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def filterDeclaration(self):

        localctx = DemiseParser.FilterDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(DemiseParser.FILTER)
            self.state = 37
            self.match(DemiseParser.LPAREN)
            self.state = 38
            self.filterName()
            self.state = 39
            self.match(DemiseParser.COMMA)
            self.state = 40
            self.target()
            self.state = 41
            self.match(DemiseParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DemiseParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_filterName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterName" ):
                listener.enterFilterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterName" ):
                listener.exitFilterName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterName" ):
                return visitor.visitFilterName(self)
            else:
                return visitor.visitChildren(self)




    def filterName(self):

        localctx = DemiseParser.FilterNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_filterName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(DemiseParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TargetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(DemiseParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget" ):
                listener.enterTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget" ):
                listener.exitTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget" ):
                return visitor.visitTarget(self)
            else:
                return visitor.visitChildren(self)




    def target(self):

        localctx = DemiseParser.TargetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(DemiseParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOORCASTING_TEST(self):
            return self.getToken(DemiseParser.FLOORCASTING_TEST, 0)

        def RAYCASTING_TEST(self):
            return self.getToken(DemiseParser.RAYCASTING_TEST, 0)

        def RAYCASTING_MAZE_TEST(self):
            return self.getToken(DemiseParser.RAYCASTING_MAZE_TEST, 0)

        def REFLEXING_FLOOR(self):
            return self.getToken(DemiseParser.REFLEXING_FLOOR, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_testCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestCommand" ):
                listener.enterTestCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestCommand" ):
                listener.exitTestCommand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestCommand" ):
                return visitor.visitTestCommand(self)
            else:
                return visitor.visitChildren(self)




    def testCommand(self):

        localctx = DemiseParser.TestCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_testCommand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(DemiseParser.COMMENT, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComment" ):
                return visitor.visitComment(self)
            else:
                return visitor.visitChildren(self)




    def comment(self):

        localctx = DemiseParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_comment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DemiseParser.COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





