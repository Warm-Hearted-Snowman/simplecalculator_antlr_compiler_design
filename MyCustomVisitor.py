from SimpleCalculatorParser import SimpleCalculatorParser
from SimpleCalculatorVisitor import SimpleCalculatorVisitor


class MyCustomVisitor(SimpleCalculatorVisitor):

    def __init__(self):
        super().__init__()
        self.variables = {}

    def visitProgram(self, ctx: SimpleCalculatorParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitVariableDeclaration_Statement(self, ctx: SimpleCalculatorParser.VariableDeclaration_StatementContext):
        return super().visitVariableDeclaration_Statement(ctx)

    def visitBeginEnd_Statement(self, ctx: SimpleCalculatorParser.BeginEnd_StatementContext):
        return super().visitBeginEnd_Statement(ctx)

    def visitIfElse_Statement(self, ctx: SimpleCalculatorParser.IfElse_StatementContext):
        return super().visitIfElse_Statement(ctx)

    def visitWhileDo_Statement(self, ctx: SimpleCalculatorParser.WhileDo_StatementContext):
        return super().visitWhileDo_Statement(ctx)

    def visitForDo_Statement(self, ctx: SimpleCalculatorParser.ForDo_StatementContext):
        return super().visitForDo_Statement(ctx)

    def visitLoopDo_Statement(self, ctx: SimpleCalculatorParser.LoopDo_StatementContext):
        return super().visitLoopDo_Statement(ctx)

    def visitPrint_Statement(self, ctx: SimpleCalculatorParser.Print_StatementContext):
        return super().visitPrint_Statement(ctx)

    def visitExpr_bin(self, ctx: SimpleCalculatorParser.Expr_binContext):
        return int(self.visit(ctx.bin_()))

    def visitExpr_bool(self, ctx: SimpleCalculatorParser.Expr_boolContext):
        return super().visitExpr_bool(ctx)

    def visitBin_mathematical(self, ctx: SimpleCalculatorParser.Bin_mathematicalContext):
        return int(self.visit(ctx.mathematical()))

    def visitBin_binop(self, ctx: SimpleCalculatorParser.Bin_binopContext):
        return super().visitBin_binop(ctx)

    def visitMathematical_minus(self, ctx: SimpleCalculatorParser.Mathematical_minusContext):
        return int(self.visit(ctx.mathematical()) - self.visit(ctx.term()))

    def visitMathematical_term(self, ctx: SimpleCalculatorParser.Mathematical_termContext):
        return int(self.visit(ctx.term()))

    def visitMathematical_plus(self, ctx: SimpleCalculatorParser.Mathematical_plusContext):
        return int(self.visit(ctx.mathematical()) + self.visit(ctx.term()))

    def visitTerm_factor(self, ctx: SimpleCalculatorParser.Term_factorContext):
        return int(self.visit(ctx.factor()))

    def visitTerm_div(self, ctx: SimpleCalculatorParser.Term_divContext):
        return int(self.visit(ctx.term()) / self.visit(ctx.factor()))

    def visitTerm_mult(self, ctx: SimpleCalculatorParser.Term_multContext):
        return int(self.visit(ctx.term()) * self.visit(ctx.factor()))

    def visitFactor_minus_number(self, ctx: SimpleCalculatorParser.Factor_minus_numberContext):
        return -int(self.visit(ctx.factor()))

    def visitFactor_id(self, ctx: SimpleCalculatorParser.Factor_idContext):
        return self.variables[ctx.ID().getText()]['value']

    def visitFactor_power(self, ctx: SimpleCalculatorParser.Factor_powerContext):
        return int(pow(self.visit(ctx.factor()), ctx.Number().getText()))

    def visitFactor_expr(self, ctx: SimpleCalculatorParser.Factor_exprContext):
        return int(self.visit(ctx.expr()))

    def visitFactor_number(self, ctx: SimpleCalculatorParser.Factor_numberContext):
        return int(ctx.Number().getText())