# Historial — Clase 36b (Mi base: abrir y mirar)

## 2026-10-06 — Links en una celda de código comentada

- La tabla de links (que dentro de markdown era incómoda de copiar) se reemplaza por **una celda de código con todo comentado**: número, nombre de la base y su link entre comillas, listo para pegar en `pd.read_csv(...)`. Ejecutarla no hace nada.
- Verificado: la celda no contiene líneas que no sean comentario, no quedó ningún link suelto en el markdown, y los 9 links cargan en vivo desde GitHub con las formas esperadas.

## 2026-10-06 — Solucionario y encabezado vacío para estudiantes

- **Cuaderno de estudiantes:** la celda donde escriben el encabezado queda **vacía**. La instrucción de arriba solo nombra qué herramienta va en cada línea.
- **Nuevo `Clase 36b - Mi Base - Abrir y Mirar - Solucionario.ipynb`** (solo profesor), generado desde el mismo `generar_cuaderno.py` y ejecutado contra la URL real para dejar los resultados guardados. Trae: tabla de qué se revisa en cada parte (Proceso), el **encabezado terminado** (renderizado y con su texto fuente línea por línea, con marcadores *Estudiante 1/2*), y los Pasos 1-5 + bitácora resueltos con **CONASET RM** como base de ejemplo, con su link.
- Dato real usado en el ejemplo: `Ruta` trae solo un espacio en 118.077 de 123.343 filas; pandas no lo cuenta como vacío (anzuelo para la clase 37).

## 2026-10-06 — Ajustes tras revisar el cuaderno

- **Markdown:** la mini-lección pasa de una tabla suelta a **escribir en conjunto el encabezado del proyecto** (nombre, base de datos, integrantes, por qué esa base), con una herramienta de markdown por línea: título, negrita, lista, cita y línea separadora; código en línea y cursiva quedan como extras para las respuestas. La celda-plantilla trae todo el esqueleto para completar. Se amplía a ~10 min en el guion.
- **Pistas siempre visibles:** se eliminan todos los `<details>`. Razón: dentro de una celda de markdown, un doble clic para abrir la pista entra al modo edición y muestra el código fuente. Ahora hay una tabla "qué ves → qué falta → se arregla con" y una sección visible por parámetro (`sep=`, `encoding=`, `header=`), más archivos pesados y la tabla "cómo se abre cada base". La pista del Paso 4 es una cita visible.
- **Sin "guardar una copia":** se quita la sección y el paso de la entrega, porque Classroom entrega una copia a cada estudiante. La entrega queda en ejecutar todo, revisar las celdas 📝 y presionar **Entregar**.
- Verificación repetida: ejecución limpia con celdas vacías y Pasos 1-4 rellenados en CONASET RM, Hospitalarias y SIMCE.

## 2026-10-06 — Diseño y generación

**Por qué existe.** Diego perdió clases y va a perder más, así que cambió el patrón del bloque pandas: *por cada clase de contenido, la siguiente es de aplicación* — cada equipo usa lo recién visto sobre la base que eligió para el proyecto. Esta es la primera (aplica N°36). Los números de N°37-N°40 y su calendario no se tocaron: siguen pendientes de reprogramación (Calendario v2 sin aprobar).

**Decisiones de Diego en la sesión de diseño**
- Un solo cuaderno para todos: preguntas amplias ("¿cuáles son las dimensiones de tu base?") que sirven para cualquier base. Sin personalizar según desempeño previo; hoy se quiere ver cómo les va solo con un repaso de N°36.
- Abre con la rúbrica resumida (las 4 notas + qué se mira de este cuaderno para **Proceso 15%**), sigue con el resumen de comandos de N°36 (sin `.notna()`, que no se enseñó) y una mini-lección de markdown.
- Las respuestas se escriben en markdown dentro del cuaderno y se entregan en Classroom como parte de la nota de Proceso.
- Incluye la tabla de equipos y bases elegidas, y los links de las 9 bases con pistas desplegables que explican `sep`, `encoding` y `header`.
- CONASET se recorta a la Región Metropolitana **con todas las columnas** y se sube hoy.
- Quien no se ha inscrito elige base hoy.
- Cierre del trabajo: "Ahora que saben lo que hay, ¿qué pregunta les gustaría responder?" (borrador; los filtros formales siguen para el 13-oct).

**Qué se produjo**
- `generar_cuaderno.py` → `Clase 36b - Mi Base - Abrir y Mirar - Clase.ipynb` (33 celdas). Fuente de verdad: editar el script y regenerar, no el `.ipynb`.
- `tools/datos_octubre/recortar_conaset_rm.py` → `datos-compartidos/07_conaset/CONASET_siniestros-transito-RM_2020-2025.csv` (123.343 de 436.521 filas, 36 columnas, 45,5 MB).
- `clases-octubre/seguimiento/revision/Clase 36b - Referencia Docente.md` (ignorado por git): guion minuto a minuto, demo, torpedo oral con respuestas, ficha de cada base y notas por equipo.

**Hallazgos al verificar las bases (corregidos en `datos-compartidos/README.md`)**
- Matrícula es UTF-8: el README decía `latin-1`, que rompe los nombres (`CAMIÃ‘A`). No lleva parámetros.
- SIMCE por comuna **sí** necesita `sep=";"` + `encoding="latin-1"`; el README decía que abría sin parámetros.
- Solo DEMRE (`sep`), SIMCE (`sep` + `latin-1`) y Hospitalarias (`header=2`) necesitan algo extra.
- Datos que pandas no cuenta como vacíos: `s/i` en SIES (555), celdas de solo espacios en CONASET (`Ruta`, `Calle_Dos`, `Calle_Uno`), textos con espacios al final en Matrícula. Material para N°37.

**Verificación**
- Ejecución completa con celdas vacías: sin errores.
- Pasos 1-4 rellenados y ejecutados en CONASET RM (`(123343, 36)`), Hospitalarias con `header=2` (`(14639, 20)`) y SIMCE por establecimiento con `sep` + `latin-1` (`(3002, 42)`).
- Los 9 links se corresponden con archivos reales de `datos-compartidos/`.
- Sin `$` sin escapar, sin soluciones, sin menciones a la modalidad de trabajo, sin outputs guardados.

**Pendiente**
- El cuaderno dice "avísale al profe" para quien no está inscrito porque el link del Form no está en el repo.
- Sin Ejercicios, PPT ni Ticket de Salida: no corresponde a una clase de aplicación.
