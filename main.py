from antlr4 import *
from SimpleCalculatorLexer import SimpleCalculatorLexer
from SimpleCalculatorParser import SimpleCalculatorParser
from MyCustomVisitor import MyCustomVisitor


def main():
    sample_codes = ["""a = 2 + 3 * 4;
print "a is ", a;
a = 2 - 1 - 1 - 1;
print "a is ", a;
b = 8 / 2 / 2 / 2;
print "b is ", b;
a = 2 ^ 3 ^ 2 ^ b;
print "a is ", a;
c = 2 ^ 1 ^ 2 ^ 3;
print "c is ", c;
d = c ^ 3 * c;
print "d is ", d;
e = 3 ^ (3 / 3);
f = c * c ^ e * e;
print "f is ", f;
a = 2 * 2 ^ (3 * 3);
print "a is ", a;""",
                    """loop a:4 do
                    begin
                     if a % 2 == 1 then
                     print "a is odd: ", a;
                     else
                     print "a is even: ", a;
                    end""", """for a=1:4 do
begin
 if a % 2 == 1 then
 print "a is odd: ", a;
end""",
                    """a = 4;
                    while a > 0 do
                    begin
                     if a % 2 == 1 then
                     print "a is odd: ", a;
                     else
                     print "a is even: ", a;
                     a = a - 1;
                    end"""]
    for i, code in enumerate(sample_codes):
        print(f"""Sample Code Number {i+1}: 
""")
        input_stream = InputStream(code)
        # Create a lexer
        f_lexer = SimpleCalculatorLexer(input_stream)

        # Create a token stream from the lexer
        token_stream = CommonTokenStream(f_lexer)

        # Create a parser
        f_parser = SimpleCalculatorParser(token_stream)

        f_context = f_parser.program()

        f_visitor = MyCustomVisitor()

        f_visitor.visit(f_context)

        print("==========================================")


if __name__ == '__main__':
    main()
