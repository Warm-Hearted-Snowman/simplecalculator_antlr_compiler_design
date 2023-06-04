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


    # Visit a parse tree produced by SimpleCalculatorParser#variableDeclaration_Statement.
    def visitVariableDeclaration_Statement(self, ctx:SimpleCalculatorParser.VariableDeclaration_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#beginEnd_Statement.
    def visitBeginEnd_Statement(self, ctx:SimpleCalculatorParser.BeginEnd_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#ifElse_Statement.
    def visitIfElse_Statement(self, ctx:SimpleCalculatorParser.IfElse_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#whileDo_Statement.
    def visitWhileDo_Statement(self, ctx:SimpleCalculatorParser.WhileDo_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#forDo_Statement.
    def visitForDo_Statement(self, ctx:SimpleCalculatorParser.ForDo_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#loopDo_Statement.
    def visitLoopDo_Statement(self, ctx:SimpleCalculatorParser.LoopDo_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#print_Statement.
    def visitPrint_Statement(self, ctx:SimpleCalculatorParser.Print_StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#expr_bin.
    def visitExpr_bin(self, ctx:SimpleCalculatorParser.Expr_binContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#expr_bool.
    def visitExpr_bool(self, ctx:SimpleCalculatorParser.Expr_boolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#bin_mathematical.
    def visitBin_mathematical(self, ctx:SimpleCalculatorParser.Bin_mathematicalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#bin_binop.
    def visitBin_binop(self, ctx:SimpleCalculatorParser.Bin_binopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#mathematical_minus.
    def visitMathematical_minus(self, ctx:SimpleCalculatorParser.Mathematical_minusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#mathematical_term.
    def visitMathematical_term(self, ctx:SimpleCalculatorParser.Mathematical_termContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#mathematical_plus.
    def visitMathematical_plus(self, ctx:SimpleCalculatorParser.Mathematical_plusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#term_factor.
    def visitTerm_factor(self, ctx:SimpleCalculatorParser.Term_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#term_div.
    def visitTerm_div(self, ctx:SimpleCalculatorParser.Term_divContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#term_mult.
    def visitTerm_mult(self, ctx:SimpleCalculatorParser.Term_multContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#factor_minus_number.
    def visitFactor_minus_number(self, ctx:SimpleCalculatorParser.Factor_minus_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#factor_id.
    def visitFactor_id(self, ctx:SimpleCalculatorParser.Factor_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#factor_power.
    def visitFactor_power(self, ctx:SimpleCalculatorParser.Factor_powerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#factor_expr.
    def visitFactor_expr(self, ctx:SimpleCalculatorParser.Factor_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleCalculatorParser#factor_number.
    def visitFactor_number(self, ctx:SimpleCalculatorParser.Factor_numberContext):
        return self.visitChildren(ctx)



del SimpleCalculatorParser