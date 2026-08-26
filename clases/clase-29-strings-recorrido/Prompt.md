# Prompt de sesión — Clase N°29: Strings — recorriendo texto con for

**Fecha programada:** martes 2026-09-01
**Clase Picuino de referencia:** N°22 — Índices de cadenas de texto (parte de recorrido/iteración, separada de N°28 en sesión de diseño 2026-08-26)
**Estado:** clase nueva, creada en sesión de diseño 2026-08-26. Contenidos acordados en chat, spec aún sin generar.

## Origen de esta clase

Surge al diseñar la Clase N°28 (indexing/slicing): el recorrido de cadenas con `for` se sacó de ahí para no diluir el foco en índice/rebanada, y en vez de descartarlo se decidió darle su propia clase — hay suficiente contenido propio (recorrido directo, recorrido con índice, combinación con slicing) más las actividades de Picuino N°22 que quedaban sin usar. Ver el Prompt.md de `clase-28-strings` para el detalle del recorte.

## Contexto acordado (planificación 2026-08-26)

- Segunda de 3 clases de Strings dictadas en la misma semana: N°28 (indexing/slicing, lunes 31-ago) → **N°29 (esta, martes 1-sep)** → N°30 (métodos/f-strings, jueves 3-sep) → N°31 (lunes estándar, control sobre las 3, 7-sep).
- Contenidos previos asumidos: todo hasta N°28 inclusive (Ciclos + Funciones + Strings indexing/slicing). Depende directamente de N°28 — necesita que los estudiantes ya sepan indexar y hacer slicing antes de recorrer con `for`.
- Funciona como puente hacia el patrón de iteración de secuencias que van a reencontrar en Listas (N°33, "iteración y métodos") — vale la pena mencionar esa conexión en el cierre o el propósito.

## Foco de contenido (acordado en chat de diseño 2026-08-26)

- **Recorrer una cadena directo, carácter por carácter:** `for c in texto:` — cuándo alcanza con el carácter, sin necesitar su posición.
- **Recorrer con índice:** `for i in range(len(texto)): texto[i]` — cuándo sí se necesita la posición (compararla, guardarla, usarla en una condición). No es sintaxis nueva (for+range ya consolidado desde N°16/N°20), solo se aplica a un objeto nuevo (cadenas) sumando `len()`.
- **Combinar recorrido + rebanada:** usar el índice del ciclo para armar una versión progresiva o una "ventana" del texto.

**Actividades de Picuino N°22 mapeadas a esta clase (candidatas para Práctica Independiente, a confirmar ejercicio por ejercicio en el diseño):**
- *Deletrea sin índices* (`for c in texto:`) y *deletrea con índices* (`for i in range(len(texto)): texto[i]`) → candidatos a Ejercicios 0a/0b (práctica directa) o ejemplos del ICN.
- *Impresión progresiva desde la izquierda* y *desde la derecha* → candidatos a Ejercicios 1 y 2 (directos).
- *Ventana móvil de cinco caracteres* → candidato a Ejercicio 3 (contextualizado) o Ejercicio 4 (desafío) — es la más compleja de las cinco.

## OAs sugeridos

OA2, OA3 (mismo bloque que N°28 y N°30).

## Qué falta para la especificación completa

Solo se acordó el **foco de contenido** (sección de arriba) — la sesión de diseño 2026-08-26 no llegó a elegir actitud, objetivo ni propósito para esta clase (a diferencia de N°28, que sí los tiene aprobados). Al retomar, `disenar-clase` debe partir desde su Paso 3 (ofrecer opciones de actitud) con este foco de contenido ya como dato de entrada, no desde cero.

## Prompt para iniciar la sesión

> Vamos con la clase nueva de Strings — recorriendo texto con for, para el martes 2026-09-01. Es N°29 en `Historial-Curricular.md`, carpeta `clase-29-strings-recorrido`. Contenidos previos: todo hasta N°28 (Strings indexing/slicing, recién dictada). Foco de contenido ya acordado (ver arriba) — falta elegir actitud, objetivo y propósito. Usa las actividades de Picuino N°22 (deletrea, impresión progresiva, ventana móvil) como base de la Independiente. Actívate con `disenar-clase`.
