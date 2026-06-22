# herramientas_ast.py
import sys
import os

# 1. Añadir raíz del proyecto en sys.path para importar el paquete 'gen'
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# 2. Soluciona el error de Graphviz inyectando la ruta de instalación al PATH de esta sesión
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

from graphviz import Digraph
from antlr4 import InputStream, CommonTokenStream
from gen.F1CompilerLexer import F1CompilerLexer
from gen.F1CompilerParser import F1CompilerParser

def visualizar_arbol(nodo, parser, grafo=None, id_padre=None, contador=None):
    if contador is None:
        contador = [0]

    if grafo is None:
        grafo = Digraph()
        contador[0] = 0

    # Determinar la etiqueta de este nodo
    if nodo.getChildCount() == 0:
        etiqueta = nodo.getText()
    else:
        etiqueta = parser.ruleNames[nodo.getRuleIndex()]

    if not etiqueta or etiqueta.strip() == '':
        etiqueta = '<vacío>'

    # Crear este nodo en el grafo con un ID único
    id_actual = str(contador[0])
    grafo.node(id_actual, etiqueta)
    contador[0] += 1

    # Conectar con el padre si existe
    if id_padre is not None:
        grafo.edge(id_padre, id_actual)

    # Procesar todos los hijos recursivamente
    for i in range(nodo.getChildCount()):
        hijo = nodo.getChild(i)
        visualizar_arbol(hijo, parser, grafo, id_actual, contador)

    return grafo

def analizar_y_visualizar(codigo_fuente, nombre_archivo='ast'):
    flujo_entrada = InputStream(codigo_fuente)
    lexer  = F1CompilerLexer(flujo_entrada)
    tokens = CommonTokenStream(lexer)
    parser = F1CompilerParser(tokens)

    arbol = parser.program()

    print("Árbol en formato texto:")
    print(arbol.toStringTree(recog=parser))
    print()

    grafo = visualizar_arbol(arbol, parser)
    # view=True abrirá la imagen automáticamente en tu visor de imágenes
    grafo.render(nombre_archivo, format='png', cleanup=True, view=True)
    print(f"Imagen generada y abierta como '{nombre_archivo}.png'")

if __name__ == '__main__':
    import sys
    import os
    if len(sys.argv) < 3:
        print("Uso: python {} <archivo_f1> <nombre_arbol>".format(os.path.basename(__file__)))
        sys.exit(1)
        
    ruta_archivo = sys.argv[1]
    nombre_arbol = sys.argv[2]
    
    if not os.path.exists(ruta_archivo):
        print(f"Error: No se encontró el archivo '{ruta_archivo}'")
        sys.exit(1)
        
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        codigo_f1 = archivo.read()
        
    print("Generando telemetría visual del AST...")
    analizar_y_visualizar(codigo_f1, nombre_archivo=nombre_arbol)
