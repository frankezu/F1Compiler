# generador_codigo.py
import sys
import os
import math

# Asegurar que la raíz del proyecto esté en sys.path para poder importar el paquete 'gen'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

from antlr4 import InputStream, CommonTokenStream
from gen.F1CompilerLexer import F1CompilerLexer
from gen.F1CompilerParser import F1CompilerParser
from gen.F1CompilerVisitor import F1CompilerVisitor

class GeneradorCodigo(F1CompilerVisitor):
    def __init__(self):
        self.nivel_indent = 0
        self.codigo_generado = []

    def indentar(self):
        return "    " * self.nivel_indent

    def visitProgram(self, ctx):
        # Cabecera oficial del código transpilado
        self.codigo_generado.append("# ==========================================")
        self.codigo_generado.append("# CÓDIGO GENERADO AUTOMÁTICAMENTE (F1Compiler)")
        self.codigo_generado.append("# ==========================================")
        self.codigo_generado.append("import math")
        self.codigo_generado.append("")
        self.codigo_generado.append("# --- Funciones Nativas de Telemetría ---")
        self.codigo_generado.append("def tyre_wear_calc(x): return math.sqrt(x)")
        self.codigo_generado.append("def calc_steering(x): return math.cos(math.radians(x))")
        self.codigo_generado.append("def deploy_ers(x, y): return math.pow(x, y)")
        self.codigo_generado.append("def calculate_undercut_delta(x): return math.log(x)")
        self.codigo_generado.append("")
        self.codigo_generado.append("# --- Estrategia Principal ---")

        # Procesar todas las instrucciones
        for stmt in ctx.statement():
            linea = self.visitStatement(stmt)
            if linea:
                self.codigo_generado.append(linea)

        return "\n".join(self.codigo_generado)

    def visitStatement(self, ctx):
        if ctx.declaracion(): return self.visit(ctx.declaracion())
        elif ctx.asignacion(): return self.visit(ctx.asignacion())
        elif ctx.impresion(): return self.visit(ctx.impresion())
        elif ctx.condicional(): return self.visit(ctx.condicional())
        elif ctx.ciclo(): return self.visit(ctx.ciclo())
        elif ctx.llamada_funcion():
            return f"{self.indentar()}{self.visit(ctx.llamada_funcion())}"

    def visitDeclaracion(self, ctx):
        var_name = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        return f"{self.indentar()}{var_name} = {valor}"

    def visitAsignacion(self, ctx):
        var_name = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        return f"{self.indentar()}{var_name} = {valor}"

    def visitImpresion(self, ctx):
        valor = self.visit(ctx.expresion())
        return f"{self.indentar()}print({valor})"

    def visitCondicional(self, ctx):
        condicion = self.visit(ctx.expresion())
        resultado = f"{self.indentar()}if {condicion}:\n"
        self.nivel_indent += 1

        # Manejo dinámico de bloques IF / ELSE
        in_else = False
        for i in range(ctx.getChildCount()):
            hijo = ctx.getChild(i)
            if hijo.getText() == 'otherwise_box':
                in_else = True
                self.nivel_indent -= 1
                resultado += f"{self.indentar()}else:\n"
                self.nivel_indent += 1
            elif type(hijo).__name__ == "StatementContext":
                resultado += self.visitStatement(hijo) + "\n"

        self.nivel_indent -= 1
        return resultado.rstrip()

    def visitCiclo(self, ctx):
        if ctx.WHILE():
            # Quitamos el (0) porque solo hay 1 expresión en la regla WHILE
            condicion = self.visit(ctx.expresion())
            resultado = f"{self.indentar()}while {condicion}:\n"
            self.nivel_indent += 1
            for stmt in ctx.statement():
                resultado += self.visitStatement(stmt) + "\n"
            self.nivel_indent -= 1
            return resultado.rstrip()

        elif ctx.FOR():
            var_name = ctx.asignacion().ID().getText()
            inicio = self.visit(ctx.asignacion().expresion())
            # Quitamos el (0) porque solo hay 1 expresión límite en la regla FOR
            limite = self.visit(ctx.expresion())

            resultado = f"{self.indentar()}for {var_name} in range(int({inicio}), int({limite}) + 1):\n"
            self.nivel_indent += 1
            for stmt in ctx.statement():
                resultado += self.visitStatement(stmt) + "\n"
            self.nivel_indent -= 1
            return resultado.rstrip()

    # --- Traducción de Expresiones y Operadores ---
    def visitParentesisExp(self, ctx): return f"({self.visit(ctx.expresion())})"
    def visitNotExp(self, ctx): return f"not {self.visit(ctx.expresion())}"
    def visitAndExp(self, ctx): return f"{self.visit(ctx.expresion(0))} and {self.visit(ctx.expresion(1))}"
    def visitOrExp(self, ctx): return f"{self.visit(ctx.expresion(0))} or {self.visit(ctx.expresion(1))}"

    def visitMultiplicativaExp(self, ctx):
        op = "*" if ctx.MUL() else "/"
        return f"{self.visit(ctx.expresion(0))} {op} {self.visit(ctx.expresion(1))}"

    def visitAditivaExp(self, ctx):
        op = "+" if ctx.ADD() else "-"
        return f"{self.visit(ctx.expresion(0))} {op} {self.visit(ctx.expresion(1))}"

    def visitRelacionalExp(self, ctx):
        if ctx.LESS_THAN(): op = "<"
        elif ctx.GREATER_THAN(): op = ">"
        else: op = "=="
        return f"{self.visit(ctx.expresion(0))} {op} {self.visit(ctx.expresion(1))}"

    # --- Traducción de Literales y Constantes Lógicas ---
    def visitIntLiteral(self, ctx): return ctx.getText()
    def visitFloatLiteral(self, ctx): return ctx.getText()
    def visitStringLiteral(self, ctx): return ctx.getText()
    def visitIdLiteral(self, ctx): return ctx.getText()
    def visitTrueLiteral(self, ctx): return "True"
    def visitFalseLiteral(self, ctx): return "False"

    def visitFuncionExp(self, ctx): return self.visit(ctx.llamada_funcion())

    def visitLlamada_funcion(self, ctx):
        if ctx.FUNC_WEAR(): return f"tyre_wear_calc({self.visit(ctx.expresion(0))})"
        elif ctx.FUNC_STEER(): return f"calc_steering({self.visit(ctx.expresion(0))})"
        elif ctx.FUNC_ERS(): return f"deploy_ers({self.visit(ctx.expresion(0))}, {self.visit(ctx.expresion(1))})"
        elif ctx.FUNC_UNDERCUT(): return f"calculate_undercut_delta({self.visit(ctx.expresion(0))})"

def compilar_y_ejecutar(codigo_fuente):
    flujo_entrada = InputStream(codigo_fuente)
    lexer = F1CompilerLexer(flujo_entrada)
    tokens = CommonTokenStream(lexer)
    parser = F1CompilerParser(tokens)
    arbol = parser.program()

    # Transpilación
    generador = GeneradorCodigo()
    codigo_python = generador.visit(arbol)

    print("=" * 60)
    print("CÓDIGO TRADUCIDO (PYTHON):")
    print("=" * 60)
    print(codigo_python)
    print("=" * 60)

    print("\nEJECUTANDO ESTRATEGIA EN EL MOTOR PYTHON:")
    print("-" * 60)
    # Aquí se cumple la exigencia de usar exec() para ejecutar dinámicamente el código
    exec(codigo_python, globals())
    print("-" * 60)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python generador_codigo.py <archivo_f1>")
        sys.exit(1)
        
    ruta_archivo = sys.argv[1]
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
        sys.exit(1)
        
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        codigo_prueba = archivo.read()
        
    print(f"Leyendo programa desde: {ruta_archivo}")
    compilar_y_ejecutar(codigo_prueba)