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
        4,1,32,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,5,1,18,8,1,10,1,12,1,21,9,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,71,8,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,82,8,3,1,3,1,3,1,3,1,3,5,3,88,8,3,10,
        3,12,3,91,9,3,1,4,1,4,1,4,0,2,2,6,5,0,2,4,6,8,0,1,1,0,3,13,102,0,
        10,1,0,0,0,2,12,1,0,0,0,4,70,1,0,0,0,6,81,1,0,0,0,8,92,1,0,0,0,10,
        11,3,2,1,0,11,1,1,0,0,0,12,13,6,1,-1,0,13,14,3,4,2,0,14,19,1,0,0,
        0,15,16,10,1,0,0,16,18,3,4,2,0,17,15,1,0,0,0,18,21,1,0,0,0,19,17,
        1,0,0,0,19,20,1,0,0,0,20,3,1,0,0,0,21,19,1,0,0,0,22,23,5,30,0,0,
        23,24,5,15,0,0,24,25,3,6,3,0,25,26,5,27,0,0,26,71,1,0,0,0,27,28,
        5,16,0,0,28,29,3,2,1,0,29,30,5,17,0,0,30,71,1,0,0,0,31,32,5,18,0,
        0,32,33,3,6,3,0,33,34,5,19,0,0,34,35,3,4,2,0,35,71,1,0,0,0,36,37,
        5,18,0,0,37,38,3,6,3,0,38,39,5,19,0,0,39,40,3,4,2,0,40,41,5,20,0,
        0,41,42,3,4,2,0,42,71,1,0,0,0,43,44,5,21,0,0,44,45,3,6,3,0,45,46,
        5,22,0,0,46,47,3,4,2,0,47,71,1,0,0,0,48,49,5,23,0,0,49,50,5,30,0,
        0,50,51,5,11,0,0,51,52,5,31,0,0,52,53,5,28,0,0,53,54,5,31,0,0,54,
        55,5,22,0,0,55,71,3,4,2,0,56,57,5,24,0,0,57,58,5,30,0,0,58,59,5,
        28,0,0,59,60,5,31,0,0,60,61,5,22,0,0,61,71,3,4,2,0,62,63,5,25,0,
        0,63,64,5,30,0,0,64,71,5,27,0,0,65,66,5,25,0,0,66,67,5,32,0,0,67,
        68,5,26,0,0,68,69,5,30,0,0,69,71,5,27,0,0,70,22,1,0,0,0,70,27,1,
        0,0,0,70,31,1,0,0,0,70,36,1,0,0,0,70,43,1,0,0,0,70,48,1,0,0,0,70,
        56,1,0,0,0,70,62,1,0,0,0,70,65,1,0,0,0,71,5,1,0,0,0,72,73,6,3,-1,
        0,73,74,5,14,0,0,74,82,3,6,3,4,75,76,5,1,0,0,76,77,3,6,3,0,77,78,
        5,2,0,0,78,82,1,0,0,0,79,82,5,30,0,0,80,82,5,31,0,0,81,72,1,0,0,
        0,81,75,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,89,1,0,0,0,83,84,
        10,5,0,0,84,85,3,8,4,0,85,86,3,6,3,6,86,88,1,0,0,0,87,83,1,0,0,0,
        88,91,1,0,0,0,89,87,1,0,0,0,89,90,1,0,0,0,90,7,1,0,0,0,91,89,1,0,
        0,0,92,93,7,0,0,0,93,9,1,0,0,0,4,19,70,81,89
    ]

class SimpleCalculatorParser ( Parser ):

    grammarFileName = "SimpleCalculator.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'+'", "'-'", "'*'", "'/'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'^'", 
                     "'!'", "'='", "'begin'", "'end'", "'if'", "'then'", 
                     "'else'", "'while'", "'do'", "'for'", "'loop'", "'print'", 
                     "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "LPAREN", "RPAREN", "PLUS", "MINUS", 
                      "MULT", "DIV", "LT", "GT", "LTE", "GTE", "EQ", "NEQ", 
                      "EXP", "NOT", "ASGN", "BEGIN", "END", "IF", "THEN", 
                      "ELSE", "WHILE", "DO", "FOR", "LOOP", "PRINT", "COMMA", 
                      "SEMICOLON", "COLON", "WS", "ID", "INT", "STRING" ]

    RULE_program = 0
    RULE_statements = 1
    RULE_statement = 2
    RULE_expr = 3
    RULE_binop = 4

    ruleNames =  [ "program", "statements", "statement", "expr", "binop" ]

    EOF = Token.EOF
    LPAREN=1
    RPAREN=2
    PLUS=3
    MINUS=4
    MULT=5
    DIV=6
    LT=7
    GT=8
    LTE=9
    GTE=10
    EQ=11
    NEQ=12
    EXP=13
    NOT=14
    ASGN=15
    BEGIN=16
    END=17
    IF=18
    THEN=19
    ELSE=20
    WHILE=21
    DO=22
    FOR=23
    LOOP=24
    PRINT=25
    COMMA=26
    SEMICOLON=27
    COLON=28
    WS=29
    ID=30
    INT=31
    STRING=32

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

        def statements(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StatementsContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.statements(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StatementsContext,0)


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)



    def statements(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.StatementsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_statements, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.statement()
            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.StatementsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_statements)
                    self.state = 15
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 16
                    self.statement() 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)

        def ASGN(self):
            return self.getToken(SimpleCalculatorParser.ASGN, 0)

        def expr(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(SimpleCalculatorParser.SEMICOLON, 0)

        def BEGIN(self):
            return self.getToken(SimpleCalculatorParser.BEGIN, 0)

        def statements(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.StatementsContext,0)


        def END(self):
            return self.getToken(SimpleCalculatorParser.END, 0)

        def IF(self):
            return self.getToken(SimpleCalculatorParser.IF, 0)

        def THEN(self):
            return self.getToken(SimpleCalculatorParser.THEN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCalculatorParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleCalculatorParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(SimpleCalculatorParser.ELSE, 0)

        def WHILE(self):
            return self.getToken(SimpleCalculatorParser.WHILE, 0)

        def DO(self):
            return self.getToken(SimpleCalculatorParser.DO, 0)

        def FOR(self):
            return self.getToken(SimpleCalculatorParser.FOR, 0)

        def EQ(self):
            return self.getToken(SimpleCalculatorParser.EQ, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleCalculatorParser.INT)
            else:
                return self.getToken(SimpleCalculatorParser.INT, i)

        def COLON(self):
            return self.getToken(SimpleCalculatorParser.COLON, 0)

        def LOOP(self):
            return self.getToken(SimpleCalculatorParser.LOOP, 0)

        def PRINT(self):
            return self.getToken(SimpleCalculatorParser.PRINT, 0)

        def STRING(self):
            return self.getToken(SimpleCalculatorParser.STRING, 0)

        def COMMA(self):
            return self.getToken(SimpleCalculatorParser.COMMA, 0)

        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_statement

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

        localctx = SimpleCalculatorParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(SimpleCalculatorParser.ID)
                self.state = 23
                self.match(SimpleCalculatorParser.ASGN)
                self.state = 24
                self.expr(0)
                self.state = 25
                self.match(SimpleCalculatorParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.match(SimpleCalculatorParser.BEGIN)
                self.state = 28
                self.statements(0)
                self.state = 29
                self.match(SimpleCalculatorParser.END)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(SimpleCalculatorParser.IF)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(SimpleCalculatorParser.THEN)
                self.state = 34
                self.statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.match(SimpleCalculatorParser.IF)
                self.state = 37
                self.expr(0)
                self.state = 38
                self.match(SimpleCalculatorParser.THEN)
                self.state = 39
                self.statement()
                self.state = 40
                self.match(SimpleCalculatorParser.ELSE)
                self.state = 41
                self.statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.match(SimpleCalculatorParser.WHILE)
                self.state = 44
                self.expr(0)
                self.state = 45
                self.match(SimpleCalculatorParser.DO)
                self.state = 46
                self.statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(SimpleCalculatorParser.FOR)
                self.state = 49
                self.match(SimpleCalculatorParser.ID)
                self.state = 50
                self.match(SimpleCalculatorParser.EQ)
                self.state = 51
                self.match(SimpleCalculatorParser.INT)
                self.state = 52
                self.match(SimpleCalculatorParser.COLON)
                self.state = 53
                self.match(SimpleCalculatorParser.INT)
                self.state = 54
                self.match(SimpleCalculatorParser.DO)
                self.state = 55
                self.statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 56
                self.match(SimpleCalculatorParser.LOOP)
                self.state = 57
                self.match(SimpleCalculatorParser.ID)
                self.state = 58
                self.match(SimpleCalculatorParser.COLON)
                self.state = 59
                self.match(SimpleCalculatorParser.INT)
                self.state = 60
                self.match(SimpleCalculatorParser.DO)
                self.state = 61
                self.statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 62
                self.match(SimpleCalculatorParser.PRINT)
                self.state = 63
                self.match(SimpleCalculatorParser.ID)
                self.state = 64
                self.match(SimpleCalculatorParser.SEMICOLON)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 65
                self.match(SimpleCalculatorParser.PRINT)
                self.state = 66
                self.match(SimpleCalculatorParser.STRING)
                self.state = 67
                self.match(SimpleCalculatorParser.COMMA)
                self.state = 68
                self.match(SimpleCalculatorParser.ID)
                self.state = 69
                self.match(SimpleCalculatorParser.SEMICOLON)
                pass


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

        def NOT(self):
            return self.getToken(SimpleCalculatorParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleCalculatorParser.ExprContext)
            else:
                return self.getTypedRuleContext(SimpleCalculatorParser.ExprContext,i)


        def LPAREN(self):
            return self.getToken(SimpleCalculatorParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SimpleCalculatorParser.RPAREN, 0)

        def ID(self):
            return self.getToken(SimpleCalculatorParser.ID, 0)

        def INT(self):
            return self.getToken(SimpleCalculatorParser.INT, 0)

        def binop(self):
            return self.getTypedRuleContext(SimpleCalculatorParser.BinopContext,0)


        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleCalculatorParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.state = 73
                self.match(SimpleCalculatorParser.NOT)
                self.state = 74
                self.expr(4)
                pass
            elif token in [1]:
                self.state = 75
                self.match(SimpleCalculatorParser.LPAREN)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(SimpleCalculatorParser.RPAREN)
                pass
            elif token in [30]:
                self.state = 79
                self.match(SimpleCalculatorParser.ID)
                pass
            elif token in [31]:
                self.state = 80
                self.match(SimpleCalculatorParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleCalculatorParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 83
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 84
                    self.binop()
                    self.state = 85
                    self.expr(6) 
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(SimpleCalculatorParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(SimpleCalculatorParser.MINUS, 0)

        def MULT(self):
            return self.getToken(SimpleCalculatorParser.MULT, 0)

        def DIV(self):
            return self.getToken(SimpleCalculatorParser.DIV, 0)

        def LT(self):
            return self.getToken(SimpleCalculatorParser.LT, 0)

        def GT(self):
            return self.getToken(SimpleCalculatorParser.GT, 0)

        def LTE(self):
            return self.getToken(SimpleCalculatorParser.LTE, 0)

        def GTE(self):
            return self.getToken(SimpleCalculatorParser.GTE, 0)

        def EQ(self):
            return self.getToken(SimpleCalculatorParser.EQ, 0)

        def NEQ(self):
            return self.getToken(SimpleCalculatorParser.NEQ, 0)

        def EXP(self):
            return self.getToken(SimpleCalculatorParser.EXP, 0)

        def getRuleIndex(self):
            return SimpleCalculatorParser.RULE_binop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinop" ):
                listener.enterBinop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinop" ):
                listener.exitBinop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinop" ):
                return visitor.visitBinop(self)
            else:
                return visitor.visitChildren(self)




    def binop(self):

        localctx = SimpleCalculatorParser.BinopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_binop)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 16376) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.statements_sempred
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def statements_sempred(self, localctx:StatementsContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




