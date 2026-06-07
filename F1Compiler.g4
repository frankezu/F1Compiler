// El nombre de la gramática DEBE coincidir exactamente con el nombre del archivo.
// Esto determina cómo ANTLR nombrará las clases generadas:
// F1CompilerLexer.py, F1CompilerParser.py, etc.
grammar F1Compiler;

// ═══════════════════════════════════════════════════════════════════════════
// REGLAS DEL PARSER
// ═══════════════════════════════════════════════════════════════════════════
// Las reglas del parser definen la ESTRUCTURA del lenguaje.
// Se escriben en minúsculas.
// Describen cómo se combinan los tokens para formar construcciones válidas.
// El símbolo '*' significa "cero o más veces".
// El símbolo '?' significa "cero o una vez" (opcional).
// El símbolo '|' significa "o" (alternativa).
// ═══════════════════════════════════════════════════════════════════════════

// Regla raíz: todo programa comienza con INICIO, tiene cero o más sentencias,
// y termina con FIN seguido de EOF (End Of File, marca el final del texto).
program
    : INICIO sentencia* FIN EOF
    ;

// Una sentencia es cualquier instrucción válida del lenguaje.
// Agrega aquí nuevas opciones a medida que amplíes la gramática.
sentencia
    : declaracion
    | asignacion
    | si_stmt
    | mientras_stmt
    | para_stmt
    | print_stmt
    | llamada_funcion_stmt ';'
    ;

// ── Declaración de variables ───────────────────────────────────────────────
// Define una variable con su tipo y un valor inicial opcional.
// El '?' hace que '=' expresion sea opcional (puede declararse sin valor inicial).
// Ejemplos: "entero x = 5;"  o  "flotante temperatura;"
declaracion
    : tipo ID ('=' expresion)? ';'
    ;

// Los tipos de datos disponibles en el lenguaje.
// Debes tener al menos 3. Estos son 4 de ejemplo.
tipo
    : ENTERO //ENTERO
    | FLOTANTE //FLOTANTE
    | BOOLEANO //BOOLEANO
    | CADENA //CADENA
    ;

// ── Asignación ────────────────────────────────────────────────────────────
// Modifica el valor de una variable ya declarada.
// Ejemplo: "x = x + 1;"
asignacion
    : ID '=' expresion ';'
    ;

// ── Estructura condicional ────────────────────────────────────────────────
// Equivalente al if/else clásico.
// El bloque 'sino' es completamente opcional (de ahí el '?').
si_stmt
    : SI '(' condicion ')' '{' sentencia* '}'
      (SINO '{' sentencia* '}')?
    ;

// ── Ciclo mientras (while) ────────────────────────────────────────────────
// Se repite mientras la condición sea verdadera.
// Ejemplo: "mientras (x < 10) { x = x + 1; }"
mientras_stmt
    : MIENTRAS '(' condicion ')' '{' sentencia* '}'
    ;

// ── Ciclo para (for) ──────────────────────────────────────────────────────
// Ciclo con contador. Tiene tres partes:
//   1. Inicialización (declaracion): crea e inicializa el contador
//   2. Condición (condicion ';'): se evalúa antes de cada iteración
//   3. Actualización (asignacion_simple): se ejecuta al final de cada iteración
// Ejemplo: "para (entero i = 0; i < 10; i = i + 1) { imprimir(i); }"
para_stmt
    : PARA '(' declaracion condicion ';' asignacion_simple ')' '{' sentencia* '}'
    ;

// Asignación sin punto y coma: se usa en la cabecera del 'para'
// donde el ';' ya está incluido explícitamente en para_stmt.
asignacion_simple
    : ID '=' expresion
    ;

// ── Impresión ─────────────────────────────────────────────────────────────
// Muestra un valor en la consola. Acepta expresiones (variables, cálculos)
// o una cadena de texto literal directamente.
print_stmt
    : IMPRIMIR '(' (expresion | CADENA_LITERAL) ')' ';'
    ;

// ── Llamada a funciones matemáticas como sentencia ───────────────────────
// Permite llamar a una función matemática como instrucción propia (no solo
// dentro de una expresión). El resultado se descarta en este caso.
llamada_funcion_stmt
    : llamada_funcion
    ;

// Las funciones matemáticas pueden aparecer dentro de expresiones
// (por ejemplo: "entero r = raiz(25);") o como sentencias solas.
// Agrega aquí las 4 funciones matemáticas que requiere el proyecto.
llamada_funcion
    : RAIZ     '(' expresion ')'
    | COSENO   '(' expresion ')'
    | SENO     '(' expresion ')'
    | POTENCIA '(' expresion ',' expresion ')'
    ;

// ── Condiciones ───────────────────────────────────────────────────────────
// Una condición puede ser:
//   - Una comparación simple entre dos expresiones
//   - Una combinación de condiciones con operadores lógicos Y / O
//   - La negación de una condición con NO
condicion
    : expresion op_comparacion expresion
    | condicion Y condicion
    | condicion O condicion
    | NO condicion
    ;

// ── Expresiones ───────────────────────────────────────────────────────────
// Las expresiones representan valores que se pueden calcular.
// ANTLR resuelve la ambigüedad de precedencia según el orden de las alternativas:
// las que aparecen primero tienen MENOR precedencia.
// En esta gramática: suma/resta < multiplicación/división < demás.
//
// Nota: ANTLR 4 maneja la recursión a izquierda ('expresion OP expresion')
// automáticamente, sin necesidad de transformar la gramática a mano.
expresion
    : expresion SUMA expresion          // Suma
    | expresion RESTA expresion          // Resta
    | expresion MULT expresion          // Multiplicación
    | expresion DIV expresion          // División
    | llamada_funcion                  // Resultado de una función matemática
    | '(' expresion ')'               // Agrupación con paréntesis
    | NUMERO_ENTERO                    // Literal entero: 42
    | NUMERO_FLOTANTE                  // Literal flotante: 3.14
    | VERDADERO                        // Literal booleano verdadero
    | FALSO                            // Literal booleano falso
    | ID                               // Variable (referenciada por su nombre)
    ;

// ── Operadores de comparación ─────────────────────────────────────────────
// Utilizamos los definidos en el Lexer
op_comparacion
    : IGUAL
    | DISTINTO
    | MENOR_QUE
    | MAYOR_QUE
    | MENOR_IGUAL
    | MAYOR_IGUAL
    ;


// ═══════════════════════════════════════════════════════════════════════════
// REGLAS DEL LEXER (TOKENS)
// ═══════════════════════════════════════════════════════════════════════════
// Las reglas del Lexer definen los TOKENS: las unidades mínimas del lenguaje.
// Se escriben en MAYÚSCULAS.
//
// ORDEN CRÍTICO:
//   1. Palabras clave LARGAS antes que las CORTAS
//      (ej: 'inicio_loop' debe ir antes que 'inicio')
//   2. Todas las palabras clave ANTES que ID
//      (el comodín ID siempre va al final)
//   3. NUMERO_FLOTANTE antes que NUMERO_ENTERO
//      (para que "3.14" sea flotante, no entero + punto + entero)
// ═══════════════════════════════════════════════════════════════════════════

// ── Delimitadores del programa ────────────────────────────────────────────
// Estas palabras marcan el inicio y fin de cualquier programa.
// Son las primeras que el Lexer debe reconocer.
// PERSONALIZA ESTAS: son la "firma" de tu lenguaje.
// Ejemplos: 'start engine' / 'shutdown', 'erase una vez' / 'fin del cuento'
INICIO  : 'green_light' ;
FIN     : 'chequered_flag' ;

// ── Tipos de datos ────────────────────────────────────────────────────────
// Palabras clave que indican el tipo de una variable al declararla.
// PERSONALIZA ESTAS según la temática de tu lenguaje.
ENTERO   : 'gethe amount of lap is' ;
FLOTANTE : 'sensor telemetry reports' ;
BOOLEANO : 'race control confirms' ;
CADENA   : 'the selected compound is' ;

// ── Estructuras de control ────────────────────────────────────────────────
SI      : 'if the pit wall says' ;
SINO    : 'otherwise we box and' ;
MIENTRAS: 'keep pushing while' ;
PARA    : 'start stint from' ;

// ── Operadores lógicos ────────────────────────────────────────────────────
// Deben aparecer ANTES que ID para tener prioridad como palabras clave.
Y   : 'and drs is open' ;      // Equivalente a AND lógico
O   : 'or team orders dictate' ;      // Equivalente a OR lógico
NO  : 'the telemetry denies that' ;     // Equivalente a NOT lógico

// ── Valores booleanos literales ───────────────────────────────────────────
VERDADERO : 'track is clear' ;
FALSO     : 'danger on track (RED FLAG)' ; // RED_FLAG COMO TOKEN

// ── Funciones matemáticas y de salida ────────────────────────────────────
// El proyecto requiere al menos 4 funciones matemáticas + la función de impresión.
IMPRIMIR : 'engineer says on radio' ;
RAIZ     : 'calculate the square root of' ;        // Raíz cuadrada
COSENO   : 'coseno' ;      // Coseno (puede recibir grados o radianes, tú decides)
SENO     : 'seno' ;        // Seno
POTENCIA : 'potencia' ;    // Potencia: potencia(base, exponente)

// ── Operadores Matemáticos (NUEVOS) ───────────────────────────────────────
SUMA  : 'throttle' ;
RESTA : 'brake' ;
MULT  : 'slipstream' ;
DIV   : 'degrade' ;

// ── Operadores de Comparación (NUEVOS) ────────────────────────────────────
MAYOR_QUE    : 'faster_than' ;
MENOR_QUE    : 'slower_than' ;
IGUAL        : 'matched_delta' ;
DISTINTO     : 'diff_strategy' ;
MAYOR_IGUAL  : 'faster_or_matched' ;
MENOR_IGUAL  : 'slower_or_matched' ;


// ── Tokens de datos ───────────────────────────────────────────────────────
// Reconocen valores concretos escritos en el código fuente.

// FLOTANTE va AN