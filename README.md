# F1Compiler 🏎️

> **IMPORTANTE:** Ya moví la primera celda fuera del notebook `skeleton.ipynb` hacia el archivo `F1Compiler.g4`, lo demás del proyecto sigue en el notebook, por lo tanto, lo ideal sería seguir moviendo las demás celdas de código hacia archivos .py independientes para que quede todo más ordenado y profesional, y que quede un archivo `main.py` que conecte todo. Lo otro, el archivo del lenguaje ya no se llama `MiLenguaje`, le puse `F1Compiler`, lo digo, ya que las últimas celdas donde se importa el lenguaje no está actualizado el nombre.

---

## 1. Dependencias del sistema

**Windows (PowerShell como Administrador):**
```powershell
winget install Oracle.JDK.17
winget install Graphviz.Graphviz
```

## 2. Dependencias de Python

Con el entorno virtual activado en la terminal de IntelliJ:
```pip install -r requirements.txt```

## 3. Configuración ANTLR v4 en IntelliJ

1. Instalar el plugin ANTLR v4.
2. Clic derecho en F1Compiler.g4 -> Configure ANTLR...
3. Establecer Language en Python3.
4. Dejar Output directory por defecto (apunta a gen).
5. Marcar Generate parse tree listener y Generate parse tree visitor.
6. Clic en OK.
7. Clic derecho en F1Compiler.g4 -> Generate ANTLR Recognizer.

## 4. Directorio de Fuentes

1. En el panel izquierdo del proyecto, hacer clic derecho en la carpeta autogenerada gen.
2. Seleccionar Mark Directory as -> Sources Root.