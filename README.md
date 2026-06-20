# F1Compiler 🏎️

**Lenguaje de programación basado en telemetría y estrategias de Fórmula 1.**
*Creado por: Ariel Leiva, Franco Bernal, Felipe Romero, Hugo Palomino.*

---

## Ambición Técnica (Sección Z3 de la Rúbrica)

Para lograr un resultado más robusto y profesional, hemos migrado el esquema inicial del Jupyter Notebook hacia un **proyecto modular en Python puro**. Esta arquitectura nos permitió segmentar el Lexer, Parser, Análisis Semántico y Generación de Código en archivos especializados, logrando un código limpio, mantenible y la renderización en tiempo real del Árbol de Sintaxis Abstracta (AST) usando **Graphviz** nativo en el sistema.

---

## 1. Dependencias del Sistema (Windows)

Abre PowerShell como administrador y ejecuta:

```powershell
winget install Oracle.JDK.17
winget install Graphviz.Graphviz
```

> **Nota 1:** Es necesario reiniciar tu IDE tras instalar Graphviz para que el sistema reconozca la ruta en el PATH.
> **Nota 2:** La instalación de Java (`Oracle.JDK.17`) es **opcional** y solo es necesaria si deseas volver a compilar la gramática desde cero. Para ejecutar y evaluar este proyecto, la carpeta autogenerada `gen/` ya viene incluida en el repositorio.

---

## 2. Entorno y Dependencias de Python

Con el entorno virtual activado en la terminal de IntelliJ, instala las librerías necesarias:

```powershell
pip install -r requirements.txt
```

---

## 3. ¿Cómo Ejecutar el Compilador?

### Opción A: Ejecutar el flujo completo vía Notebook (Recomendado)

La forma más sencilla de evaluar el proyecto es a través del archivo **`F1Compiler.ipynb`**. 
1. Sube el `.zip` del proyecto a Google Colab o ábrelo localmente en Jupyter Notebook.
2. Ejecuta las celdas en orden (Shift + Enter). El notebook instalará las dependencias y ejecutará cada una de las fases del compilador automáticamente, imprimiendo los resultados.

### Opción B: Ejecutar vía Terminal

Para ver el compilador en acción (incluyendo la generación de código Python y su ejecución dinámica) desde tu consola, ejecuta el módulo principal:

```powershell
python generador_codigo.py
```

### Otras herramientas disponibles

#### Análisis Léxico

```powershell
python ejecutar_lexer.py
```

Muestra la tabla detallada de tokens.

#### Análisis Sintáctico

```powershell
python src/tools/herramientas_ast.py
```

Genera y abre el PNG del Árbol de Sintaxis Abstracta (AST).

#### Análisis Semántico

```powershell
python src/tools/herramientas_semanticas.py
```

Ejecuta las validaciones de Dirección de Carrera para detectar infracciones semánticas.

#### Casos de Prueba

```powershell
python casos_prueba.py
```

Ejecuta tres baterías de pruebas distintas validando la correctitud de todas las características.

---

## Estructura del Proyecto

| Archivo                            | Descripción                                                 |
| ---------------------------------- | ----------------------------------------------------------- |
| `F1Compiler.ipynb`                 | Notebook principal para ejecutar el pipeline completo.      |
| `src/core/F1Compiler.g4`           | Gramática ANTLR oficial del lenguaje.                       |
| `docs/gramatica_ebnf.txt`          | Reglas de la gramática expresadas en formato E-BNF.         |
| `examples/estrategia_carrera.txt`  | Código fuente de ejemplo escrito en lenguaje F1.            |
| `generador_codigo.py`              | Transpilador final que traduce programas F1 a Python.       |
| `ejecutar_lexer.py`                | Script de entrada para visualizar la tabla de tokens.       |
| `casos_prueba.py`                  | Diferentes escenarios de pruebas y testeo del lenguaje.     |
| `src/tools/herramientas_ast.py`    | Generación y visualización del AST mediante Graphviz.       |
| `src/tools/herramientas_semanticas.py` | Validaciones semánticas y detección de errores.         |
| `gen/`                             | Carpeta con los analizadores generados por ANTLR.           |

---

## Flujo de Compilación

El compilador sigue las fases clásicas de construcción de compiladores:

1. **Análisis Léxico**

    * Reconocimiento de tokens.
    * Validación de símbolos válidos.

2. **Análisis Sintáctico**

    * Construcción del Árbol de Sintaxis Abstracta (AST).
    * Verificación de estructura gramatical.

3. **Análisis Semántico**

    * Validación de reglas del dominio Fórmula 1.
    * Detección de infracciones de carrera.

4. **Generación de Código**

    * Traducción del programa F1 a código Python ejecutable.
    * Ejecución dinámica del resultado.

---

## Características Destacadas

* Gramática diseñada en ANTLR4.
* Lexer y Parser personalizados en Python.
* AST visualizado automáticamente mediante Graphviz.
* Verificación semántica inspirada en Dirección de Carrera de Fórmula 1.
* Generación automática de código Python.
* Arquitectura modular y mantenible.
* Proyecto alineado con los requisitos de la sección Z3 (Ambición Técnica).

---


## Integrantes

* Ariel Leiva
* Franco Bernal
* Felipe Romero
* Hugo Palomino

---

**Autómatas y Compiladores — Semestre 1, 2026**
