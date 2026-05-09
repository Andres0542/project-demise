grammar Demise;

program
    : statement* EOF
    ;

statement
    : spriteDeclaration //spriteDeclaration
    | mapDeclaration //mapDeclaratuion
    | npcDeclaration //npcDeclaration
    | npcPositioning //npcPositioning
    | musicDeclaration // musicDeclaration
    | weaponDeclaration // weaponDeclaration
    | weaponLogic // weaponLogic
    | filter //filter
    | uiDeclaration //UIDeclaration
    | lightningDeclaration //lightningDeclaration
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

// filter(hotline, ceiling)
filter
    : FILTER LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN
    ;

// npc imp -> 'Imp.jpg'
npcDeclaration
    : NPC IDENTIFIER ARROW STRING_LITERAL
    ;

// music -> 'Numb.mp3'
musicDeclaration
    : MUSIC ARROW STRING_LITERAL
    ;

// map -> [1 0 0 ...] [1 0 ...] ... ;
mapDeclaration
    : MAP ARROW mapRow+ SEMICOLON
    ;

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
    : IDENTIFIER ARROW LPAREN INTEGER COMMA INTEGER RPAREN
    ;

// weapon shotgun -> 'Shotgun.png'
weaponDeclaration
    : WEAPON IDENTIFIER ARROW STRING_LITERAL
    ;

// shotgun -> shotgun
// BFG6000 -> BFG6000
weaponLogic
    : IDENTIFIER ARROW IDENTIFIER
    ;

// Predefined test commands
testCommand
    : FLOORCASTING_TEST
    | RAYCASTING_TEST
    | RAYCASTING_MAZE_TEST
    | REFLEXING_FLOOR
    ;


// ─── Keywords ────────────────────────────────────────────────────────────────

SPRITE              : 'sprite';
SPRITE_TYPE         : 'wall' | 'floor' | 'ceiling' | 'sky';
FILTER              : 'filter';
NPC                 : 'npc';
MUSIC               : 'music';
MAP                 : 'map';
LIGHTNING           : 'lightning';
UI                  : 'UI';
WEAPON              : 'weapon';

FLOORCASTING_TEST   : 'floorcasting_test';
RAYCASTING_TEST     : 'raycasting_test';
RAYCASTING_MAZE_TEST: 'raycasting_maze_test';
REFLEXING_FLOOR     : 'reflexing_floor';


// ─── Delimiters ───────────────────────────────────────────────────────────────

ARROW               : '->';
LPAREN              : '(';
RPAREN              : ')';
LBRACKET            : '[';
RBRACKET            : ']';
COMMA               : ',';
SEMICOLON           : ';';


// ─── Literals ─────────────────────────────────────────────────────────────────

INTEGER
    : [0-9]+
    ;

STRING_LITERAL
    : '\'' (~['\r\n])* '\''
    ;


// ─── Identifier ───────────────────────────────────────────────────────────────
// Must come AFTER all keywords so keywords are matched first

IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;


// ─── Comments & whitespace ────────────────────────────────────────────────────

COMENTARIO
    : '//' ~[\r\n]*
    ;

ESPACIO
    : [\r\n]+
    ;

WS
    : [ \t]+ -> skip
    ;
