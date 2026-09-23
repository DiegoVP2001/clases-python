# Prompt de sesión — Clase N°35: Listas — creación y acceso

**Fecha programada:** lunes 2026-09-28 (retorno de vacaciones de Fiestas Patrias)
**Clase Picuino de referencia:** N°25 — Listas + N°26 — Índices de listas
**Estado:** sin propuesta aún.

## Contexto acordado (planificación 2026-08-20, renumerada y refechada varias veces — ver historial completo abajo)

- Arranca el bloque temático "Datos colección" (Listas), después del bloque completo de Strings: N°28-N°29 (indexing/recorrido), N°31 (lunes estándar control, foco solo N°28 y N°29), N°32 (métodos modificar/separar), N°33 (búsqueda de texto, `in`/`find()`) y N°34 (Control Strings Métodos y Búsqueda, cubre N°32 y N°33).
- Contenidos previos asumidos: todo hasta N°34 inclusive (Strings completo: indexing/slicing, recorrido con `for`, métodos para modificar/separar, búsqueda de texto, el lunes estándar de control N°31 —cuyo foco fue solo N°28 y N°29— y el Control N°34 —cuyo foco fue N°32 y N°33—). **f-strings NO se ha visto** — quedó pendiente sin clase asignada (ver `Historial-Curricular.md`), no asumir que los estudiantes conocen formateo con f-strings.
- **Cuarta renumeración y refechada, 2026-09-11:** al crear el Control N°34 (Strings Métodos y Búsqueda, martes 15-sep — clase nueva, necesaria porque la Clase 33 se atrasó y se dicta recién el lunes 14-sep), esta clase pasó de **N°34** a **N°35**, y su fecha se corrió del jueves 10-sep al **lunes 28-sep** (retorno de Fiestas Patrias), reemplazando ahí al "Kahoot de reactivación" que el `Plan Cierre 4to Medio y Continuidad 3ro - Agosto a Noviembre 2026.md` tenía asignado ese día. Carpeta renombrada de `clase-34-listas` a `clase-35-listas`. Ver `Historial-Curricular.md`, nota "Renumeración 2026-09-11", y `Clase 34 - Control Strings Métodos y Búsqueda - Prompt.md` para el detalle completo del Control que motivó este corrimiento.
- **Tercera renumeración 2026-09-03 (sin refechada):** la clase de métodos de texto se renumeró de N°30 a N°32, corriendo en cascada todo lo que venía después — esta clase pasó de **N°33** a **N°34** (la búsqueda de texto pasó de N°32 a N°33). Carpeta renombrada de `clase-33-listas` a `clase-34-listas`.
- **Segunda renumeración y refechada 2026-08-26:** al dividir la antigua Clase 30 (métodos+f-strings) en dos, se insertó la Clase N°32 nueva (Strings — búsqueda de texto) el martes 08-sep, ocupando la fecha que tenía esta clase — así que esta clase pasó a **N°33** y su fecha se corrió al **jueves 10-sep**. Carpeta renombrada de `clase-32-listas` a `clase-33-listas`.
- **Primera renumeración y refechada 2026-08-26:** esta clase era N°30 (jueves 10-sep) hasta que se insertó la Clase N°29 nueva (recorrido con `for`) y su lunes estándar N°31 — pasó a N°32, fecha adelantada a martes 08-sep. Carpeta renombrada de `clase-30-listas` a `clase-32-listas`.

Ver `Historial-Curricular.md` para el detalle completo de cada renumeración.

## Decisión 2026-09-23 — alineación con el Proyecto Cierre Octubre

Cerrada en `clases/clases-octubre/Proyecto Cierre Octubre - Plan y Pendientes.md` sección 6. `guaguas` (nombres inscritos en Chile 1920-2021, Registro Civil) es el hilo conductor de contenido de **N°35, N°36 y las mini-clases del 1 y 5-oct** — excepción explícita y autorizada por Diego a la restricción permanente 3 del `CLAUDE.md` raíz (contextos variados), solo para este bloque.

- **La sesión abre con un lanzamiento de 15-20 min** del proyecto (presentación del menú de 5 áreas / 9 bases, ver catastro §4) antes de entrar al contenido de N°35 — no ocupa una sesión aparte de las 14 que quedan.
- **Eje del ICN de N°35:** una fila de un CSV de `guaguas`, en texto, se convierte en lista con `split(",")`; luego se accede por índice y slicing. Puente explícito con Clase 32 (donde se vio `split()`).
  ```python
  fila = "2021,Agustina,F,1234"
  datos = fila.split(",")
  print("Nombre:", datos[1])
  >> Nombre: Agustina
  print("Año y nombre:", datos[0:2])
  >> Año y nombre: ['2021', 'Agustina']
  ```
- **Objetivo propuesto para N°36 (Listas — iteración y métodos, aún sin carpeta/spec):** columnas de `guaguas` como listas paralelas (nombres / cantidad), recorridas con `for` para contar, sumar/promediar, encontrar el máximo y filtrar construyendo una lista nueva con `append` — el mismo `groupby` que pandas hará en una línea el 1-oct.
- **1-oct y 5-oct (pandas):** misma base `guaguas`, mismo CSV — 1-oct abre/mira, 5-oct filtra/agrupa/grafica. La transición Listas→pandas queda literal, no solo temática.
- ⚠️ pandas no entra en la Evaluación del 8-oct — avisarlo explícito para no generar ansiedad.

## Foco de contenido (de la ficha Picuino N°25 y N°26)

- Listas como conjunto ordenado entre corchetes, elementos de tipos mixtos, listas anidadas, listas escritas en varias líneas; concatenar con `+`, repetir con `*`; `in`/`not in` para pertenencia.
- Índices desde 0, índices negativos, slicing (`lista[1:-1]`), modificar un elemento por índice (`lista[0] = 'A'`).
- Conexión natural con lo recién visto en Strings (mismo mecanismo de índices/slicing, ahora sobre otra estructura — y `in` ya se vio para texto en la Clase 33 y se reforzó en el Control N°34, ahora se retoma para listas) — vale la pena hacerlo explícito en el ICN.

## OAs sugeridos

OA1, OA2, OA3.

## Prompt para iniciar la sesión

> Vamos con la clase de Listas — creación y acceso (Picuino N°25+N°26), para el lunes 2026-09-28 (retorno de Fiestas Patrias). Es N°35 en `Historial-Curricular.md`, carpeta `clase-35-listas`. Contenidos previos: todo hasta N°34 (Strings completo + su lunes estándar N°31 + el Control N°34 de métodos y búsqueda). Actívate con `disenar-clase`.
