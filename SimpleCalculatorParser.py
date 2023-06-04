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
        4,1,26,139,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,5,0,16,8,0,10,0,12,0,19,9,0,1,1,1,1,1,1,1,1,1,1,5,1,26,8,1,
        10,1,12,1,29,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,5,1,62,8,1,10,1,12,1,65,9,1,1,1,3,1,68,8,1,1,2,1,
        2,1,2,1,2,1,2,1,2,5,2,76,8,2,10,2,12,2,79,9,2,1,3,1,3,1,3,1,3,1,
        3,1,3,5,3,87,8,3,10,3,12,3,90,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,5,4,101,8,4,10,4,12,4,104,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,5,5,115,8,5,10,5,12,5,118,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,129,8,6,1,6,1,6,1,6,5,6,134,8,6,10,6,12,6,137,9,6,
        1,6,0,5,4,6,8,10,12,7,0,2,4,6,8,10,12,0,0,151,0,17,1,0,0,0,2,67,
        1,0,0,0,4,69,1,0,0,0,6,80,1,0,0,0,8,91,1,0,0,0,10,105,1,0,0,0,12,
        128,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,19,1,0,0,0,17,15,1,0,
        0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,17,1,0,0,0,20,21,5,24,0,0,21,22,
        5,11,0,0,22,68,3,4,2,0,23,27,5,21,0,0,24,26,3,2,1,0,25,24,1,0,0,
        0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,
        1,0,0,0,30,68,5,22,0,0,31,32,5,14,0,0,32,33,3,4,2,0,33,34,5,15,0,
        0,34,37,3,2,1,0,35,36,5,16,0,0,36,38,3,2,1,0,37,35,1,0,0,0,37,38,
        1,0,0,0,38,68,1,0,0,0,39,40,5,17,0,0,40,41,3,4,2,0,41,42,5,18,0,
        0,42,43,3,2,1,0,43,68,1,0,0,0,44,45,5,19,0,0,45,46,5,24,0,0,46,47,
        5,11,0,0,47,48,5,10,0,0,48,49,5,12,0,0,49,50,5,10,0,0,50,51,5,18,
        0,0,51,68,3,2,1,0,52,53,5,20,0,0,53,54,5,24,0,0,54,55,5,12,0,0,55,
        56,5,10,0,0,56,57,5,18,0,0,57,68,3,2,1,0,58,63,5,13,0,0,59,60,5,
        25,0,0,60,62,5,23,0,0,61,59,1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,
        63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,68,5,24,0,0,67,20,1,
        0,0,0,67,23,1,0,0,0,67,31,1,0,0,0,67,39,1,0,0,0,67,44,1,0,0,0,67,
        52,1,0,0,0,67,58,1,0,0,0,68,3,1,0,0,0,69,70,6,2,-1,0,70,71,3,6,3,
        0,71,77,1,0,0,0,72,73,10,1,0,0,73,74,5,1,0,0,74,76,3,6,3,0,75,72,
        1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,5,1,0,0,0,79,
        77,1,0,0,0,80,81,6,3,-1,0,81,82,3,8,4,0,82,88,1,0,0,0,83,84,10,1,
        0,0,84,85,5,2,0,0,85,87,3,8,4,0,86,83,1,0,0,0,87,90,1,0,0,0,88,86,
        1,0,0,0,88,89,1,0,0,0,89,7,1,0,0,0,90,88,1,0,0,0,91,92,6,4,-1,0,
        92,93,3,10,5,0,93,102,1,0,0,0,94,95,10,2,0,0,95,96,5,5,0,0,96,101,
        3,10,5,0,97,98,10,1,0,0,98,99,5,6,0,0,99,101,3,10,5,0,100,94,1,0,
        0,0,100,97,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,
        0,103,9,1,0,0,0,104,102,1,0,0,0,105,106,6,5,-1,0,106,107,3,12,6,
        0,107,116,1,0,0,0,108,109,10,2,0,0,109,110,5,7,0,0,110,115,3,12,
        6,0,111,112,10,1,0,0,112,113,5,8,0,0,113,115,3,12,6,0,114,108,1,
        0,0,0,114,111,1,0,0,0,115,118,1,0,0,0,116,114,1,0,0,0,116,117,1,
        0,0,0,117,11,1,0,0,0,118,116,1,0,0,0,119,120,6,6,-1,0,120,129,5,
        10,0,0,121,122,5,6,0,0,122,129,3,12,6,4,123,129,5,24,0,0,124,125,
        5,3,0,0,125,126,3,4,2,0,126,127,5,4,0,0,127,129,1,0,0,0,128,119,
        1,0,0,0,128,121,1,0,0,0,128,123,1,0,0,0,128,124,1,0,0,0,129,135,
        1,0,0,0,130,131,10,2,0,0,131,132,5,9,0,0,132,134,5,10,0,0,133,130,
        1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,13,1,
        0,0,0,137,135,1,0,0,0,13,17,27,37,63,67,77,88,100,102,114,116,128,
        135
    ]

class SimpleCalculatorParser ( Parser ):

    grammarFileName = "SimpleCalculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'^'", "<INVALID>", "'='", 
                     "':'", "'print'", "'if'", "'then'", "'else'", "'while'", 
                     "'do'", "'for'", "'loop'", "'begin'", "'end'", "','" ]

    symbolicNames = [ "<INVALID>", "BOOL", "BINOP", "OPENP", "CLOSEP", "PLUS", 
                      "MINUS", "MULT", "DIV", "POWER", "Number", "EQ", "COLON", 
                      "PRINT", "IF", "THEN", "ELSE", "WHILE", "DO", "FOR", 
                      "LOOP", "Begin", "END", "COMMA", "ID", "SL", "WS" ]

    RULE_program = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_bin = 3
    RULE_mathematical = 4
    RULE_term = 5
    RULE_factor = 6

    ruleNames =  [ "program", "stmt", "expr", "bin", "mathematical", "term", 
                   "factor" ]

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
    Number=10
    EQ=11
    COLON=12
    PRINT=13
    IF=14
    THEN=15
    ELSE=16
    WHILE=17
    DO=18
    FOR=19
    LOOP=20
    Begin=21
    END=22
    COMMA=23
    ID=24
    SL=25
    WS=26

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
            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 20602880) != 0):
                self.state = 14
                self.stmt()
                self.state = 19
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
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = SimpleCalculatorParser.VariableDeclaration_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.match(SimpleCalculatorParser.ID)
                self.state = 21
                self.match(SimpleCalculatorParser.EQ)
                self.state = 22
                self.expr(0)
                pass
            elif token in [21]:
                localctx = SimpleCalculatorParser.BeginEnd_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(SimpleCalculatorParser.Begin)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 20602880) != 0):
                    self.state = 24
                    self.stmt()
                    self.state = 29
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 30
                self.match(SimpleCalculatorParser.END)
                pass
            elif token in [14]:
                localctx = SimpleCalculatorParser.IfElse_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(SimpleCalculatorParser.IF)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(SimpleCalculatorParser.THEN)
                self.state = 34
                self.stmt()
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.match(SimpleCalculatorParser.ELSE)
                    self.state = 36
                    self.stmt()


                pass
            elif token in [17]:
                localctx = SimpleCalculatorParser.WhileDo_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(SimpleCalculatorParser.WHILE)
                self.state = 40
                self.expr(0)
                self.state = 41
                self.match(SimpleCalculatorParser.DO)
                self.state = 42
                self.stmt()
                pass
            elif token in [19]:
                localctx = SimpleCalculatorParser.ForDo_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 44
                self.match(SimpleCalculatorParser.FOR)
                self.state = 45
                self.match(SimpleCalculatorParser.ID)
                self.state = 46
                self.match(SimpleCalculatorParser.EQ)
                self.state = 47
                self.match(SimpleCalculatorParser.Number)
                self.state = 48
                self.match(SimpleCalculatorParser.COLON)
                self.state = 49
                self.match(SimpleCalculatorParser.Number)
                self.state = 50
                self.match(SimpleCalculatorParser.DO)
                self.state = 51
                self.stmt()
                pass
            elif token in [20]:
                localctx = SimpleCalculatorParser.LoopDo_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 52
                self.match(SimpleCalculatorParser.LOOP)
                self.state = 53
                self.match(SimpleCalculatorParser.ID)
                self.state = 54
                self.match(SimpleCalculatorParser.COLON)
                self.state = 55
                self.match(SimpleCalculatorParser.Number)
                self.state = 56
                self.match(SimpleCalculatorParser.DO)
                self.state = 57
                self.stmt()
                pass
            elif token in [13]:
                localctx = SimpleCalculatorParser.Print_StatementContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.match(SimpleCalculatorParser.PRINT)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 59
                    self.match(SimpleCalculatorParser.SL)
                    self.state = 60
                    self.match(SimpleCalculatorParser.COMMA)
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self.match(SimpleCalculatorParser.ID)
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

            self.state = 70
            self.bin_(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 77
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.Expr_boolContext(self, SimpleCalculatorParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 72
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 73
                    self.match(SimpleCalculatorParser.BOOL)
                    self.state = 74
                    self.bin_(0) 
                self.state = 79
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

            self.state = 81
            self.mathematical(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 88
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.Bin_binopContext(self, SimpleCalculatorParser.BinContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_bin)
                    self.state = 83
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 84
                    self.match(SimpleCalculatorParser.BINOP)
                    self.state = 85
                    self.mathematical(0) 
                self.state = 90
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

            self.state = 92
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 102
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 100
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SimpleCalculatorParser.Mathematical_plusContext(self, SimpleCalculatorParser.MathematicalContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mathematical)
                        self.state = 94
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 95
                        self.match(SimpleCalculatorParser.PLUS)
                        self.state = 96
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleCalculatorParser.Mathematical_minusContext(self, SimpleCalculatorParser.MathematicalContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_mathematical)
                        self.state = 97
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 98
                        self.match(SimpleCalculatorParser.MINUS)
                        self.state = 99
                        self.term(0)
                        pass

             
                self.state = 104
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

            self.state = 106
            self.factor(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 116
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 114
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = SimpleCalculatorParser.Term_multContext(self, SimpleCalculatorParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 108
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 109
                        self.match(SimpleCalculatorParser.MULT)
                        self.state = 110
                        self.factor(0)
                        pass

                    elif la_ == 2:
                        localctx = SimpleCalculatorParser.Term_divContext(self, SimpleCalculatorParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 111
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 112
                        self.match(SimpleCalculatorParser.DIV)
                        self.state = 113
                        self.factor(0)
                        pass

             
                self.state = 118
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


    class Factor_minus_numberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(SimpleCalculatorParser.MINUS, 0)
        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_minus_number" ):
                listener.enterFactor_minus_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_minus_number" ):
                listener.exitFactor_minus_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_minus_number" ):
                return visitor.visitFactor_minus_number(self)
            else:
                return visitor.visitChildren(self)


    class Factor_idContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_id" ):
                listener.enterFactor_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_id" ):
                listener.exitFactor_id(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_id" ):
                return visitor.visitFactor_id(self)
            else:
                return visitor.visitChildren(self)


    class Factor_powerContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def factor(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.FactorContext,0)

        def POWER(self):
            return self.getToken(SimpleCalculatorParser.POWER, 0)
        def Number(self):
            return self.getToken(SimpleCalculatorParser.Number, 0)

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


    class Factor_exprContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OPENP(self):
            return self.getToken(SimpleCalculatorParser.OPENP, 0)
        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)

        def CLOSEP(self):
            return self.getToken(SimpleCalculatorParser.CLOSEP, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_expr" ):
                listener.enterFactor_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_expr" ):
                listener.exitFactor_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_expr" ):
                return visitor.visitFactor_expr(self)
            else:
                return visitor.visitChildren(self)


    class Factor_numberContext(FactorContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleCalculatorParser.FactorContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Number(self):
            return self.getToken(SimpleCalculatorParser.Number, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor_number" ):
                listener.enterFactor_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor_number" ):
                listener.exitFactor_number(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor_number" ):
                return visitor.visitFactor_number(self)
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
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                localctx = SimpleCalculatorParser.Factor_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 120
                self.match(SimpleCalculatorParser.Number)
                pass
            elif token in [6]:
                localctx = SimpleCalculatorParser.Factor_minus_numberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(SimpleCalculatorParser.MINUS)
                self.state = 122
                self.factor(4)
                pass
            elif token in [24]:
                localctx = SimpleCalculatorParser.Factor_idContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.match(SimpleCalculatorParser.ID)
                pass
            elif token in [3]:
                localctx = SimpleCalculatorParser.Factor_exprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(SimpleCalculatorParser.OPENP)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(SimpleCalculatorParser.CLOSEP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 135
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
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 131
                    self.match(SimpleCalculatorParser.POWER)
                    self.state = 132
                    self.match(SimpleCalculatorParser.Number) 
                self.state = 137
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         

    def factor_sempred(self, localctx:FactorContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




