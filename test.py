from antlr4 import *
from SimpleCalculatorLexer import SimpleCalculatorLexer
from SimpleCalculatorParser import SimpleCalculatorParser
from SimpleCalculatorListener import SimpleCalculatorListener
from SimpleCalculatorVisitor import SimpleCalculatorVisitor

def main():
    # # Create an input stream from the input source
    # with open('cef.txt', 'r') as f:
    #     code = f.read()
    code = """
    for a=1:4 do
begin
 if a % 2 == 1 then
 print "a is odd: ", a;
end
    """
    input_stream = InputStream(code)
    # input_stream = InputStream("int fact *= start;")

    # Create a lexer
    f_lexer = SimpleCalculatorLexer(input_stream)

    # Create a token stream from the lexer
    token_stream = CommonTokenStream(f_lexer)

    # Create a parser
    f_parser = SimpleCalculatorParser(token_stream)

    f_context = f_parser.program()

    f_visitor = SimpleCalculatorVisitor()

    d = f_visitor.visit(f_context)


if __name__ == '__main__':
    main()
