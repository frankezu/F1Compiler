grammar F1Compiler;

// =====================================================================
// FASE 2: REGLAS DEL PARSER (Gramática Completa y Coherente)
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

// Se añaden dos estructuras repetitivas distintas: keep_pushing_while (WHILE) y start_new_stint (FOR)
ciclo       : WHILE LPAREN expresion RPAREN LBRACE statement* RBRACE
            | FOR LPAREN asignacion TO expresion RPAREN LBRACE statement* RBRACE ;

tipo        : TYPE_LAPS | TYPE_TELEMETRY | TYPE_DECISION | TYPE_COMPOUND ;

// Regla de expresión ordenada estrictamente por precedencia de operadores para cumplir con la rúbrica
expresion   : LPAREN expresion RPAREN                       # ParentesisExp
            | llamada_funcion                               # FuncionExp
            | NOT expresion                                 # NotExp
            | expresion (MUL | DIV) expresion               # MultiplicativaExp
            | expresion (ADD | SUB) expresion               # AditivaExp
            | expresion (LESS_THAN | GREATER_THAN | EQUALS) expresion # RelacionalExp
            | expresion AND expresion                       # AndExp
            | expresion OR expresion                        # OrExp
            | NUM_INT                                       # IntLiteral
            | NUM_FLOAT                                     # FloatLiteral
            | STRING                                        # StringLiteral
            | ID                                            # IdLiteral
            | TRACK_CLEAR                                   # TrueLiteral
            | RED_FLAG                                      # FalseLiteral
            ;

// Remoción del punto y coma intermedio que causaba error de sintaxis en ANTLR
llamada_funcion : FUNC_WEAR LPAREN expresion RPAREN
                | FUNC_STEER LPAREN expresion RPAREN
                | FUNC_ERS LPAREN expresion COMMA expresion RPAREN
                | FUNC_UNDERCUT LPAREN expresion RPAREN ;

// =====================================================================
// FASE 1: REGLAS DEL LEXER (Tokens Narrativos de F1)
// =====================================================================

// 1. Palabras Clave de Estructura Principal
GREEN_LIGHT    : 'green_light' ;
CHEQUERED_FLAG : 'chequered_flag' ;

// 2. Tipos de Datos (Cumple con >= 3 tipos declarados)
TYPE_LAPS      : 'laps' ;
TYPE_TELEMETRY : 'telemetry' ;
TYPE_DECISION  : 'steward_decision' ;
TYPE_COMPOUND  : 'compound' ;

// 3. Funciones Nativas (Se incluye la 4ta función matemática requerida)
PRINT          : 'engineer_says' ;
FUNC_WEAR      : 'tyre_wear_calc' ;
FUNC_STEER     : 'calc_steering' ;
FUNC_ERS       : 'deploy_ers' ;
FUNC_UNDERCUT  : 'calculate_undercut_delta' ;

// 4. Estructuras de Control (Condicional + 2 repetitivas independientes)
IF             : 'if_pitwall_says' ;
ELSE           : 'otherwise_box' ;
WHILE          : 'keep_pushing_while' ;
FOR            : 'start_new_stint' ;
TO             : 'up_to_lap' ;

// 5. Valores Booleanos
TRACK_CLEAR    : 'track_clear' ; // Actúa como Verdadero (True)
RED_FLAG       : 'red_flag' ;    // Actúa como Falso (False)

// 6. Operadores Lógicos y Relacionales (Se añade OR para soportar evaluaciones complejas)
LESS_THAN      : 'slower_than' ;
GREATER_THAN   : 'faster_than' ;
EQUALS         : 'matched_delta' ;
AND            : 'and_drs_open' ;
OR             : 'or_box_opposite' ;
NOT            : 'telemetry_denies' ;

// 7. Operadores Matemáticos (Los 4 operadores básicos con nombres temáticos)
ADD            : 'throttle' ;         // Suma (+)
SUB            : 'brake' ;            // Resta (-)
MUL            : 'catch_slipstream' ; // Multiplicación (*)
DIV            : 'in_dirty_air' ;     // División (/)

// 8. Símbolos
ASSIGN         : '=' ;
SEMI           : ';' ;
COMMA          : ',' ;
LPAREN         : '(' ;
RPAREN         : ')' ;
LBRACE         : '{' ;
RBRACE         : '}' ;

// 9. Literales e Identificadores
NUM_FLOAT      : [0-9]+ '.' [0-9]+ ;
NUM_INT        : [0-9]+ ;
STRING         : '"' ~["]* '"' ;
ID             : [a-zA-Z_] [a-zA-Z0-9_]* ;

// 10. Espacios y Comentarios (Se ignoran en el análisis)
COMMENT        : '//' ~[\r\n]* -> skip ;
WS             : [ \t\r\n]+ -> skip ;