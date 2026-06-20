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

> **Nota:** Es necesario reiniciar tu IDE tras instalar Graphviz para que el sistema reconozca la ruta en el PATH.

---

## 2. Entorno y Dependencias de Python

Con el entorno virtual activado en la terminal de IntelliJ, instala las librerías necesarias:

```powershell
pip install -r requirements.txt
```

---

## 3. ¿Cómo Ejecutar el Compilador?

Para ver el compilador en acción (incluyendo la generación de código Python y su ejecución dinámica), ejecuta el módulo principal:

```powershell
python generador_codigo.py
```

### Otras herramientas disponibles

#### Análisis Léxico

```powershell
python herramientas_lexer.py
```

Muestra la tabla detallada de tokens.

#### Análisis Sintáctico

```powershell
python herramientas_ast.py
```

Genera y abre el PNG del Árbol de Sintaxis Abstracta (AST).

#### Análisis Semántico

```powershell
python herramientas_semanticas.py
```

Ejecuta las validaciones de Dirección de Carrera para detectar infracciones semánticas.

---

## Estructura del Proyecto

| Archivo                      | Descripción                                                 |
| ---------------------------- | ----------------------------------------------------------- |
| `F1Compiler.g4`              | Gramática ANTLR oficial del lenguaje.                       |
| `gramatica_ebnf.txt`         | Reglas de la gramática expresadas en formato E-BNF.         |
| `estrategia_carrera.txt`     | Código fuente de ejemplo escrito en lenguaje F1.            |
| `generador_codigo.py`        | Transpilador final que traduce programas F1 a Python.       |
| `herramientas_lexer.py`      | Herramienta para análisis léxico y visualización de tokens. |
| `herramientas_ast.py`        | Generación y visualización del AST mediante Graphviz.       |
| `herramientas_semanticas.py` | Validaciones semánticas y detección de errores.             |
| `requirements.txt`           | Dependencias necesarias para ejecutar el proyecto.          |
| `README.md`                  | Documentación principal del proyecto.                       |

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

## Archivos Adicionales Requeridos

Antes de entregar el proyecto, asegúrate de incluir:

### `gramatica_ebnf.txt`

Contiene la gramática del lenguaje expresada en formato E-BNF.

### `estrategia_carrera.txt`

Contiene un programa de ejemplo escrito en el lenguaje F1Compiler para demostrar el funcionamiento completo del compilador.

---

## Checklist de Entrega

* [ ] `F1Compiler.g4`
* [ ] `gramatica_ebnf.txt`
* [ ] `estrategia_carrera.txt`
* [ ] Todos los archivos `.py`
* [ ] `requirements.txt`
* [ ] `README.md`

---

## Integrantes

* Ariel Leiva
* Franco Bernal
* Felipe Romero
* Hugo Palomino

---

**Autómatas y Compiladores — Semestre 1, 2026**
