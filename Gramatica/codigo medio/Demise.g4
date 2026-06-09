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
    | uiDeclaration 
    | COMENTARIO
    | ESPACIO
    ;

// sprite wall -> 'wall.jpg'
// sprite floor -> 'floor.jpg'
// sprite sky -> 'sky.jpg'

// Cambiarlo a sprite wall 1 -> 'wall.jpg'
// sprite floor 1 -> 'wall.jpg'
// sprite ceiling 1 -> 'ceiling.jpg'
// sprite sky -> 'sky.jpg'
spriteDeclaration
    : SPRITE SPRITE_TYPE ARROW STRING_LITERAL
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
// cambiarlo por weapong shotgun -> 'Shotgun.png' , shotgun;
// shotgun -> 'BFG6000.png' , BFG6000;
weaponDeclaration
    : WEAPON ID ARROW STRING_LITERAL
    ;

// shotgun -> shotgun
// BFG6000 -> BFG6000
//weaponLogic
    //: ID ARROW WEAPON_LOGIC
    //;


// ================ LEXER ==========================

SPRITE              : 'sprite';
SPRITE_TYPE         : 'wall' | 'floor' | 'sky';
NPC                 : 'npc';
MUSIC               : 'music';
MAP                 : 'map';
UI                  : 'UI';
WEAPON              : 'weapon';
WEAPON_LOGIC        : 'chainsawL' | 'fistL' | 'pistolL' | 'shotgunL' | 'chaingunL' | 'rocket_launcherL' | 'energy_rifleL' |'BFG6000L' ;


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
