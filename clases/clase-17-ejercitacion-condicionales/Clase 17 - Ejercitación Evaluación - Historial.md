# Historial — Clase 17 - Ejercitación Evaluación

## 2026-07-13 — Creación

**Motivo:** al preparar el temario de la Evaluación Individual de Condicionales (2026-07-21), se detectó que ninguna clase del curso (8a, 8b, 8c, 9/11, 13, 14, 17) practica leer código ya escrito — todos los ejercicios existentes son "escribe el programa completo desde una narrativa". El diagnóstico de medio semestre (`evaluacion_compu_solucionario.docx`, rendido 2026-07-13) sí evalúa 100% en formato de predicción de output / identificación de errores, lo que confirmó el hueco.

**Decisión de alcance:** se descartó un colab separado enfocado en "predecir sin ejecutar" — en computador el estudiante simplemente correría el código, así que ese formato de papel no aplica. Se mantiene el foco en construir programas (la habilidad que realmente se evalúa), agregando solo una sección corta de calentamiento con código real que se ejecuta (no se adivina).

**Estructura aprobada:**
- **Sección 1 — Calentamiento rápido** (variables ya definidas, el estudiante escribe solo la línea que falta o corrige el bug):
  - 1A — Arma la condición (5 ítems, Bloque 2: `and` simple, `or` simple, `var1 and (var2 or var3)`, `(var1 and var2) or var3`, `not(var1) and (var2 and var3)`)
  - 1B — Arregla el bug (5 ítems, uno por bloque: 3 caso límite, 1 `=`/`==`, 4 falta `:`, 5 indentación anidada, 6 `elif` mal ordenado)
  - Ambas subsecciones con **autocheck**: una función `verificar_<id>(valor)` por ítem (ej. `verificar_1A_1`), todas definidas en una única celda de configuración ubicada al inicio del documento (antes de la Sección 1). Esa celda usa `#@title` + `cellView: form` de Colab, por lo que aparece colapsada tras un título ("🔧 Configuración automática") en vez de mostrar el código — sutil sin dejar de ejecutarse. Cada ítem llama a su función al final de su propia celda, así el estudiante ve el resultado ("✅ ¡Muy bien!" o el error) de inmediato al ejecutar, sin tener que buscar nada al final del documento.
- **Sección 2 — Programas completos** (Bloque 7, criterio de selección): 4 ejercicios narrativos nuevos (kiosco escolar, taller de teatro, torneo de ajedrez, transporte compartido a concierto), contextos sin repetir los de Clase 17 original ni de clases previas.
- **1A — línea en blanco:** en vez de un comentario genérico ("Escribe aquí tu línea"), la celda deja directamente `nombre_variable = ` con el `=` ya escrito, para que el estudiante complete solo la expresión del lado derecho.
- **Práctica Guiada** (descuentos por compra, patrón `elif` con `if` anidado): recuperada tal cual de la Clase 17 original y agregada al inicio del documento (después de las Instrucciones, antes de la Sección 1) — sin solución visible para el estudiante, igual que en el original. La solución de referencia se agregó al Solucionario.

**Décimas:** +6 en total — +1 en bloque para la Sección 1 (los 10 ítems deben mostrar "✅ ¡Muy bien!"; se verifica visualmente al recibir en Classroom, sin código anti-copia) + 5 en la Sección 2 (+1/+1/+1/+2, mismo esquema que la Clase 17 original). Son décimas independientes de las +5 ya otorgadas en la Clase 17 original — no se suman entre sí.

**Archivo original archivado:** `Clase 17 - Ejercitación Condicionales - Clase.ipynb` y su Solucionario se movieron a `old/` sin modificarse. `Clase 17 - Ejercitación Evaluación` pasa a ser el material vigente de la carpeta.

**Generación:** ambos notebooks (`Clase 17 - Ejercitación Evaluación - Clase.ipynb` y `- Solucionario.ipynb`) se generan con `generar_v2.py` (fuente de verdad — no editar los `.ipynb` a mano, regenerar el script si hay que cambiar algo).
