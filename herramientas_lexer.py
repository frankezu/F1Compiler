# herramientas_lexer.py
from antlr4 import InputStream, CommonTokenStream
from F1CompilerLexer import F1CompilerLexer
from F1CompilerParser import F1CompilerParser

def mostrar_tokens(codigo_fuente):
    """
    Ejecuta SOLO el Lexer sobre el código fuente y muestra en pantalla
    la lista completa de tokens reconocidos con su tipo, texto, línea y columna.
    """
    flujo_entrada = InputStream(codigo_fuente)
    lexer = F1CompilerLexer(flujo_entrada)
    flujo_tokens = CommonTokenStream(lexer)
    flujo_tokens.fill()

    tokens = flujo_tokens.tokens

    print(f"{'Num':<5} {'Tipo':<25} {'Texto':<30} {'Línea':<8} {'Columna'}")
    print("-" * 80)

    for token in tokens:
        tipo_num = token.type

        if tipo_num == -1:
            nombre_tipo = "EOF"
        else:
            nombre_tipo = lexer.symbolicNames[tipo_num] if tipo_num < len(lexer.symbolicNames) else str(tipo_num)

        texto = repr(token.text)
        linea = token.line
        columna = token.column

        print(f"{tipo_num:<5} {nombre_tipo:<25} {texto:<30} {linea:<8} {columna}")

def contar_tokens_por_tipo(codigo_fuente):
    """
    Cuenta cuántos tokens de cada tipo aparecen en el código fuente
    y muestra el resultado ordenado de mayor a menor.
    """
    flujo_entrada = InputStream(codigo_fuente)
    lexer = F1CompilerLexer(flujo_entrada)
    flujo_tokens = CommonTokenStream(lexer)
    flujo_tokens.fill()

    conteo = {}
    for token in flujo_tokens.tokens:
        tipo_num = token.type
        if tipo_num == -1:
            nombre = "EOF"
        else:
            nombre = lexer.symbolicNames[tipo_num] if tipo_num < len(lexer.symbolicNames) else str(tipo_num)
        conteo[nombre] = conteo.get(nombre, 0) + 1

    print("Resumen de tokens encontrados:")
    print(f"  {'Tipo':<25} {'Cantidad'}")
    print("  " + "-" * 35)
    for nombre, cantidad in sorted(conteo.items(), key=lambda x: -x[1]):
        print(f"  {nombre:<25} {cantidad}")
    print(f"\n  Total (incluyendo EOF): {sum(conteo.values())}")