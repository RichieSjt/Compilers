grammar hello;

program : expr+statement* ;

expr:
    expr '+' expr #add 
    | expr '-' expr #substract 
    | expr '*' expr #multiply 
    | expr '/' expr #divide
    | expr '<' expr #lessthan
    | expr '>' expr #greaterthan
    | Number #number
    | String #string
    ;

statement:
    'int' Variable #declare
    | Variable '=' Number #assign
    | 'if(' expr ')' (expr | statement) #if
    | 'if(' expr ')' (expr | statement) 'else' (expr | statement) #ifelse
    | 'print(' expr ')' #print
    ;

Number : [0-9]+;
String :  [a-zA-Z0-9]+;
Variable :  [a-zA-Z]+;
WS : [ \t\r\n]+ -> skip;