grammar Demise;

program
    : statement* EOF
    ;

statement
    : spriteDeclaration    // Prioridad 1
    | filterDeclaration    // Prioridad 2
    | testCommand         // Prioridad 3
    | comment
    | NEWLINE
    ;

spriteDeclaration
    : SPRITE SPRITE_TYPE ARROW STRING_LITERAL
    ;

filterDeclaration
    : FILTER LPAREN filterName COMMA target RPAREN
    ;

filterName
    : IDENTIFIER
    ;

target
    : IDENTIFIER
    ;

testCommand
    : FLOORCASTING_TEST
    | RAYCASTING_TEST
    | RAYCASTING_MAZE_TEST
    | REFLEXING_FLOOR
    ;

comment
    : COMMENT
    ;



// Keywords
SPRITE_TYPE         : 'floor'| 'ceiling'|'wall';
SPRITE              : 'sprite';
FILTER              : 'filter';
FLOORCASTING_TEST   : 'floorcasting_test';
RAYCASTING_TEST     : 'raycasting_test';
RAYCASTING_MAZE_TEST: 'raycasting_maze_test';
REFLEXING_FLOOR     : 'reflexing_floor';

// Delimitadores
ARROW               : '->';
LPAREN              : '(';
RPAREN              : ')';
COMMA               : ',';

// Identificadores
IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

STRING_LITERAL
    : '\'' (~['\r\n])* '\''
    ;

// Comentarios
COMMENT
    : '//' ~[\r\n]*
    ;

// Espacios en blanco
NEWLINE
    : [\r\n]+
    ;

WS
    : [ \t]+ -> skip
    ;
