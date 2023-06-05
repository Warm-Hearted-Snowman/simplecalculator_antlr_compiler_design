from SimpleCalculatorParser import SimpleCalculatorParser
from SimpleCalculatorVisitor import SimpleCalculatorVisitor


class MyCustomVisitor(SimpleCalculatorVisitor):

    def __init__(self):
        super().__init__()
        self.variables = {}
        self.power_queue = []

    def visitProgram(self, ctx: SimpleCalculatorParser.ProgramContext):
        for statement in ctx.stmt():
            self.visit(statement)
        return "Finish"

    def visitVariableDeclaration_Statement(self, ctx: SimpleCalculatorParser.VariableDeclaration_StatementContext):
        self.variables[ctx.ID().getText()] = {"value": self.visit(ctx.expr())}
        return self.variables[ctx.ID().getText()]

    def visitBeginEnd_Statement(self, ctx: SimpleCalculatorParser.BeginEnd_StatementContext):
        for statement in ctx.stmt():
            self.visit(statement)
        return "Begin-End Finish"

    def visitIfElse_Statement(self, ctx: SimpleCalculatorParser.IfElse_StatementContext):
        flag = True
        if self.visit(ctx.expr()):
            self.visit(ctx.stmt(0))
            flag = False
        if flag and (ctx.ELSE() is not None):
            self.visit(ctx.stmt(1))

    def visitWhileDo_Statement(self, ctx: SimpleCalculatorParser.WhileDo_StatementContext):
        while self.visit(ctx.expr()):
            self.visit(ctx.stmt())
        return "While-Do Finish"

    def visitForDo_Statement(self, ctx: SimpleCalculatorParser.ForDo_StatementContext):
        self.variables[ctx.ID().getText()] = {"value": ctx.Number(0).getText()}
        for i in range(int(self.variables[ctx.ID().getText()]['value']), int(ctx.Number(1).getText())):
            self.variables[ctx.ID().getText()]['value'] = i
            self.visit(ctx.stmt())
        return "For Finish"

    def visitLoopDo_Statement(self, ctx: SimpleCalculatorParser.LoopDo_StatementContext):
        self.variables[ctx.ID().getText()] = {"value": ctx.Number().getText()}
        for i in range(1, int(self.variables[ctx.ID().getText()]['value']) + 1):
            self.variables[ctx.ID().getText()]['value'] = i
            self.visit(ctx.stmt())
        return "Loop Finish"

    def visitPrint_Statement(self, ctx: SimpleCalculatorParser.Print_StatementContext):
        for string in ctx.SL():
            print(str(string).strip('"'), end='')
        print(self.variables[ctx.ID().getText()]['value'])

    def visitExpr_bin(self, ctx: SimpleCalculatorParser.Expr_binContext):
        return int(self.visit(ctx.bin_()))

    def visitExpr_bool(self, ctx: SimpleCalculatorParser.Expr_boolContext):
        if str(ctx.BOOL()) == "==":
            return self.visit(ctx.expr()) == self.visit(ctx.bin_())
        if str(ctx.BOOL()) == "!=":
            return self.visit(ctx.expr()) != self.visit(ctx.bin())

    def visitBin_mathematical(self, ctx: SimpleCalculatorParser.Bin_mathematicalContext):
        return int(self.visit(ctx.mathematical()))

    def visitBin_binop(self, ctx: SimpleCalculatorParser.Bin_binopContext):
        if str(ctx.BINOP()) == "<":
            return self.visit(ctx.bin_()) < self.visit(ctx.mathematical())
        if str(ctx.BINOP()) == "<=":
            return self.visit(ctx.bin_()) <= self.visit(ctx.mathematical())
        if str(ctx.BINOP()) == ">":
            return self.visit(ctx.bin_()) > self.visit(ctx.mathematical())
        if str(ctx.BINOP()) == ">=":
            return self.visit(ctx.bin_()) >= self.visit(ctx.mathematical())

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

    def visitTerm_mod(self, ctx: SimpleCalculatorParser.Term_modContext):
        return int(self.visit(ctx.term()) % self.visit(ctx.factor()))

    def visitFactor_power(self, ctx: SimpleCalculatorParser.Factor_powerContext):
        length = len(ctx.finalfactor())
        if length > 1:
            result = pow(self.visit(ctx.finalfactor().pop(-2)), self.visit(ctx.finalfactor().pop(-1)))
            length -= 2
            while length > 0:
                result = pow(self.visit(ctx.finalfactor().pop(length-1)), result)
                length -= 1
            return int(pow(self.visit(ctx.factor()), result))
        else:
            return int(pow(self.visit(ctx.factor()), self.visit(ctx.finalfactor(0))))

    def visitFactor_finalfactor(self, ctx: SimpleCalculatorParser.Factor_finalfactorContext):
        return int(self.visit(ctx.finalfactor()))

    def visitFinalfactor_number(self, ctx: SimpleCalculatorParser.Finalfactor_numberContext):
        return int(ctx.Number().getText())

    def visitFinalfactor_minus_number(self, ctx: SimpleCalculatorParser.Finalfactor_minus_numberContext):
        return -int(self.visit(ctx.finalfactor()))

    def visitFinalfactor_id(self, ctx: SimpleCalculatorParser.Finalfactor_idContext):
        return int(self.variables[ctx.ID().getText()]['value'])

    def visitFinalfactor_expr(self, ctx: SimpleCalculatorParser.Finalfactor_exprContext):
        return int(self.visit(ctx.expr()))
