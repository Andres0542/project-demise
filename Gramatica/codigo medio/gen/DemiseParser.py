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
        4,1,21,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,4,5,57,8,5,11,
        5,12,5,58,1,5,1,5,1,6,1,6,4,6,65,8,6,11,6,12,6,66,1,6,1,6,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,88,0,23,1,0,0,0,2,37,1,0,0,
        0,4,39,1,0,0,0,6,44,1,0,0,0,8,49,1,0,0,0,10,53,1,0,0,0,12,62,1,0,
        0,0,14,70,1,0,0,0,16,74,1,0,0,0,18,82,1,0,0,0,20,22,3,2,1,0,21,20,
        1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,
        25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,38,3,4,2,0,29,38,3,10,
        5,0,30,38,3,6,3,0,31,38,3,16,8,0,32,38,3,8,4,0,33,38,3,18,9,0,34,
        38,3,14,7,0,35,38,5,19,0,0,36,38,5,20,0,0,37,28,1,0,0,0,37,29,1,
        0,0,0,37,30,1,0,0,0,37,31,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,37,
        34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,3,1,0,0,0,39,40,5,1,0,
        0,40,41,5,2,0,0,41,42,5,9,0,0,42,43,5,17,0,0,43,5,1,0,0,0,44,45,
        5,3,0,0,45,46,5,18,0,0,46,47,5,9,0,0,47,48,5,17,0,0,48,7,1,0,0,0,
        49,50,5,4,0,0,50,51,5,9,0,0,51,52,5,17,0,0,52,9,1,0,0,0,53,54,5,
        5,0,0,54,56,5,9,0,0,55,57,3,12,6,0,56,55,1,0,0,0,57,58,1,0,0,0,58,
        56,1,0,0,0,58,59,1,0,0,0,59,60,1,0,0,0,60,61,5,15,0,0,61,11,1,0,
        0,0,62,64,5,12,0,0,63,65,5,16,0,0,64,63,1,0,0,0,65,66,1,0,0,0,66,
        64,1,0,0,0,66,67,1,0,0,0,67,68,1,0,0,0,68,69,5,13,0,0,69,13,1,0,
        0,0,70,71,5,6,0,0,71,72,5,9,0,0,72,73,5,17,0,0,73,15,1,0,0,0,74,
        75,5,18,0,0,75,76,5,9,0,0,76,77,5,10,0,0,77,78,5,16,0,0,78,79,5,
        14,0,0,79,80,5,16,0,0,80,81,5,11,0,0,81,17,1,0,0,0,82,83,5,7,0,0,
        83,84,5,18,0,0,84,85,5,9,0,0,85,86,5,17,0,0,86,19,1,0,0,0,4,23,37,
        58,66
    ]

class DemiseParser ( Parser ):

    grammarFileName = "Demise.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'sprite'", "<INVALID>", "'npc'", "'music'", 
                     "'map'", "'UI'", "'weapon'", "<INVALID>", "'->'", "'('", 
                     "')'", "'['", "']'", "','", "';'" ]

    symbolicNames = [ "<INVALID>", "SPRITE", "SPRITE_TYPE", "NPC", "MUSIC", 
                      "MAP", "UI", "WEAPON", "WEAPON_LOGIC", "ARROW", "LPAREN", 
                      "RPAREN", "LBRACKET", "RBRACKET", "COMMA", "SEMICOLON", 
                      "INTEGER", "STRING_LITERAL", "ID", "COMENTARIO", "ESPACIO", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_spriteDeclaration = 2
    RULE_npcDeclaration = 3
    RULE_musicDeclaration = 4
    RULE_mapDeclaration = 5
    RULE_mapRow = 6
    RULE_uiDeclaration = 7
    RULE_npcPositioning = 8
    RULE_weaponDeclaration = 9

    ruleNames =  [ "program", "statement", "spriteDeclaration", "npcDeclaration", 
                   "musicDeclaration", "mapDeclaration", "mapRow", "uiDeclaration", 
                   "npcPositioning", "weaponDeclaration" ]

    EOF = Token.EOF
    SPRITE=1
    SPRITE_TYPE=2
    NPC=3
    MUSIC=4
    MAP=5
    UI=6
    WEAPON=7
    WEAPON_LOGIC=8
    ARROW=9
    LPAREN=10
    RPAREN=11
    LBRACKET=12
    RBRACKET=13
    COMMA=14
    SEMICOLON=15
    INTEGER=16
    STRING_LITERAL=17
    ID=18
    COMENTARIO=19
    ESPACIO=20
    WS=21

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
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1835258) != 0):
                self.state = 20
                self.statement()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
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


        def mapDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.MapDeclarationContext,0)


        def npcDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.NpcDeclarationContext,0)


        def npcPositioning(self):
            return self.getTypedRuleContext(DemiseParser.NpcPositioningContext,0)


        def musicDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.MusicDeclarationContext,0)


        def weaponDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.WeaponDeclarationContext,0)


        def uiDeclaration(self):
            return self.getTypedRuleContext(DemiseParser.UiDeclarationContext,0)


        def COMENTARIO(self):
            return self.getToken(DemiseParser.COMENTARIO, 0)

        def ESPACIO(self):
            return self.getToken(DemiseParser.ESPACIO, 0)

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
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.spriteDeclaration()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.mapDeclaration()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.npcDeclaration()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.npcPositioning()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.musicDeclaration()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 6)
                self.state = 33
                self.weaponDeclaration()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 34
                self.uiDeclaration()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 8)
                self.state = 35
                self.match(DemiseParser.COMENTARIO)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 9)
                self.state = 36
                self.match(DemiseParser.ESPACIO)
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

        def SPRITE_TYPE(self):
            return self.getToken(DemiseParser.SPRITE_TYPE, 0)

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
            self.state = 39
            self.match(DemiseParser.SPRITE)
            self.state = 40
            self.match(DemiseParser.SPRITE_TYPE)
            self.state = 41
            self.match(DemiseParser.ARROW)
            self.state = 42
            self.match(DemiseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NpcDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NPC(self):
            return self.getToken(DemiseParser.NPC, 0)

        def ID(self):
            return self.getToken(DemiseParser.ID, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def STRING_LITERAL(self):
            return self.getToken(DemiseParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_npcDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNpcDeclaration" ):
                listener.enterNpcDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNpcDeclaration" ):
                listener.exitNpcDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNpcDeclaration" ):
                return visitor.visitNpcDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def npcDeclaration(self):

        localctx = DemiseParser.NpcDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_npcDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(DemiseParser.NPC)
            self.state = 45
            self.match(DemiseParser.ID)
            self.state = 46
            self.match(DemiseParser.ARROW)
            self.state = 47
            self.match(DemiseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MusicDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MUSIC(self):
            return self.getToken(DemiseParser.MUSIC, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def STRING_LITERAL(self):
            return self.getToken(DemiseParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_musicDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMusicDeclaration" ):
                listener.enterMusicDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMusicDeclaration" ):
                listener.exitMusicDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMusicDeclaration" ):
                return visitor.visitMusicDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def musicDeclaration(self):

        localctx = DemiseParser.MusicDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_musicDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(DemiseParser.MUSIC)
            self.state = 50
            self.match(DemiseParser.ARROW)
            self.state = 51
            self.match(DemiseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(DemiseParser.MAP, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def SEMICOLON(self):
            return self.getToken(DemiseParser.SEMICOLON, 0)

        def mapRow(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(DemiseParser.MapRowContext)
            else:
                return self.getTypedRuleContext(DemiseParser.MapRowContext,i)


        def getRuleIndex(self):
            return DemiseParser.RULE_mapDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDeclaration" ):
                listener.enterMapDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDeclaration" ):
                listener.exitMapDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDeclaration" ):
                return visitor.visitMapDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def mapDeclaration(self):

        localctx = DemiseParser.MapDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mapDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(DemiseParser.MAP)
            self.state = 54
            self.match(DemiseParser.ARROW)
            self.state = 56 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.mapRow()
                self.state = 58 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==12):
                    break

            self.state = 60
            self.match(DemiseParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapRowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(DemiseParser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(DemiseParser.RBRACKET, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(DemiseParser.INTEGER)
            else:
                return self.getToken(DemiseParser.INTEGER, i)

        def getRuleIndex(self):
            return DemiseParser.RULE_mapRow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapRow" ):
                listener.enterMapRow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapRow" ):
                listener.exitMapRow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapRow" ):
                return visitor.visitMapRow(self)
            else:
                return visitor.visitChildren(self)




    def mapRow(self):

        localctx = DemiseParser.MapRowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_mapRow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(DemiseParser.LBRACKET)
            self.state = 64 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 63
                self.match(DemiseParser.INTEGER)
                self.state = 66 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

            self.state = 68
            self.match(DemiseParser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UiDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UI(self):
            return self.getToken(DemiseParser.UI, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def STRING_LITERAL(self):
            return self.getToken(DemiseParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_uiDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUiDeclaration" ):
                listener.enterUiDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUiDeclaration" ):
                listener.exitUiDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUiDeclaration" ):
                return visitor.visitUiDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def uiDeclaration(self):

        localctx = DemiseParser.UiDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_uiDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(DemiseParser.UI)
            self.state = 71
            self.match(DemiseParser.ARROW)
            self.state = 72
            self.match(DemiseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NpcPositioningContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DemiseParser.ID, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def LPAREN(self):
            return self.getToken(DemiseParser.LPAREN, 0)

        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(DemiseParser.INTEGER)
            else:
                return self.getToken(DemiseParser.INTEGER, i)

        def COMMA(self):
            return self.getToken(DemiseParser.COMMA, 0)

        def RPAREN(self):
            return self.getToken(DemiseParser.RPAREN, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_npcPositioning

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNpcPositioning" ):
                listener.enterNpcPositioning(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNpcPositioning" ):
                listener.exitNpcPositioning(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNpcPositioning" ):
                return visitor.visitNpcPositioning(self)
            else:
                return visitor.visitChildren(self)




    def npcPositioning(self):

        localctx = DemiseParser.NpcPositioningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_npcPositioning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(DemiseParser.ID)
            self.state = 75
            self.match(DemiseParser.ARROW)
            self.state = 76
            self.match(DemiseParser.LPAREN)
            self.state = 77
            self.match(DemiseParser.INTEGER)
            self.state = 78
            self.match(DemiseParser.COMMA)
            self.state = 79
            self.match(DemiseParser.INTEGER)
            self.state = 80
            self.match(DemiseParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeaponDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WEAPON(self):
            return self.getToken(DemiseParser.WEAPON, 0)

        def ID(self):
            return self.getToken(DemiseParser.ID, 0)

        def ARROW(self):
            return self.getToken(DemiseParser.ARROW, 0)

        def STRING_LITERAL(self):
            return self.getToken(DemiseParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return DemiseParser.RULE_weaponDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeaponDeclaration" ):
                listener.enterWeaponDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeaponDeclaration" ):
                listener.exitWeaponDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeaponDeclaration" ):
                return visitor.visitWeaponDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def weaponDeclaration(self):

        localctx = DemiseParser.WeaponDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_weaponDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(DemiseParser.WEAPON)
            self.state = 83
            self.match(DemiseParser.ID)
            self.state = 84
            self.match(DemiseParser.ARROW)
            self.state = 85
            self.match(DemiseParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





