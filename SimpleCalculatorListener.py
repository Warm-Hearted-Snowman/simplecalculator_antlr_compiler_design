# Generated from SimpleCalculator.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleCalculatorParser import SimpleCalculatorParser
else:
    from SimpleCalculatorParser import SimpleCalculatorParser

# This class defines a complete listener for a parse tree produced by SimpleCalculatorParser.
class SimpleCalculatorListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleCalculatorParser#program.
    def enterProgram(self, ctx:SimpleCalculatorParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#program.
    def exitProgram(self, ctx:SimpleCalculatorParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#statements.
    def enterStatements(self, ctx:SimpleCalculatorParser.StatementsContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#statements.
    def exitStatements(self, ctx:SimpleCalculatorParser.StatementsContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#statement.
    def enterStatement(self, ctx:SimpleCalculatorParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#statement.
    def exitStatement(self, ctx:SimpleCalculatorParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#expr.
    def enterExpr(self, ctx:SimpleCalculatorParser.ExprContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#expr.
    def exitExpr(self, ctx:SimpleCalculatorParser.ExprContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#binop.
    def enterBinop(self, ctx:SimpleCalculatorParser.BinopContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#binop.
    def exitBinop(self, ctx:SimpleCalculatorParser.BinopContext):
        pass



del SimpleCalculatorParser