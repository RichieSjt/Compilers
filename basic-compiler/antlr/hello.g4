grammar hello;

program : expression+ ;

expression:
    expression '=' expression #assign 
    | expression '+' expression #add 
    | expression '-' expression #substract 
    | expression '*' expression #multiply 
    | expression '/' expression #divide
    | expression '<' expression #lessthan
    | expression '>' expression #greaterthan
    | Number #number
    | String #string
    | Endline #endline
    ;

statement:
    'var' Var #declare
    | expression '?' statement #if
    | expression '?' statement ':' statement #ifelse
    | 'print(' expression ')' #print
    ;

Number : [0-9]+;
String :  [a-zA-Z0-9]+;
Var :  [a-zA-Z]+;
Endline: [\n];
WS : [\t\r]+ -> skip;