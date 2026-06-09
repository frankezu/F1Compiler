# esqueletos_fases_futuras.py

"""
Aquí residen los esquemas para las Fases 2, 3 y 4.
Están comentados listos para que los desarrolles en las próximas sesiones.
"""

# --- FASE 2: ANALIZADOR SINTÁCTICO (Error Listener) ---
# from antlr4.error.ErrorListener import ErrorListener
#
# class MiErrorListener(ErrorListener):
#     def __init__(self):
#         super().__init__()
#         self.errores = []
#
#     def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
#         error = f"Error de sintaxis en línea {line}, columna {column}: {msg}"
#         self.errores.append(error)
#         print(error)


# --- FASE 3: ANÁLISIS SEMÁNTICO (Listener Base) ---
# from F1CompilerListener import F1CompilerListener
# from F1CompilerParser import F1CompilerParser
#
# class AnalizadorSemantico(F1CompilerListener):
#     def __init__(self):
#         self.tabla_simbolos = {}
#         self.errores = []
#
#     def enterDeclaracion(self, ctx):
#         pass
#
#     def enterAsignacion(self, ctx):
#         pass
#
#     def exitProgram(self, ctx):
#         pass


# --- FASE 4: GENERACIÓN DE CÓDIGO (Visitor Base) ---
# from F1CompilerVisitor import F1CompilerVisitor
#
# class GeneradorCodigo(F1CompilerVisitor):
#     def __init__(self):
#         self.lineas_codigo = []
#         self.nivel_indent = 0
#
#     def indentar(self):
#         return "    " * self.nivel_indent
#
#     def visitProgram(self, ctx):
#         self.lineas_codigo.append("# Código generado automáticamente")
#         self.visitChildren(ctx)
#         return "\n".join(self.lineas_codigo)
#
#     def visitDeclaracion(self, ctx):
#         pass
#
#     def visitPrint_stmt(self, ctx):
#         pass
#
#     def visitSi_stmt(self, ctx):
#         pass