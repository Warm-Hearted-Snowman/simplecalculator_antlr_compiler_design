# Generated from SimpleCalculator.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SimpleCalculatorParser import SimpleCalculatorParser
else:
    from SimpleCalculatorParser import SimpleCalculatorParser

# This class defines a complete generic visitor for a parse tree produced by SimpleCalculatorParser.

class SimpleCalculatorVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleCalculatorParser#program.
    def visitProgram(self, ctx:SimpleCalculatorParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#statements.
    def visitStatements(self, ctx:SimpleCalculatorParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#statement.
    def visitStatement(self, ctx:SimpleCalculatorParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#expr.
    def visitExpr(self, ctx:SimpleCalculatorParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#binop.
    def visitBinop(self, ctx:SimpleCalculatorParser.BinopContext):
        return self.visitChildren(ctx)



del SimpleCalculatorParser