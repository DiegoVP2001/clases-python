# Reforzamiento — Debuggear errores de Python

## Contexto
- **Curso:** 4to Medio
- **Sesión:** Martes — Reforzamiento previo a evaluación del jueves
- **Contenidos nuevos:** Debuggear errores de sintaxis, lógica e indentación
- **Contenidos previos:** Clases 1–7 (variables, tipos, operadores, `print()`, `input()`, comentarios, booleanos)

## Objetivo
Debuggear errores de Python: identificar y corregir errores de `sintaxis`, `lógica` e `indentación` en un programa.

## Propósito
Practicar las habilidades que entran en la evaluación del jueves, entendiendo que debuggear es una habilidad central de cualquier programador.

## Estructura de la clase
1. Haz Ahora — ¿Verdadero o Falso?
2. ¿Qué es debuggear?
3. Práctica guiada — depuramos juntos (en el Colab)
4. Práctica independiente — depuras tú (en el Colab)
5. Ejercicios a elección (en el Colab)

### 1. Haz Ahora

**Actividad:** ¿Verdadero o Falso? Sin ejecutar, escribe V o F en tu cuaderno para cada caso.

1. `nota promedio = 6.5` → Esta línea es válida en Python.  *(F — espacio en el nombre)*
2. `total = 10 + 20 / 2` → `total` vale `15`.  *(F — vale 20: primero se divide 20/2, luego se suma 10)*
3. ¿El siguiente código da error? *(V — indentación inesperada)*

```python
precio = 990
    descuento = 100
```

### 2. Introducción al Contenido Nuevo

**Concepto 1: Error de sintaxis**
- Definición: Python no puede leer el código y se detiene con un mensaje de error antes de ejecutar nada.
- Ejemplo:
  ```python
  nota promedio = 6.0   # espacio en el nombre
  precio = 4.990        # punto como separador decimal
  nombre = "Juan        # comilla sin cerrar
  ```
- Idea clave: Si Python lanza `SyntaxError`, busca el problema en la línea indicada.

**Concepto 2: Error de lógica**
- Definición: El código se ejecuta sin errores, pero da un resultado incorrecto porque la operación está mal planteada.
- Ejemplo:
  ```python
  promedio = nota_1 + nota_2 + nota_3 / 3   # mal: divide solo nota_3
  promedio = (nota_1 + nota_2 + nota_3) / 3  # correcto
  ```
- Idea clave: Sin mensaje de error, compara el resultado obtenido con el esperado.

**Concepto 3: Error de indentación**
- Definición: Una línea tiene sangría inesperada al inicio del programa, sin un bloque que la justifique.
- Ejemplo:
  ```python
  precio = 990
      descuento = 100   # IndentationError: unexpected indent
  ```
- Idea clave: En Python la sangría tiene significado — úsala solo cuando corresponde.

**Errores típicos:**
| Tipo | Qué pasa | Ejemplos |
|---|---|---|
| `SyntaxError` | Python no puede leer el código — se detiene antes de correr | `nota promedio = 5` / `precio = 4.990` / `nombre = "Juan` |
| Error de lógica | El código corre pero el resultado es incorrecto | `total / 3` en vez de `(a + b + c) / 3` |
| `IndentationError` | Sangría inesperada — Python no sabe a qué bloque pertenece la línea | `    descuento = 100` al inicio del programa |
