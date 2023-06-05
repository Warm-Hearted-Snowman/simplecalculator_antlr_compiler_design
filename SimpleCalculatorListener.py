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


    # Enter a parse tree produced by SimpleCalculatorParser#variableDeclaration_Statement.
    def enterVariableDeclaration_Statement(self, ctx:SimpleCalculatorParser.VariableDeclaration_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#variableDeclaration_Statement.
    def exitVariableDeclaration_Statement(self, ctx:SimpleCalculatorParser.VariableDeclaration_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#beginEnd_Statement.
    def enterBeginEnd_Statement(self, ctx:SimpleCalculatorParser.BeginEnd_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#beginEnd_Statement.
    def exitBeginEnd_Statement(self, ctx:SimpleCalculatorParser.BeginEnd_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#ifElse_Statement.
    def enterIfElse_Statement(self, ctx:SimpleCalculatorParser.IfElse_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#ifElse_Statement.
    def exitIfElse_Statement(self, ctx:SimpleCalculatorParser.IfElse_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#whileDo_Statement.
    def enterWhileDo_Statement(self, ctx:SimpleCalculatorParser.WhileDo_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#whileDo_Statement.
    def exitWhileDo_Statement(self, ctx:SimpleCalculatorParser.WhileDo_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#forDo_Statement.
    def enterForDo_Statement(self, ctx:SimpleCalculatorParser.ForDo_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#forDo_Statement.
    def exitForDo_Statement(self, ctx:SimpleCalculatorParser.ForDo_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#loopDo_Statement.
    def enterLoopDo_Statement(self, ctx:SimpleCalculatorParser.LoopDo_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#loopDo_Statement.
    def exitLoopDo_Statement(self, ctx:SimpleCalculatorParser.LoopDo_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#print_Statement.
    def enterPrint_Statement(self, ctx:SimpleCalculatorParser.Print_StatementContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#print_Statement.
    def exitPrint_Statement(self, ctx:SimpleCalculatorParser.Print_StatementContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#expr_bin.
    def enterExpr_bin(self, ctx:SimpleCalculatorParser.Expr_binContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#expr_bin.
    def exitExpr_bin(self, ctx:SimpleCalculatorParser.Expr_binContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#expr_bool.
    def enterExpr_bool(self, ctx:SimpleCalculatorParser.Expr_boolContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#expr_bool.
    def exitExpr_bool(self, ctx:SimpleCalculatorParser.Expr_boolContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#bin_mathematical.
    def enterBin_mathematical(self, ctx:SimpleCalculatorParser.Bin_mathematicalContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#bin_mathematical.
    def exitBin_mathematical(self, ctx:SimpleCalculatorParser.Bin_mathematicalContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#bin_binop.
    def enterBin_binop(self, ctx:SimpleCalculatorParser.Bin_binopContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#bin_binop.
    def exitBin_binop(self, ctx:SimpleCalculatorParser.Bin_binopContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#mathematical_minus.
    def enterMathematical_minus(self, ctx:SimpleCalculatorParser.Mathematical_minusContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#mathematical_minus.
    def exitMathematical_minus(self, ctx:SimpleCalculatorParser.Mathematical_minusContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#mathematical_term.
    def enterMathematical_term(self, ctx:SimpleCalculatorParser.Mathematical_termContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#mathematical_term.
    def exitMathematical_term(self, ctx:SimpleCalculatorParser.Mathematical_termContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#mathematical_plus.
    def enterMathematical_plus(self, ctx:SimpleCalculatorParser.Mathematical_plusContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#mathematical_plus.
    def exitMathematical_plus(self, ctx:SimpleCalculatorParser.Mathematical_plusContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#term_factor.
    def enterTerm_factor(self, ctx:SimpleCalculatorParser.Term_factorContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#term_factor.
    def exitTerm_factor(self, ctx:SimpleCalculatorParser.Term_factorContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#term_div.
    def enterTerm_div(self, ctx:SimpleCalculatorParser.Term_divContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#term_div.
    def exitTerm_div(self, ctx:SimpleCalculatorParser.Term_divContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#term_mod.
    def enterTerm_mod(self, ctx:SimpleCalculatorParser.Term_modContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#term_mod.
    def exitTerm_mod(self, ctx:SimpleCalculatorParser.Term_modContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#term_mult.
    def enterTerm_mult(self, ctx:SimpleCalculatorParser.Term_multContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#term_mult.
    def exitTerm_mult(self, ctx:SimpleCalculatorParser.Term_multContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#factor_power.
    def enterFactor_power(self, ctx:SimpleCalculatorParser.Factor_powerContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#factor_power.
    def exitFactor_power(self, ctx:SimpleCalculatorParser.Factor_powerContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#factor_finalfactor.
    def enterFactor_finalfactor(self, ctx:SimpleCalculatorParser.Factor_finalfactorContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#factor_finalfactor.
    def exitFactor_finalfactor(self, ctx:SimpleCalculatorParser.Factor_finalfactorContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#finalfactor_number.
    def enterFinalfactor_number(self, ctx:SimpleCalculatorParser.Finalfactor_numberContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#finalfactor_number.
    def exitFinalfactor_number(self, ctx:SimpleCalculatorParser.Finalfactor_numberContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#finalfactor_minus_number.
    def enterFinalfactor_minus_number(self, ctx:SimpleCalculatorParser.Finalfactor_minus_numberContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#finalfactor_minus_number.
    def exitFinalfactor_minus_number(self, ctx:SimpleCalculatorParser.Finalfactor_minus_numberContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#finalfactor_id.
    def enterFinalfactor_id(self, ctx:SimpleCalculatorParser.Finalfactor_idContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#finalfactor_id.
    def exitFinalfactor_id(self, ctx:SimpleCalculatorParser.Finalfactor_idContext):
        pass


    # Enter a parse tree produced by SimpleCalculatorParser#finalfactor_expr.
    def enterFinalfactor_expr(self, ctx:SimpleCalculatorParser.Finalfactor_exprContext):
        pass

    # Exit a parse tree produced by SimpleCalculatorParser#finalfactor_expr.
    def exitFinalfactor_expr(self, ctx:SimpleCalculatorParser.Finalfactor_exprContext):
        pass



del SimpleCalculatorParser