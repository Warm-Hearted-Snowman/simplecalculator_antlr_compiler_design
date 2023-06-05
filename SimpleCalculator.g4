grammar SimpleCalculator;

program : (stmt)* ;

stmt: ID EQ expr SEMICOLON #variableDeclaration_Statement
    | Begin (stmt)* END #beginEnd_Statement
    | IF expr THEN stmt (ELSE stmt)? #ifElse_Statement
    | WHILE expr DO stmt #whileDo_Statement
    | FOR ID EQ Number COLON Number DO stmt #forDo_Statement
    | LOOP ID COLON Number DO stmt #loopDo_Statement
    | PRINT (SL COMMA)* ID SEMICOLON #print_Statement
    ;


expr: bin #expr_bin
    | expr BOOL bin #expr_bool
    ;


bin: mathematical #bin_mathematical
  | bin BINOP mathematical #bin_binop
  ;

mathematical: term #mathematical_term
  | mathematical PLUS term #mathematical_plus
  | mathematical MINUS term #mathematical_minus
  ;

term: factor #term_factor
  | term MULT factor #term_mult
  | term DIV factor #term_div
  | term MOD factor #term_mod
  ;

factor: finalfactor #factor_finalfactor
      | factor (POWER finalfactor)+ #factor_power
      ;

finalfactor: Number #finalfactor_number
  | MINUS finalfactor #finalfactor_minus_number
  | ID #finalfactor_id
  | OPENP expr CLOSEP #finalfactor_expr
  ;

BOOL : '==' | '!=';
BINOP :  '<' | '>' | '<=' | '>=' ;
OPENP : '(' ;
CLOSEP : ')' ;
PLUS : '+';
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;
POWER : '^' ;
MOD: '%';
Number : [0-9]+ ;
EQ : '=' ;
COLON : ':';
PRINT : 'print';
IF : 'if';
THEN : 'then';
ELSE : 'else';
WHILE : 'while';
DO : 'do';
FOR : 'for';
LOOP : 'loop';
Begin : 'begin';
END : 'end';
COMMA: ',';
SEMICOLON: ';';
ID : [a-zA-Z][a-zA-Z0-9_]* ;
SL : '"' ~["\r\n]* '"';
WS :[ \t\n\r]+ -> skip;
