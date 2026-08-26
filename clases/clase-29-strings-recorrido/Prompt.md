# Prompt de sesión — Clase N°29: Strings — recorriendo texto con for

**Fecha programada:** martes 2026-09-01
**Clase Picuino de referencia:** N°22 — Índices de cadenas de texto (parte de recorrido/iteración, separada de N°28 en sesión de diseño 2026-08-26)
**Estado:** ✅ Estructura completa de los 5 pasos APROBADA por Diego (sesión de diseño 2026-08-26). **Falta ejecutar el Paso 5 de `disenar-clase`**: escribir el archivo `Clase 29 - Strings - Recorrido - Spec.md` formal con las soluciones de código completas + `**Celda de verificación:**` de cada ejercicio (siguiendo el patrón de `clase-28-strings/Clase 28 - Strings - Spec.md`), crear `Clase 29 - Strings - Recorrido - Historial.md` inicial, actualizar `Historial-Curricular.md` (cambiar estado de N°29 a "Spec aprobada" + fecha), y hacer commit+push solo de la carpeta `clase-29-strings-recorrido/` según el protocolo de cierre de etapa del `CLAUDE.md` raíz. Ningún archivo `.md`/`.ipynb` de este gate se ha guardado todavía — esta sesión se cortó por límite de tokens justo después de la aprobación verbal.

## Origen de esta clase

Surge al diseñar la Clase N°28 (indexing/slicing): el recorrido de cadenas con `for` se sacó de ahí para no diluir el foco en índice/rebanada, y en vez de descartarlo se decidió darle su propia clase — hay suficiente contenido propio (recorrido directo, recorrido con índice, combinación con slicing) más las actividades de Picuino N°22 que quedaban sin usar. Ver el Prompt.md de `clase-28-strings` para el detalle del recorte.

## Contexto acordado (planificación 2026-08-26)

- Segunda de 3 clases de Strings dictadas en la misma semana: N°28 (indexing/slicing, lunes 31-ago) → **N°29 (esta, martes 1-sep)** → N°30 (métodos/f-strings, jueves 3-sep) → N°31 (lunes estándar, control sobre las 3, 7-sep).
- Contenidos previos asumidos: todo hasta N°28 inclusive (Ciclos + Funciones + Strings indexing/slicing). Depende directamente de N°28 — necesita que los estudiantes ya sepan indexar y hacer slicing antes de recorrer con `for`.
- Funciona como puente hacia el patrón de iteración de secuencias que van a reencontrar en Listas (N°33, "iteración y métodos") — vale la pena mencionar esa conexión en el cierre o el propósito.

## Foco de contenido

- **Recorrer una cadena directo, carácter por carácter:** `for c in texto:` — cuándo alcanza con el carácter, sin necesitar su posición.
- **Recorrer con índice:** `for i in range(len(texto)): texto[i]` — cuándo sí se necesita la posición. No es sintaxis nueva (for+range consolidado desde N°16/N°20), solo se aplica a un objeto nuevo (cadenas) sumando `len()`.
- **Combinar recorrido + rebanada:** usar el índice del ciclo para armar una versión progresiva o una "ventana" del texto.

## OAs

OA2, OA3 (mismo bloque que N°28 y N°30).

---

## DECISIONES APROBADAS DE ESTA SESIÓN (2026-08-26)

### Actitud, objetivo y propósito (Paso 3 — APROBADO)

- **Actitud elegida:** Constancia (entre las opciones ofrecidas: Criterio, Método, Paciencia, Constancia).
- **Objetivo:** Construir programas que recorran cadenas de texto con `for` —directo o por índice— y los combinen con rebanadas para generar progresiones y ventanas de texto, con constancia.
- **Propósito:** La constancia es repetir el mismo paso, vuelta tras vuelta, sin saltarte ninguno. Hoy la practicamos recorriendo un texto carácter por carácter con `for`.

### Escenario (rediseñado en la sesión — reemplaza la propuesta inicial de "letrero LED/marcador deportivo")

Diego pidió explícitamente **continuar la línea de problema de patentes de autos** de `clase-28-strings/Clase 28 - Strings - Clase.ipynb` (Registro Civil, patente `"BRTZ21"` = 4 letras + 2 números), en vez de introducir un escenario nuevo. Escenario final aprobado: **un estacionamiento con cámara lectora de patentes en la barrera** (entrada) y una **pantalla angosta en la barrera de salida** que solo muestra unos pocos caracteres a la vez. Reutiliza literalmente la patente `"BRTZ21"` de N°28 en Haz Ahora/ICN, para que el "aha" sea inmediato.

### Paso 4 — Estructura completa APROBADA

**Duración total:** ~74 min dentro del bloque de 80.

#### 1. Haz Ahora (6 min) — texto final aprobado

> La cámara de la barrera del estacionamiento escanea la patente `BRTZ21` leyendo un carácter a la vez, de izquierda a derecha. El guardia, sabiendo que ya saben programar, les pide ayuda para automatizar esto — pero antes, quiere que tengan clara la lógica:
>
> 1. ¿Cuál es el primer carácter que lee la cámara?
> 2. ¿Cuántas veces tiene que "mirar" la cámara para terminar de leer toda la patente?
> 3. Si la cámara falla justo al leer el 3er carácter que escanea, ¿qué carácter de la patente es ese?
> 4. La pantalla angosta de la barrera de salida solo alcanza a mostrar 4 caracteres a la vez de la patente completa. ¿Qué 4 caracteres muestra en la primera imagen, contando desde el inicio?
> 5. Cuando la pantalla se desliza una posición y deja de mostrar la "B", ¿qué carácter nuevo aparece al final?

**Respuestas esperadas:** 1. "B" — 2. 6 veces — 3. "T" — 4. "BRTZ" — 5. "2"

(Nota de diseño: la primera versión de este Haz Ahora usaba un escenario de "letrero LED / marcador deportivo" con el mensaje `"CAMPEONES"` — Diego lo encontró confuso/ni bien simple ni bien complejo y pidió reemplazarlo por la línea de patentes. No reusar esa versión.)

#### 2. Introducción al Contenido Nuevo (18 min) — 3 conceptos, contexto patente/estacionamiento

**Concepto 1 — Recorrer directo, carácter por carácter (`for caracter in patente:`)**
- Ejemplo: `patente = "BRTZ21"` → `for caracter in patente: print(caracter)` (la cámara anuncia/registra cada carácter escaneado, en orden).
- Idea clave: cuando solo necesitas el carácter y no su posición, `for caracter in texto` alcanza.

**Concepto 2 — Recorrer con índice (`for i in range(len(patente)): patente[i]`)**
- Ejemplo: `for i in range(len(patente)): print("Posición", i, "->", patente[i])` — el sistema registra la posición de cada carácter, para poder reportar con precisión si la cámara falla en una posición específica.
- Idea clave: `range(len(texto))` genera exactamente las posiciones válidas del texto, y `texto[i]` entrega el carácter ahí.

**Concepto 3 — Combinar recorrido + rebanada (ventana móvil)**
- Ejemplo: `ancho = 4; for i in range(len(patente) - ancho + 1): print(patente[i:i+ancho])` sobre `"BRTZ21"` → `BRTZ / RTZ2 / TZ21` (la pantalla angosta de la barrera de salida).
- Idea clave: el rango no llega hasta `len(texto)` — hay que restar el ancho de la ventana y sumar 1, para que la última ventana no se salga del texto.

**Errores típicos:** usar `for caracter in patente` cuando se necesita reportar la posición de un carácter fallido; olvidar el `+1` (o restar mal el ancho) al calcular el rango de una ventana; confundir `patente[i]` (un carácter) con `patente[i:i+n]` (un trozo).

#### 3. Práctica Guiada (22 min) — texto final aprobado

> El estacionamiento del mall tiene una pantalla aún más angosta en su barrera de salida, que solo muestra 3 caracteres a la vez. Antes de instalarla, el encargado quiere probar cómo se vería la patente `"FGHT58"` recorriendo esa pantalla.

**El programa debe:** guardar la patente en una variable · calcular cuántas "fotos" de 3 caracteres se necesitan · mostrar cada una, una por línea, deslizándose de a una posición.

**Resultado esperado:** `FGH / GHT / HT5 / T58`

(Verificar al escribir la solución: `patente="FGHT58"` (6 caracteres), `ancho=3` → `range(6-3+1)=range(4)`: i=0,1,2,3 → `FGH`,`GHT`,`HT5`,`T58`. ✅ Cuadra.)

#### 4. Práctica Independiente (17 min) — todo en el universo de patentes/estacionamiento

**Ejercicio 0a — Práctica directa: deletrear sin índice.** Sin narrativa. Consigna técnica: recorrer una patente dada con `for` e imprimir cada carácter en su propia línea. Patente sugerida: `"JKLM52"` (a confirmar/ajustar al escribir la solución).

**Ejercicio 0b — Práctica directa: deletrear con índice.** Sin narrativa. Consigna técnica: recorrer una patente con índice e imprimir cada posición junto a su carácter. Patente sugerida: `"NPQR84"`.

**Ejercicio 1 — Pantalla de la barrera cargando.** La pantalla del sistema, mientras la cámara termina de escanear, muestra la patente apareciendo progresivamente de izquierda a derecha (efecto "cargando"), agregando un carácter más en cada línea. Patente sugerida: `"DFRT39"` (a confirmar).

**Ejercicio 2 — App de transporte compartido.** La app muestra la patente del vehículo asignado revelándose de derecha a izquierda (agregando un carácter más a la izquierda en cada línea), porque recomienda verificar primero los últimos caracteres. Patente sugerida: `"MNQP68"` (a confirmar).

**Ejercicio 3 — Carácter dudoso (contextualizado, combina recorrido con índice + `if` ya visto).** La cámara a veces confunde la letra "O" con el número "0". El programa debe recorrer la patente con índice y reportar en qué posición(es) aparece la letra "O", para que el guardia las revise a mano. Patente sugerida (con 2 apariciones de "O" para que el ejercicio tenga sentido): `"ROTOR25"` → imprime posición 1 y posición 3.

**Ejercicio 4 — Desafío: patente capicúa.** Algunos conductores creen que una patente "capicúa" (se lee igual al derecho y al revés) trae buena suerte. El programa debe comprobarlo con un ciclo con índice que compare cada carácter con su posición simétrica desde el final — generaliza el Ejercicio 4 desafío de la Clase 28 (que solo comparaba 2 pares fijos para un código de 4 caracteres) a patentes de cualquier largo. Patente sugerida (palíndromo real): `"AB22BA"` → `¿Es una patente capicúa? True`.

Todos los ejercicios llevan `**Celda de verificación:**` con su propio `verificar_ejercicio_N()`, siguiendo el patrón exacto de `clase-28-strings` (ver ese Spec.md como plantilla del preámbulo del verificador — copiarlo tal cual).

**Pistas `<details>` a definir al escribir el Spec final** (1-2 por ejercicio, default desde Clase 24b) — no se redactaron aún el texto exacto de cada pista en esta sesión, salvo las ideas ya insinuadas arriba (ventana móvil, posición simétrica, etc.).

#### 5. Ticket de Salida (6 min) — código también con patentes (acordado, contenido exacto de las 4 alternativas por pregunta AÚN NO redactado)

Reemplazar los ejemplos genéricos por variables `patente = "..."` para mantener coherencia visual con el resto de la clase. Ideas ya esbozadas en la sesión (afinar al escribir el Spec):

- **Pregunta 1** (recorrido directo): `patente = "AB12"; for c in patente: print(c)` — predecir que imprime "A","B","1","2" cada uno en su propia línea. Distractores: todo en una línea, orden invertido, imprime "AB12" una sola vez.
- **Pregunta 2** (recorrido con índice, distractor off-by-one): `patente = "XY45"; for i in range(len(patente)): print(i, patente[i])` — correcto: `0 X / 1 Y / 2 4 / 3 5`. Distractores: arranca en 1 (off-by-one), invierte el orden de los argumentos del print, "solo imprime la última línea".
- **Pregunta 3** (fórmula de ventana móvil): `patente = "KLMN73"; ancho = 4; for i in range(len(patente) - ancho + 1): print(patente[i:i+ancho])` — correcto: `KLMN / LMN7 / MN73`. Distractores: no resta `ancho+1` (imprime de más, incluyendo trozos cortos fuera de rango), usa un ancho equivocado, "solo se ejecuta una vez".

Repartir la respuesta correcta en 3 letras distintas (A/B/C/D, sin repetir) — no asignadas todavía en esta sesión.

#### Cierre (5 min)

- **Objetivo:** el mismo de arriba (reimpreso).
- **Pregunta 1 — Metacognición (1-5):** qué tan seguro/a se siente recorriendo un texto con `for` (directo/índice) y combinándolo con rebanadas.
- **Pregunta 2 — Actitud proyectada:** en qué otra situación real hay que repetir el mismo paso, uno por uno, sin saltarse ninguno — conectada a Constancia.

---

## Qué falta exactamente para cerrar el gate de Spec

1. Escribir `clases/clase-29-strings-recorrido/Clase 29 - Strings - Recorrido - Spec.md` completo, con:
   - Todo el contenido ya aprobado arriba, en el formato canónico de `disenar-clase` (ver plantilla del SKILL.md y `clase-28-strings/Clase 28 - Strings - Spec.md` como referencia de formato real).
   - Las patentes "sugeridas" de cada ejercicio Independiente están anotadas como *a confirmar* — verificar que no se repitan entre ejercicios y que produzcan el resultado esperado exacto antes de fijarlas.
   - Código de solución completo de cada ejercicio (Guiada + 0a/0b/1/2/3/4) + su `**Celda de verificación:**` con `esperadas = [...]`, siguiendo el patrón de N°28.
   - Las 3 preguntas del Ticket de Salida con sus 4 alternativas A/B/C/D completas, respuesta correcta y justificación — el contenido conceptual ya está decidido arriba, falta solo redactar las alternativas.
   - Pistas `<details>` de cada ejercicio de la Independiente (1-2 c/u).
   - Sección "Decisiones de diseño relevantes" registrando: el cambio de escenario (LED deportivo → patentes, a pedido de Diego) y la razón de continuidad con N°28.
2. Crear `Clase 29 - Strings - Recorrido - Historial.md` inicial con el resumen de esta sesión de diseño.
3. Actualizar `clases/Historial-Curricular.md`: cambiar el estado de la fila N°29 de "Contenidos acordados en chat de diseño — spec sin generar" a "Spec aprobada" + fecha, y actualizar la línea correspondiente en "Próxima clase disponible".
4. Commit + push **solo** de `clases/clase-29-strings-recorrido/` (protocolo de cierre de etapa del `CLAUDE.md` raíz) — mensaje sugerido: `Clase 29 - Strings - Recorrido: Spec aprobada`.
5. Confirmar a Diego qué se guardó/subió, recomendar `/compact`, y activar `generar-colab-clase` cuando él esté listo.

## Prompt para retomar la sesión

> Retomemos la Clase 29 (Strings — recorriendo texto con for). Ya está todo aprobado por mí en la sesión de diseño anterior (2026-08-26): actitud Constancia, objetivo, propósito, y la estructura completa de los 5 pasos con el escenario de patentes/estacionamiento (continuación de la Clase 28). Todo el detalle aprobado está en `clases/clase-29-strings-recorrido/Prompt.md` — falta solo ejecutar el Paso 5 de `disenar-clase`: escribir el Spec.md formal con las soluciones de código y los verificadores, el Historial.md, actualizar Historial-Curricular.md, y hacer commit+push. Actívate con `disenar-clase` directo en el Paso 5, no vuelvas a proponer estructura desde cero.
