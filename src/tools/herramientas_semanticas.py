# herramientas_semanticas.py
import sys
import os

# Añadir raíz del proyecto a sys.path para importar paquete 'gen'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
from gen.F1CompilerLexer import F1CompilerLexer
from gen.F1CompilerParser import F1CompilerParser
from gen.F1CompilerListener import F1CompilerListener

class AnalizadorSemantico(F1CompilerListener):
    def __init__(self):
        # La tabla de símbolos guarda el estado y la memoria de cada parámetro
        self.tabla_simbolos = {}
        self.errores = []

    def enterDeclaracion(self, ctx):
        nombre_var = ctx.ID().getText()
        linea = ctx.ID().getSymbol().line

        # REGLA 1: Evitar declarar una variable dos veces
        if nombre_var in self.tabla_simbolos:
            self.errores.append(f"Grid Penalty (Línea {linea}): El parámetro '{nombre_var}' ya estaba registrado.")
        else:
            tipo_var = ctx.tipo().getText()
            self.tabla_simbolos[nombre_var] = {'tipo': tipo_var, 'linea': linea, 'usado': False}

    def enterAsignacion(self, ctx):
        nombre_var = ctx.ID().getText()
        linea = ctx.ID().getSymbol().line

        # REGLA 2: Evitar asignar valores a variables no declaradas
        if nombre_var not in self.tabla_simbolos:
            self.errores.append(f"Black Flag (Línea {linea}): Intento de reasignar '{nombre_var}', pero no existe en telemetría.")
        else:
            self.tabla_simbolos[nombre_var]['usado'] = True

    # Función auxiliar para revisar lectura de variables (ej. al imprimir o hacer matemáticas)
    def verificar_uso_variable(self, ctx):
        nombre_var = ctx.ID().getText()
        linea = ctx.ID().getSymbol().line

        # REGLA 2 (Continuación): Uso en expresiones de variables no declaradas
        if nombre_var not in self.tabla_simbolos:
            self.errores.append(f"Black Flag (Línea {linea}): Se intentó leer '{nombre_var}', pero no está registrado.")
        else:
            self.tabla_simbolos[nombre_var]['usado'] = True

    # Soporte para interceptar las variables dentro de las expresiones
    def enterIdLiteral(self, ctx):
        self.verificar_uso_variable(ctx)

    def enterExpresion(self, ctx):
        if hasattr(ctx, 'ID') and ctx.ID() is not None:
            self.verificar_uso_variable(ctx)

    def exitProgram(self, ctx):
        # REGLA 3: Al terminar la carrera, revisar si sobraron variables sin usar
        for nombre_var, info in self.tabla_simbolos.items():
            if not info['usado']:
                linea = info['linea']
                self.errores.append(f"Warning (Línea {linea}): El parámetro '{nombre_var}' fue declarado pero nunca se utilizó en la estrategia.")


def ejecutar_analisis_semantico(codigo):
    flujo_entrada = InputStream(codigo)
    lexer = F1CompilerLexer(flujo_entrada)
    tokens = CommonTokenStream(lexer)
    parser = F1CompilerParser(tokens)
    arbol = parser.program()

    analizador = AnalizadorSemantico()
    walker = ParseTreeWalker()

    # El walker recorre el AST disparando los eventos "enter" y "exit" de nuestro Listener
    walker.walk(analizador, arbol)

    print("=" * 80)
    print("REPORTE DE DIRECCIÓN DE CARRERA (Análisis Semántico)")
    print("=" * 80)

    if not analizador.errores:
        print("Estrategia legal. No se encontraron infracciones semánticas.")
    else:
        for error in analizador.errores:
            print(error)

    print("\nTabla de Símbolos Final:")
    for var, info in analizador.tabla_simbolos.items():
        print(f"  - {var}: {info}")
    print("=" * 80)

if __name__ == '__main__':
    # Este código está diseñado INTENCIONALMENTE con infracciones para probar las 3 reglas
    codigo_infracciones = """
    green_light
        // Infracción 1: Declaración duplicada
        laps current_lap = 1;
        telemetry current_lap = 2.5;

        // Infracción 2: Uso de variable fantasma (nunca se declaró)
        fuel_load = 105.0;
        engineer_says(unknown_tyre);

        // Infracción 3: Se declara pero nadie la usa
        compound neumatico = "Hard";
        
        telemetry pace = 85.5;
        pace = pace throttle 1.0; // Esta sí es completamente legal
    chequered_flag
    """

    ejecutar_analisis_semantico(codigo_infracciones)