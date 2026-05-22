---
name: referencia-curriculo
description: Consulta el currículo de Python del Tutorial de Picuino (clases 1 a 33). Usa esta skill cuando necesites conocer el foco, conceptos, sintaxis, actividades originales o URL de una clase específica del programa, o cuando necesites verificar la progresión y prerrequisitos entre clases. Es una skill de consulta, no de generación.
---

# Skill: Referencia del currículo Picuino (clases 1-33)

## Propósito

Esta skill es una referencia consultable del Tutorial de Python de Picuino. Permite saber, para cualquier clase del programa:

- Foco principal
- Conceptos recuperados
- Sintaxis y herramientas clave
- Actividades originales
- URL oficial
- Sugerencias de uso pedagógico

El contenido completo está en `curriculo_picuino_completo.md`. Este SKILL.md actúa como índice navegable para no cargar todo el documento cuando solo se necesita una clase específica.

## Cuándo usar esta skill

Actívate cuando:

- La skill `disenar-clase` necesite confirmar el foco de una clase Picuino
- Diego mencione un número de clase Picuino sin más contexto
- Necesites verificar qué contenidos vienen antes o después de una clase para validar prerrequisitos
- Estés diseñando ejercicios y quieras revisar las actividades originales que propone Picuino para inspirarte (no para copiar literal)
- Quieras consultar la sintaxis exacta que introduce Picuino para un tema

## Cómo consultar el documento

El archivo `curriculo_picuino_completo.md` tiene dos secciones grandes:

1. **Mapa general de progresión** (líneas 9-46): tabla con las 33 clases en una sola vista. Útil para ver de un vistazo qué cubre cada clase y compararlas.

2. **Fichas por clase** (líneas 47 en adelante): cada clase tiene su ficha con `### N. [Título]`. Estructura de cada ficha:
   - URL
   - Foco
   - Conceptos recuperados
   - Sintaxis / herramientas
   - Actividades o ejercicios recuperados
   - Uso pedagógico sugerido

Para buscar una clase específica, usa `grep` o lee solo el rango de líneas de esa ficha. **No leas todo el archivo de una sola vez** salvo que sea estrictamente necesario.

Comandos útiles:

```bash
# Ver la tabla general completa
sed -n '9,46p' curriculo_picuino_completo.md

# Buscar el inicio de una ficha específica
grep -n "^### 9\." curriculo_picuino_completo.md

# Leer la ficha de la clase 9 (ajustando rangos según resultado del grep)
sed -n '180,210p' curriculo_picuino_completo.md
```

## Mapa rápido de las 33 clases

Esta tabla resumida sirve para identificar la clase correcta sin abrir el documento completo:

| # | Tema | Foco breve |
|---:|---|---|
| 1 | Introducción al lenguaje Python | Qué es Python, IDLE, primeros pasos |
| 2 | Datos numéricos | int, float, operadores aritméticos |
| 3 | Las variables | Asignación, nombres significativos |
| 4 | Palabras reservadas | Identificadores válidos, funciones integradas |
| 5 | Los comentarios | Uso de `#` y criterio para comentar |
| 6 | La función print() | Salida por pantalla, `sep` y `end` |
| 7 | La función input() | Entrada por teclado, conversiones |
| 8 | El tipo Booleano | True/False, comparaciones, lógica |
| 9 | Sentencia if else | Control de flujo condicional |
| 10 | Operadores and, or, not | Condiciones compuestas |
| 11 | Sentencias if anidadas | Decisiones jerárquicas |
| 12 | Sentencia elif | Múltiples condiciones |
| 13 | Sentencia for | Bucles definidos |
| 14 | La función range() | Generar secuencias numéricas |
| 15 | Sentencia continue | Saltar iteración |
| 16 | Sentencia break | Interrumpir bucle, for/else |
| 17 | Sentencias for anidadas | Bucles dentro de bucles |
| 18 | Sentencia while | Bucles condicionados |
| 19 | Definición de funciones | def, parámetros, return |
| 20 | Parámetros con valores por omisión | Argumentos opcionales |
| 21 | Cadenas de texto | Manipulación básica de strings |
| 22 | Índices de cadenas | Acceso, rebanadas, iteración |
| 23 | Métodos de cadenas | upper, find, replace, in |
| 24 | Formateo de cadenas | f-strings, formatos numéricos |
| 25 | Listas | Estructuras ordenadas, operaciones básicas |
| 26 | Índices de listas | Acceso, rebanadas, modificación |
| 27 | Iteración de listas | Recorrer y generar listas |
| 28 | Métodos de listas | append, pop, index |
| 29 | Búsqueda de datos | Búsqueda lineal manual |
| 30 | Búsqueda binaria | Algoritmo eficiente |
| 31 | Desplazamiento de datos | Intercambio y desplazamientos |
| 32 | Ordenación por selección | Selection sort |
| 33 | Ordenación por inserción | Insertion sort |

## Prerrequisitos por clase (regla general)

Por defecto, **cada clase asume que se vieron todas las clases anteriores**. Algunas dependencias especialmente fuertes:

- Clase 9 (if-else) requiere clase 8 (booleanos)
- Clase 10 (and/or/not) y 11 (if anidadas) y 12 (elif) requieren clase 9
- Clase 13 (for) y 18 (while) son las dos formas de bucle: pueden enseñarse en orden, pero clase 13 viene antes en Picuino
- Clase 14 (range) requiere clase 13
- Clases 15-17 requieren clases 13-14
- Clase 19 (funciones) puede enseñarse después de cualquier estructura de control básica
- Clases 25-28 (listas) son un bloque coherente, conviene mantenerlas juntas
- Clases 29-33 (algoritmos) requieren funciones (19), listas (25-28) y bucles (13)

## Bloques temáticos del programa

Para planificación de unidades, las 33 clases agrupan así:

| Bloque | Clases | Tema general |
|---|---|---|
| Fundamentos | 1-7 | Sintaxis básica, variables, I/O |
| Lógica y control | 8-12 | Booleanos y condicionales |
| Iteración | 13-18 | Bucles for y while |
| Abstracción | 19-20 | Funciones |
| Datos textuales | 21-24 | Strings |
| Datos colección | 25-28 | Listas |
| Algoritmos | 29-33 | Búsqueda y ordenación |

## Reglas de uso

1. **El currículo Picuino es referencia, no plantilla.** No copies literalmente las actividades de Picuino. Adáptalas al contexto chileno de 4to medio y a los intereses del curso (usa `referencia-intereses-estudiantes` para esto).

2. **Picuino usa IDLE; Diego usa Colab.** Cualquier mención a IDLE, F5 o "guardar archivo .py" debe traducirse a celdas de Colab y `Shift+Enter`.

3. **El uso pedagógico sugerido es opinable.** Las notas de "uso pedagógico" al final de cada ficha son sugerencias generales, no instrucciones obligatorias. Diego decide cómo abordar cada clase según su contexto.

4. **No inventes contenido fuera del programa Picuino.** Si Diego pregunta por una clase fuera del rango 1-33, indica que esta skill cubre solo ese tramo y pide confirmación.

## Atribución

El documento de referencia se basa en: Picuino, Tutorial de Python, Carlos Félix Pardo Martín. Contenidos bajo licencia CC BY-SA 4.0. Fuente: https://www.picuino.com/es/python.html
