# Generated from SimpleCalculator.g4 by ANTLR 4.13.0
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
        4,1,28,153,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,
        1,42,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,66,8,1,10,1,12,1,69,9,1,1,1,
        1,1,3,1,73,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,81,8,2,10,2,12,2,84,9,
        2,1,3,1,3,1,3,1,3,1,3,1,3,5,3,92,8,3,10,3,12,3,95,9,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,106,8,4,10,4,12,4,109,9,4,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,5,5,123,8,5,10,5,12,5,126,
        9,5,1,6,1,6,1,6,1,6,1,6,1,6,4,6,134,8,6,11,6,12,6,135,5,6,138,8,
        6,10,6,12,6,141,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,151,8,7,
        1,7,0,5,4,6,8,10,12,8,0,2,4,6,8,10,12,14,0,0,166,0,19,1,0,0,0,2,
        72,1,0,0,0,4,74,1,0,0,0,6,85,1,0,0,0,8,96,1,0,0,0,10,110,1,0,0,0,
        12,127,1,0,0,0,14,150,1,0,0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,21,
        1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,1,0,0,0,21,19,1,0,0,0,22,
        23,5,26,0,0,23,24,5,12,0,0,24,25,3,4,2,0,25,26,5,25,0,0,26,73,1,
        0,0,0,27,31,5,22,0,0,28,30,3,2,1,0,29,28,1,0,0,0,30,33,1,0,0,0,31,
        29,1,0,0,0,31,32,1,0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,73,5,23,
        0,0,35,36,5,15,0,0,36,37,3,4,2,0,37,38,5,16,0,0,38,41,3,2,1,0,39,
        40,5,17,0,0,40,42,3,2,1,0,41,39,1,0,0,0,41,42,1,0,0,0,42,73,1,0,
        0,0,43,44,5,18,0,0,44,45,3,4,2,0,45,46,5,19,0,0,46,47,3,2,1,0,47,
        73,1,0,0,0,48,49,5,20,0,0,49,50,5,26,0,0,50,51,5,12,0,0,51,52,5,
        11,0,0,52,53,5,13,0,0,53,54,5,11,0,0,54,55,5,19,0,0,55,73,3,2,1,
        0,56,57,5,21,0,0,57,58,5,26,0,0,58,59,5,13,0,0,59,60,5,11,0,0,60,
        61,5,19,0,0,61,73,3,2,1,0,62,67,5,14,0,0,63,64,5,27,0,0,64,66,5,
        24,0,0,65,63,1,0,0,0,66,69,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,
        70,1,0,0,0,69,67,1,0,0,0,70,71,5,26,0,0,71,73,5,25,0,0,72,22,1,0,
        0,0,72,27,1,0,0,0,72,35,1,0,0,0,72,43,1,0,0,0,72,48,1,0,0,0,72,56,
        1,0,0,0,72,62,1,0,0,0,73,3,1,0,0,0,74,75,6,2,-1,0,75,76,3,6,3,0,
        76,82,1,0,0,0,77,78,10,1,0,0,78,79,5,1,0,0,79,81,3,6,3,0,80,77,1,
        0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,5,1,0,0,0,84,
        82,1,0,0,0,85,86,6,3,-1,0,86,87,3,8,4,0,87,93,1,0,0,0,88,89,10,1,
        0,0,89,90,5,2,0,0,90,92,3,8,4,0,91,88,1,0,0,0,92,95,1,0,0,0,93,91,
        1,0,0,0,93,94,1,0,0,0,94,7,1,0,0,0,95,93,1,0,0,0,96,97,6,4,-1,0,
        97,98,3,10,5,0,98,107,1,0,0,0,99,100,10,2,0,0,100,101,5,5,0,0,101,
        106,3,10,5,0,102,103,10,1,0,0,103,104,5,6,0,0,104,106,3,10,5,0,105,
        99,1,0,0,0,105,102,1,0,0,0,106,109,1,0,0,0,107,105,1,0,0,0,107,108,
        1,0,0,0,108,9,1,0,0,0,109,107,1,0,0,0,110,111,6,5,-1,0,111,112,3,
        12,6,0,112,124,1,0,0,0,113,114,10,3,0,0,114,115,5,7,0,0,115,123,
        3,12,6,0,116,117,10,2,0,0,117,118,5,8,0,0,118,123,3,12,6,0,119,120,
        10,1,0,0,120,121,5,10,0,0,121,123,3,12,6,0,122,113,1,0,0,0,122,116,
        1,0,0,0,122,119,1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,
        1,0,0,0,125,11,1,0,0,0,126,124,1,0,0,0,127,128,6,6,-1,0,128,129,
        3,14,7,0,129,139,1,0,0,0,130,133,10,1,0,0,131,132,5,9,0,0,132,134,
        3,14,7,0,133,131,1,0,0,0,134,135,1,0,0,0,135,133,1,0,0,0,135,136,
        1,0,0,0,136,138,1,0,0,0,137,130,1,0,0,0,138,141,1,0,0,0,139,137,
        1,0,0,0,139,140,1,0,0,0,140,13,1,0,0,0,141,139,1,0,0,0,142,151,5,
        11,0,0,143,144,5,6,0,0,144,151,3,14,7,0,145,151,5,26,0,0,146,147,
        5,3,0,0,147,148,3,4,2,0,148,149,5,4,0,0,149,151,1,0,0,0,150,142,
        1,0,0,0,150,143,1,0,0,0,150,145,1,0,0,0,150,146,1,0,0,0,151,15,1,
        0,0,0,14,19,31,41,67,72,82,93,105,107,122,124,135,139,150
    ]

class SimpleCalculatorParser ( Parser ):

    grammarFileName = "SimpleCalculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "'%'", "<INVALID>", 
                     "'='", "':'", "'print'", "'if'", "'then'", "'else'", 
                     "'while'", "'do'", "'for'", "'loop'", "'begin'", "'end'", 
                     "','", "';'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "BINOP", "OPENP", "CLOSEP", "PLUS", 
                      "MINUS", "MULT", "DIV", "POWER", "MOD", "Number", 
                      "EQ", "COLON", "PRINT", "IF", "THEN", "ELSE", "WHILE", 
                      "DO", "FOR", "LOOP", "Begin", "END", "COMMA", "SEMICOLON", 
                      "ID", "SL", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_bin = 3
    RULE_mathematical = 4
    RULE_term = 5
    RULE_factor = 6
    RULE_finalfactor = 7

    ruleNames =  [ "program", "stmt", "expr", "bin", "mathematical", "term", 
                   "factor", "finalfactor" ]

    EOF = Token.EOF
    BOOL=1
    BINOP=2
    OPENP=3
    CLOSEP=4
    PLUS=5
    MINUS=6
    MULT=7
    DIV=8
    POWER=9
    MOD=10
    Number=11
    EQ=12
    COLON=13
    PRINT=14
    IF=15
    THEN=16
    ELSE=17
    WHILE=18
    DO=19
    FOR=20
    LOOP=21
    Begin=22
    END=23
    COMMA=24
    SEMICOLON=25
    ID=26
    SL=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCalculatorParser.StmtContext)
            else:
                return self.getTypedRuleContext(SimpleCalculatorParser.StmtContext,i)


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_program

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

        localctx = SimpleCalculatorParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 74760192) != 0):
                self.state = 16
                self.stmt()
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return SimpleCalculatorParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class WhileDo_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def WHILE(self):
            return self.getToken(SimpleCalculatorParser.WHILE, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)

        def DO(self):
            return self.getToken(SimpleCalculatorParser.DO, 0)
        def stmt(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileDo_Statement" ):
                listener.enterWhileDo_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileDo_Statement" ):
                listener.exitWhileDo_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileDo_Statement" ):
                return visitor.visitWhileDo_Statement(self)
            else:
                return visitor.visitChildren(self)


    class LoopDo_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LOOP(self):
            return self.getToken(SimpleCalculatorParser.LOOP, 0)
        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)
        def COLON(self):
            return self.getToken(SimpleCalculatorParser.COLON, 0)
        def Number(self):
            return self.getToken(SimpleCalculatorParser.Number, 0)
        def DO(self):
            return self.getToken(SimpleCalculatorParser.DO, 0)
        def stmt(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoopDo_Statement" ):
                listener.enterLoopDo_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoopDo_Statement" ):
                listener.exitLoopDo_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoopDo_Statement" ):
                return visitor.visitLoopDo_Statement(self)
            else:
                return visitor.visitChildren(self)


    class VariableDeclaration_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)
        def EQ(self):
            return self.getToken(SimpleCalculatorParser.EQ, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)

        def SEMICOLON(self):
            return self.getToken(SimpleCalculatorParser.SEMICOLON, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration_Statement" ):
                listener.enterVariableDeclaration_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration_Statement" ):
                listener.exitVariableDeclaration_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableDeclaration_Statement" ):
                return visitor.visitVariableDeclaration_Statement(self)
            else:
                return visitor.visitChildren(self)


    class IfElse_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(SimpleCalculatorParser.IF, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)

        def THEN(self):
            return self.getToken(SimpleCalculatorParser.THEN, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCalculatorParser.StmtContext)
            else:
                return self.getTypedRuleContext(SimpleCalculatorParser.StmtContext,i)

        def ELSE(self):
            return self.getToken(SimpleCalculatorParser.ELSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse_Statement" ):
                listener.enterIfElse_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse_Statement" ):
                listener.exitIfElse_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfElse_Statement" ):
                return visitor.visitIfElse_Statement(self)
            else:
                return visitor.visitChildren(self)


    class ForDo_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(SimpleCalculatorParser.FOR, 0)
        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)
        def EQ(self):
            return self.getToken(SimpleCalculatorParser.EQ, 0)
        def Number(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCalculatorParser.Number)
            else:
                return self.getToken(SimpleCalculatorParser.Number, i)
        def COLON(self):
            return self.getToken(SimpleCalculatorParser.COLON, 0)
        def DO(self):
            return self.getToken(SimpleCalculatorParser.DO, 0)
        def stmt(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForDo_Statement" ):
                listener.enterForDo_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForDo_Statement" ):
                listener.exitForDo_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForDo_Statement" ):
                return visitor.visitForDo_Statement(self)
            else:
                return visitor.visitChildren(self)


    class BeginEnd_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Begin(self):
            return self.getToken(SimpleCalculatorParser.Begin, 0)
        def END(self):
            return self.getToken(SimpleCalculatorParser.END, 0)
        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCalculatorParser.StmtContext)
            else:
                return self.getTypedRuleContext(SimpleCalculatorParser.StmtContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBeginEnd_Statement" ):
                listener.enterBeginEnd_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBeginEnd_Statement" ):
                listener.exitBeginEnd_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBeginEnd_Statement" ):
                return visitor.visitBeginEnd_Statement(self)
            else:
                return visitor.visitChildren(self)


    class Print_StatementContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(SimpleCalculatorParser.PRINT, 0)
        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)
        def SEMICOLON(self):
            return self.getToken(SimpleCalculatorParser.SEMICOLON, 0)
        def SL(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCalculatorParser.SL)
            else:
                return self.getToken(SimpleCalculatorParser.SL, i)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCalculatorParser.COMMA)
            else:
                return self.getToken(SimpleCalculatorParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_Statement" ):
                listener.enterPrint_Statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_Statement" ):
                listener.exitPrint_Statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_Statement" ):
                return visitor.visitPrint_Statement(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = SimpleCalculatorParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        self._la = 0 # Token type
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                localctx = SimpleCalculatorParser.VariableDeclaration_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(SimpleCalculatorParser.ID)
                self.state = 23
                self.match(SimpleCalculatorParser.EQ)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(SimpleCalculatorParser.SEMICOLON)
                pass
            elif token in [22]:
                localctx = SimpleCalculatorParser.BeginEnd_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(SimpleCalculatorParser.Begin)
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 74760192) != 0):
                    self.state = 28
                    self.stmt()
                    self.state = 33
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 34
                self.match(SimpleCalculatorParser.END)
                pass
            elif token in [15]:
                localctx = SimpleCalculatorParser.IfElse_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(SimpleCalculatorParser.IF)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(SimpleCalculatorParser.THEN)
                self.state = 38
                self.stmt()
                self.state = 41
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 39
                    self.match(SimpleCalculatorParser.ELSE)
                    self.state = 40
                    self.stmt()


                pass
            elif token in [18]:
                localctx = SimpleCalculatorParser.WhileDo_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(SimpleCalculatorParser.WHILE)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(SimpleCalculatorParser.DO)
                self.state = 46
                self.stmt()
                pass
            elif token in [20]:
                localctx = SimpleCalculatorParser.ForDo_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(SimpleCalculatorParser.FOR)
                self.state = 49
                self.match(SimpleCalculatorParser.ID)
                self.state = 50
                self.match(SimpleCalculatorParser.EQ)
                self.state = 51
                self.match(SimpleCalculatorParser.Number)
                self.state = 52
                self.match(SimpleCalculatorParser.COLON)
                self.state = 53
                self.match(SimpleCalculatorParser.Number)
                self.state = 54
                self.match(SimpleCalculatorParser.DO)
                self.state = 55
                self.stmt()
                pass
            elif token in [21]:
                localctx = SimpleCalculatorParser.LoopDo_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 56
                self.match(SimpleCalculatorParser.LOOP)
                self.state = 57
                self.match(SimpleCalculatorParser.ID)
                self.state = 58
                self.match(SimpleCalculatorParser.COLON)
                self.state = 59
                self.match(SimpleCalculatorParser.Number)
                self.state = 60
                self.match(SimpleCalculatorParser.DO)
                self.state = 61
                self.stmt()
                pass
            elif token in [14]:
                localctx = SimpleCalculatorParser.Print_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.match(SimpleCalculatorParser.PRINT)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==27:
                    self.state = 63
                    self.match(SimpleCalculatorParser.SL)
                    self.state = 64
                    self.match(SimpleCalculatorParser.COMMA)
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 70
                self.match(SimpleCalculatorParser.ID)
                self.state = 71
                self.match(SimpleCalculatorParser.SEMICOLON)
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
            return SimpleCalculatorParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Expr_binContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bin_(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.BinContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_bin" ):
                listener.enterExpr_bin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_bin" ):
                listener.exitExpr_bin(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_bin" ):
                return visitor.visitExpr_bin(self)
            else:
                return visitor.visitChildren(self)


    class Expr_boolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)

        def BOOL(self):
            return self.getToken(SimpleCalculatorParser.BOOL, 0)
        def bin_(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.BinContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_bool" ):
                listener.enterExpr_bool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_bool" ):
                listener.exitExpr_bool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_bool" ):
                return visitor.visitExpr_bool(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleCalculatorParser.Expr_binContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 75
            self.bin_(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.Expr_boolContext(self, SimpleCalculatorParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 77
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 78
                    self.match(SimpleCalculatorParser.BOOL)
                    self.state = 79
                    self.bin_(0) 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_bin

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Bin_mathematicalContext(BinContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.BinContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mathematical(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.MathematicalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_mathematical" ):
                listener.enterBin_mathematical(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_mathematical" ):
                listener.exitBin_mathematical(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_mathematical" ):
                return visitor.visitBin_mathematical(self)
            else:
                return visitor.visitChildren(self)


    class Bin_binopContext(BinContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.BinContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def bin_(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.BinContext,0)

        def BINOP(self):
            return self.getToken(SimpleCalculatorParser.BINOP, 0)
        def mathematical(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.MathematicalContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBin_binop" ):
                listener.enterBin_binop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBin_binop" ):
                listener.exitBin_binop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBin_binop" ):
                return visitor.visitBin_binop(self)
            else:
                return visitor.visitChildren(self)



    def bin_(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.BinContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_bin, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleCalculatorParser.Bin_mathematicalContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 86
            self.mathematical(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.Bin_binopContext(self, SimpleCalculatorParser.BinContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bin)
                    self.state = 88
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 89
                    self.match(SimpleCalculatorParser.BINOP)
                    self.state = 90
                    self.mathematical(0) 
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MathematicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_mathematical

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Mathematical_minusContext(MathematicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.MathematicalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mathematical(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.MathematicalContext,0)

        def MINUS(self):
            return self.getToken(SimpleCalculatorParser.MINUS, 0)
        def term(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathematical_minus" ):
                listener.enterMathematical_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathematical_minus" ):
                listener.exitMathematical_minus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathematical_minus" ):
                return visitor.visitMathematical_minus(self)
            else:
                return visitor.visitChildren(self)


    class Mathematical_termContext(MathematicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.MathematicalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathematical_term" ):
                listener.enterMathematical_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathematical_term" ):
                listener.exitMathematical_term(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathematical_term" ):
                return visitor.visitMathematical_term(self)
            else:
                return visitor.visitChildren(self)


    class Mathematical_plusContext(MathematicalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.MathematicalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mathematical(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.MathematicalContext,0)

        def PLUS(self):
            return self.getToken(SimpleCalculatorParser.PLUS, 0)
        def term(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMathematical_plus" ):
                listener.enterMathematical_plus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMathematical_plus" ):
                listener.exitMathematical_plus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMathematical_plus" ):
                return visitor.visitMathematical_plus(self)
            else:
                return visitor.visitChildren(self)



    def mathematical(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.MathematicalContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_mathematical, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleCalculatorParser.Mathematical_termContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 97
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 107
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 105
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SimpleCalculatorParser.Mathematical_plusContext(self, SimpleCalculatorParser.MathematicalContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mathematical)
                        self.state = 99
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 100
                        self.match(SimpleCalculatorParser.PLUS)
                        self.state = 101
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleCalculatorParser.Mathematical_minusContext(self, SimpleCalculatorParser.MathematicalContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mathematical)
                        self.state = 102
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 103
                        self.match(SimpleCalculatorParser.MINUS)
                        self.state = 104
                        self.term(0)
                        pass

             
                self.state = 109
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Term_factorContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_factor" ):
                listener.enterTerm_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_factor" ):
                listener.exitTerm_factor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_factor" ):
                return visitor.visitTerm_factor(self)
            else:
                return visitor.visitChildren(self)


    class Term_divContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.TermContext,0)

        def DIV(self):
            return self.getToken(SimpleCalculatorParser.DIV, 0)
        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_div" ):
                listener.enterTerm_div(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_div" ):
                listener.exitTerm_div(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_div" ):
                return visitor.visitTerm_div(self)
            else:
                return visitor.visitChildren(self)


    class Term_modContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.TermContext,0)

        def MOD(self):
            return self.getToken(SimpleCalculatorParser.MOD, 0)
        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_mod" ):
                listener.enterTerm_mod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_mod" ):
                listener.exitTerm_mod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_mod" ):
                return visitor.visitTerm_mod(self)
            else:
                return visitor.visitChildren(self)


    class Term_multContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.TermContext,0)

        def MULT(self):
            return self.getToken(SimpleCalculatorParser.MULT, 0)
        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm_mult" ):
                listener.enterTerm_mult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm_mult" ):
                listener.exitTerm_mult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm_mult" ):
                return visitor.visitTerm_mult(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleCalculatorParser.Term_factorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 111
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 124
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 122
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = SimpleCalculatorParser.Term_multContext(self, SimpleCalculatorParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 113
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 114
                        self.match(SimpleCalculatorParser.MULT)
                        self.state = 115
                        self.factor(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleCalculatorParser.Term_divContext(self, SimpleCalculatorParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 116
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 117
                        self.match(SimpleCalculatorParser.DIV)
                        self.state = 118
                        self.factor(0)
                        pass

                    elif la_ == 3:
                        localctx = SimpleCalculatorParser.Term_modContext(self, SimpleCalculatorParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 119
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 120
                        self.match(SimpleCalculatorParser.MOD)
                        self.state = 121
                        self.factor(0)
                        pass

             
                self.state = 126
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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
            return SimpleCalculatorParser.RULE_factor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class Factor_powerContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)

        def POWER(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCalculatorParser.POWER)
            else:
                return self.getToken(SimpleCalculatorParser.POWER, i)
        def finalfactor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCalculatorParser.FinalfactorContext)
            else:
                return self.getTypedRuleContext(SimpleCalculatorParser.FinalfactorContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_power" ):
                listener.enterFactor_power(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_power" ):
                listener.exitFactor_power(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_power" ):
                return visitor.visitFactor_power(self)
            else:
                return visitor.visitChildren(self)


    class Factor_finalfactorContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def finalfactor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FinalfactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_finalfactor" ):
                listener.enterFactor_finalfactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_finalfactor" ):
                listener.exitFactor_finalfactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_finalfactor" ):
                return visitor.visitFactor_finalfactor(self)
            else:
                return visitor.visitChildren(self)



    def factor(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.FactorContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_factor, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = SimpleCalculatorParser.Factor_finalfactorContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 128
            self.finalfactor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.Factor_powerContext(self, SimpleCalculatorParser.FactorContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_factor)
                    self.state = 130
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 133 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 131
                            self.match(SimpleCalculatorParser.POWER)
                            self.state = 132
                            self.finalfactor()

                        else:
                            raise NoViableAltException(self)
                        self.state = 135 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
             
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FinalfactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_finalfactor

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Finalfactor_idContext(FinalfactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FinalfactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalfactor_id" ):
                listener.enterFinalfactor_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalfactor_id" ):
                listener.exitFinalfactor_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinalfactor_id" ):
                return visitor.visitFinalfactor_id(self)
            else:
                return visitor.visitChildren(self)


    class Finalfactor_minus_numberContext(FinalfactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FinalfactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SimpleCalculatorParser.MINUS, 0)
        def finalfactor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FinalfactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalfactor_minus_number" ):
                listener.enterFinalfactor_minus_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalfactor_minus_number" ):
                listener.exitFinalfactor_minus_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinalfactor_minus_number" ):
                return visitor.visitFinalfactor_minus_number(self)
            else:
                return visitor.visitChildren(self)


    class Finalfactor_numberContext(FinalfactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FinalfactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(SimpleCalculatorParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalfactor_number" ):
                listener.enterFinalfactor_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalfactor_number" ):
                listener.exitFinalfactor_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinalfactor_number" ):
                return visitor.visitFinalfactor_number(self)
            else:
                return visitor.visitChildren(self)


    class Finalfactor_exprContext(FinalfactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FinalfactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPENP(self):
            return self.getToken(SimpleCalculatorParser.OPENP, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)

        def CLOSEP(self):
            return self.getToken(SimpleCalculatorParser.CLOSEP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinalfactor_expr" ):
                listener.enterFinalfactor_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinalfactor_expr" ):
                listener.exitFinalfactor_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinalfactor_expr" ):
                return visitor.visitFinalfactor_expr(self)
            else:
                return visitor.visitChildren(self)



    def finalfactor(self):

        localctx = SimpleCalculatorParser.FinalfactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_finalfactor)
        try:
            self.state = 150
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                localctx = SimpleCalculatorParser.Finalfactor_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(SimpleCalculatorParser.Number)
                pass
            elif token in [6]:
                localctx = SimpleCalculatorParser.Finalfactor_minus_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(SimpleCalculatorParser.MINUS)
                self.state = 144
                self.finalfactor()
                pass
            elif token in [26]:
                localctx = SimpleCalculatorParser.Finalfactor_idContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(SimpleCalculatorParser.ID)
                pass
            elif token in [3]:
                localctx = SimpleCalculatorParser.Finalfactor_exprContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.match(SimpleCalculatorParser.OPENP)
                self.state = 147
                self.expr(0)
                self.state = 148
                self.match(SimpleCalculatorParser.CLOSEP)
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
        self._predicates[3] = self.bin_sempred
        self._predicates[4] = self.mathematical_sempred
        self._predicates[5] = self.term_sempred
        self._predicates[6] = self.factor_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def bin_sempred(self, localctx:BinContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def mathematical_sempred(self, localctx:MathematicalContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 1)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 1)
         




