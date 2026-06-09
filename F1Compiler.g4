grammar F1Compiler;

// =====================================================================
// FASE 2: REGLAS DEL PARSER (Esqueleto Básico)
// =====================================================================

program     : GREEN_LIGHT statement* CHEQUERED_FLAG EOF ;

statement   : declaracion
            | asignacion
            | impresion
            | condicional
            | ciclo
            | llamada_funcion SEMI ;

declaracion : tipo ID ASSIGN expresion SEMI ;
asignacion  : ID ASSIGN expresion SEMI ;
impresion   : PRINT LPAREN expresion RPAREN SEMI ;

condicional : IF LPAREN expresion RPAREN LBRACE statement* RBRACE
              (ELSE LBRACE statement* RBRACE)? ;

ciclo       : WHILE LPAREN expresion RPAREN LBRACE statement* RBRACE ;

tipo        : TYPE_LAPS | TYPE_TELEMETRY | TYPE_DECISION | TYPE_COMPOUND ;

expresion   : expresion (ADD | SUB) expresion
            | expresion (LESS_THAN | GREATER_THAN | EQUALS) expresion
            | expresion AND expresion
            | NOT expresion
            | NUM_INT
            | NUM_FLOAT
            | STRING
            | ID
            | TRACK_CLEAR
            | RED_FLAG
            | llamada_funcion ;

llamada_funcion : FUNC_WEAR LPAREN expresion RPAREN
                | FUNC_STEER LPAREN expresion RPAREN
                | FUNC_ERS LPAREN expresion COMMA expresion RPAREN ;

// =====================================================================
// FASE 1: REGLAS DEL LEXER (Tokens)
// =====================================================================

// 1. Palabras Clave de Estructura Principal
GREEN_LIGHT    : 'green_light' ;
CHEQUERED_FLAG : 'chequered_flag' ;

// 2. Tipos de Datos
TYPE_LAPS      : 'laps' ;
TYPE_TELEMETRY : 'telemetry' ;
TYPE_DECISION  : 'steward_decision' ;
TYPE_COMPOUND  : 'compound' ;

// 3. Funciones Nativas
PRINT          : 'engineer_says' ;
FUNC_WEAR      : 'tyre_wear_calc' ;
FUNC_STEER     : 'calc_steering' ;
FUNC_ERS       : 'deploy_ers' ;

// 4. Estructuras de Control
IF             : 'if_pitwall_says' ;
ELSE           : 'otherwise_box' ;
WHILE          : 'keep_pushing_while' ;

// 5. Valores Booleanos
TRACK_CLEAR    : 'track_clear' ; // Actúa como Verdadero
RED_FLAG       : 'red_flag' ;    // Actúa como Falso

// 6. Operadores Lógicos y Relacionales
LESS_THAN      : 'slower_than' ;
GREATER_THAN   : 'faster_than' ;
EQUALS         : 'matched_delta' ;
AND            : 'and_drs_open' ;
NOT            : 'telemetry_denies' ;

// 7. Operadores Matemáticos
ADD            : 'throttle' ;
SUB            : 'brake' ;

// 8. Símbolos
ASSIGN         : '=' ;
SEMI           : ';' ;
COMMA          : ',' ;
LPAREN         : '(' ;
RPAREN         : ')' ;
LBRACE         : '{' ;
RBRACE         : '}' ;

// 9. Literales e Identificadores (Regla de Oro: ¡Siempre al final!)
NUM_FLOAT      : [0-9]+ '.' [0-9]+ ;
NUM_INT        : [0-9]+ ;
STRING         : '"' ~["]* '"' ;
ID             : [a-zA-Z_] [a-zA-Z0-9_]* ;

// 10. Espacios y Comentarios (Se ignoran en el Lexer)
COMMENT        : '//' ~[\r\n]* -> skip ;
WS             : [ \t\r\n]+ -> skip ;