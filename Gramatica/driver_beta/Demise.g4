grammar Demise;

program
    : statement* EOF
    ;

statement
    : spriteDeclaration 
    | mapDeclaration 
    | npcDeclaration
    | npcPositioning 
    | musicDeclaration
    | weaponDeclaration 
    | weaponLogic 
    | filter 
    | uiDeclaration 
    | lightningDeclaration 
    | testCommand
    | COMENTARIO
    | ESPACIO
    ;

// sprite wall -> 'wall.jpg'
// sprite floor -> 'floor.jpg'
// sprite sky -> 'sky.jpg'
spriteDeclaration
    : SPRITE SPRITE_TYPE ARROW STRING_LITERAL
    ;

// filter(hotline, sky)
filter
    : FILTER LPAREN FILTER_TYPE COMMA SPRITE_TYPE RPAREN
    ;

// npc imp -> 'Imp.jpg'
npcDeclaration
    : NPC ID ARROW STRING_LITERAL
    ;

// music -> 'Numb.mp3'
musicDeclaration
    : MUSIC ARROW STRING_LITERAL
    ;

// map -> [1 0 0 ...] [1 0 ...] ... ;
mapDeclaration
    : MAP ARROW mapRow+ SEMICOLON
    ;  
// 
mapRow
    : LBRACKET INTEGER+ RBRACKET
    ;

// lightning -> 50
lightningDeclaration
    : LIGHTNING ARROW INTEGER
    ;

// UI -> 'DoomUI.png'
uiDeclaration
    : UI ARROW STRING_LITERAL
    ;

// imp -> (3,3)
// Cacodemon -> (2,2)
npcPositioning
    : ID ARROW LPAREN INTEGER COMMA INTEGER RPAREN
    ;

// weapon shotgun -> 'Shotgun.png'
weaponDeclaration
    : WEAPON ID ARROW STRING_LITERAL
    ;

// shotgun -> shotgun
// BFG6000 -> BFG6000
weaponLogic
    : ID ARROW WEAPON_LOGIC
    ;

// Predefined test commands
testCommand
    : FLOORCASTING_TEST
    | RAYCASTING_TEST
    | RAYCASTING_MAZE_TEST
    ;


// ================ LEXER ==========================

SPRITE              : 'sprite';
SPRITE_TYPE         : 'wall' | 'floor' | 'sky';
FILTER              : 'filter';
FILTER_TYPE         : 'hotline' | 'green_goo' | 'blue_label';
NPC                 : 'npc';
MUSIC               : 'music';
MAP                 : 'map';
LIGHTNING           : 'lightning';
UI                  : 'UI';
WEAPON              : 'weapon';
WEAPON_LOGIC        : 'chainsawL' | 'fistL' | 'pistolL' | 'shotgunL' | 'chaingunL' | 'rocket_launcherL' | 'energy_rifleL' |'BFG6000L' ;
FLOORCASTING_TEST   : 'floorcasting_test';
RAYCASTING_TEST     : 'raycasting_test';
RAYCASTING_MAZE_TEST: 'raycasting_maze_test';


// DELIMITADORES

ARROW               : '->';
LPAREN              : '(';
RPAREN              : ')';
LBRACKET            : '[';
RBRACKET            : ']';
COMMA               : ',';
SEMICOLON           : ';';

INTEGER
    : [0-9]+
    ;

STRING_LITERAL
    : '\'' (~['\r\n])* '\''
    ;


ID
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;


COMENTARIO
    : '//' ~[\r\n]*
    ;
ESPACIO 
    : [\r\n]+ -> skip 
    ;
WS
    : [ \t]+ -> skip
    ;
