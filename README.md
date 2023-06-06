# SimpleCalculator

This repository contains a simple calculator implemented using the ANTLR4 parser generator. The calculator is capable of evaluating arithmetic expressions, handling variables, loops, conditional statements, and basic input/output operations.

## Grammar

The calculator's grammar is defined in the file `SimpleCalculator.g4`. It includes the following rules:

- `program`: Represents a program and consists of a sequence of statements.
- `stmt`: Defines different types of statements, such as variable declaration, conditional statements, loops, and print statements.
- `expr`: Represents an arithmetic expression and supports binary operations, such as addition, subtraction, multiplication, division, modulus, and exponentiation.
- `bin`: Represents a binary expression, combining two arithmetic expressions with a binary operator.
- `mathematical`: Represents a mathematical term, which can be a single factor or a combination of factors with addition or subtraction operators.
- `term`: Represents a term in an arithmetic expression, which can be a single factor or a combination of factors with multiplication, division, or modulus operators.
- `factor`: Represents a factor in an arithmetic expression, which can be a final factor (number, variable, or expression in parentheses) or a factor raised to a power.
- `finalfactor`: Represents the final factor in an arithmetic expression, which can be a number, a negative number, a variable, or an expression in parentheses.

## Usage

The main functionality of the calculator is demonstrated in the `main.py` file. It includes sample code snippets that showcase different features of the calculator. You can modify the sample codes or add your own to experiment with the calculator.

To run the calculator, follow these steps:

1. Make sure you have Python installed on your system.
2. Install the required dependencies by running the command: `pip install antlr4-python3-runtime`.
3. Execute the `main.py` script using the command: `python main.py`.
4. The output will display the result of evaluating the sample codes, along with any printed statements.

## Sample Codes

The `main.py` script contains several sample codes that demonstrate the usage of the calculator. Each code snippet is enclosed in triple quotes (`"""`) and assigned to the `sample_codes` list. You can modify the sample codes or add your own to experiment with the calculator.

Here are some of the included sample codes:

1. Arithmetic Operations:
    ```python
    a = 2 + 3 * 4;
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
    print "a is ", a;
    ```
2. Loop with Conditional Statement:
    ```python
    loop a:4 do
    begin
        if a % 2 == 1 then
            print "a is odd: ", a;
        else
            print "a is even: ", a;
    end
    ```
3. For Loop with Conditional Statement:
    ```python
    for a=1:4 do
    begin
        if a % 2 == 1 then
            print "a is odd: ", a;
    end
    ```
4. While Loop with Conditional Statement:
    ```python
    a = 4;
    while a > 0 do
    begin
        if a % 2 == 1 then
            print "a is odd: ", a;
        else
            print "a is even: ", a;
        a = a - 1;
    end
    ```

Feel free to modify the sample codes or write your own code snippets to explore the capabilities of the calculator.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code according to your needs.
