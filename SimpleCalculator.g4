grammar SimpleCalculator;

program : statements;

statements : statement
           | statements statement;

statement : ID ASGN expr SEMICOLON #variableDeclaration_Statement
          | BEGIN statements END #beginEnd_Statement
          | IF expr THEN statement (ELSE statement)? #ifElse_Statement
          | WHILE expr DO statement #whileDo_Statement
          | FOR ID ASGN INT COLON INT DO statement #forDo_Statement
          | LOOP ID COLON INT DO statement #loopDo_Statement
          | PRINT (STRING COMMA)? ID SEMICOLON #print_Statement
          ;

expr: assignmentExpression;

assignmentExpression: equalityExpression (ASGN assignmentExpression)*;

equalityExpression: relationalExpression ((EQ | NEQ) relationalExpression)*;

relationalExpression: additiveExpression ((LT | GT | LTE | GTE) additiveExpression)*;

additiveExpression: multiplicativeExpression ((PLUS | MINUS) multiplicativeExpression)*;

multiplicativeExpression: powerExpression ((MULT | DIV | MOD ) powerExpression)*;

powerExpression: unaryExpression ((POW) unaryExpression)* ;

unaryExpression: (PLUS | MINUS | NOT ) unaryExpression | primaryExpression ;

primaryExpression: INT | STRING | ID | LPAREN expr RPAREN;


LPAREN : '(';
RPAREN : ')';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';
MOD: '%';
LT : '<';
GT : '>';
LTE : '<=';
GTE : '>=';
EQ : '==';
NEQ : '!=';
POW : '^';
NOT : '!';
ASGN : '=';

BEGIN : 'begin';
END : 'end';
IF : 'if';
THEN : 'then';
ELSE : 'else';
WHILE : 'while';
DO : 'do';
FOR : 'for';
LOOP : 'loop';
PRINT : 'print';

COMMA : ',';
SEMICOLON : ';';
COLON : ':';

WS : [ \t\r\n]+ -> skip;

ID: [a-zA-Z]+;
INT: [0-9]+;
STRING: '"' ~["\r\n]* '"';
