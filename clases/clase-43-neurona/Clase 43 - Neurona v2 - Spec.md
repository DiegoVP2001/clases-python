# Clase 43 v2 — La neurona aprende sola

**Estado:** Spec v2 aprobada por Diego (2026-11-10). La v1 (`Clase 43 - Neurona - *`) queda archivada sin dictar; no se toca.
**Clase Picuino:** N/A — fila de IA (calendario v6) · **Fecha:** mar 10-nov-2026 · **Curso:** 3ro medio · **Duración:** 80 min
**Flujo:** liviano (Spec → Colab + Solucionario + Guía Docente Voz + slides + Ticket al Form → gate → push de la carpeta; el `Ticket de Salida.pptx` NO se pushea antes de dictar).
**Modalidad:** no se menciona en ningún material; la anuncia Diego.

## Objetivo
Crear, entrenar y evaluar una neurona con la misma receta del árbol y comparar ambos resultados con sorpresa.

**OAs:** OA1, OA3. **Actitud: Sorpresa** (Diego, 2026-11-10): hoy tocamos la frontera del conocimiento, porque la pieza básica de las IA actuales es esta neurona. Se aterriza al abrir la caja (pesos que nadie escribió) y al ver que con otra semilla salen distintos.

## ¿Por qué lo veremos?
Las redes que reconocen voz o rostros están hechas de millones de estas neuronas que ponderan datos; hoy creamos una sola y vemos si le gana al árbol en los datos del wifi.

## Datos (idénticos a la 42b, ya cargados)
`clases/clase-42b-tabla-a-listas/datos_wifi_verificados.json`; columnas `dispositivos_conectados`, `estudiantes_viendo_video`, `horas_desde_reinicio`; etiqueta «¿se cayó el wifi?» (1 = sí). Filas 1–16 = *train*; 17–20 = *test* (`[0, 1, 1, 0]`). Las 4 listas vienen escritas; solo se ejecutan.

**Verificado (scikit-learn 1.9.1):** árbol `max_depth=3, random_state=0` → test 1.0 (4/4). Neurona `MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=0)` → predice `[0,0,1,0]`, test 0.75 (falla la fila 18), train 0.875, pesos `[-0.035, 0.376, 0.098]`, sesgo `-0.048`. Con `random_state=1`: test 0.75, train 0.75, pesos `[-0.001, 0.767, -0.099]`, sesgo `-0.559`. `solver="lbfgs"` NO se usa sin aprobación de Diego.

## Mapa de tiempos (80 min)
Bienvenida 5 (colega) · Haz Ahora 7 · Puente 3 · ICN 30 · Guiada obligatoria 20 (12 + 8 revisión) · Ticket 5 · Cierre 5. Extras sin tiempo.

## Estructura

### Haz Ahora (colega como encargado de informática, sin código)
«El problema tenía 6 columnas, pero el encargado pide estas 3.» Preguntas cerradas:
1. Ponderación: para saber si el wifi se cae no todas las columnas pesan igual; si le pusieras una importancia de 0 a 10 a cada una de las 3 columnas, ¿qué nota le pondrías a cada una y por qué?
2. Ayer el árbol acertó los 4 días de prueba: ¿qué porcentaje de aciertos es?
3. Con 4 filas de test, ¿cuántos puntos porcentuales vale cada fila?
4. Si un modelo tuviera 0,75 de precisión, ¿cuántas de las 4 filas acertó?

### Recordatorio puente
🔁 Ayer: el árbol aprendió solo una cadena de preguntas sí/no con las listas que tipeamos · 🔀 Hoy es distinto: mismos datos, otro modelo: una neurona que pondera cada columna (mini-tabla árbol/neurona) · ➡️ La próxima clase (lun 16): mini-LLM, cómo una IA predice la siguiente palabra.

### ICN «Escríbelo tú»
0. **🔧 Ejecuta esta celda primero:** imports `DecisionTreeClassifier`, `MLPClassifier`, `accuracy_score`. Regla: los `import` raros van SIEMPRE en la primera celda, ejecutada primero.
1. **Datos listos:** las 4 listas ya escritas, solo ejecutarlas (una línea: esto lo tipearon a mano en la 42b).
2. **¿Qué es una neurona?** Recibe las 3 columnas, pondera cada una (más o menos importancia), suma, calcula su **nivel de activación** (de 0 a 1; más de 0,5 → decide 1) y decide; los pesos los ajusta sola la computadora al entrenar. Lleva **dos diagramas**: la neurona (datos × peso → suma → activación → decisión) y la curva del nivel de activación con las 4 filas de prueba.
3. **La receta, cambiando una línea:** escriben la línea que crea la neurona (llamada idéntica a la Prueba 1) y siguen con `fit` → `predict` → `accuracy_score`. Idea clave: solo cambia la línea que crea el modelo. **Debajo del bloque de código va el `<details>`: `hidden_layer_sizes=()` = una sola neurona** (se decide por prueba y error; seguimos con una).
4. **Abrir la caja:** `modelo.coefs_` e `intercepts_` = los pesos que la computadora ajustó sola. Demo en vivo `random_state` 0 → 1 → 0; en las pruebas siempre `random_state=0`. Una línea: también pueden variar por otras razones técnicas que no veremos. No leer los pesos como verdad ni concluir qué columna «importa».
5. **Revisar y comparar:** 1. leer el resultado (predicciones vs. `etiquetas_test`; falla la fila 18) · 2. comparar la precisión (árbol 1.0 vs. neurona 0.75; con 4 filas cada fila vale 25 %). Pregunta «¿cuál usarían y por qué?».

Errores típicos: no ejecutar la celda de imports; cambiar `random_state` y creer que es otro modelo; leer los pesos como verdad absoluta; concluir con 4 filas de test.

### Práctica guiada (el único ejercicio obligatorio; alineada con la Prueba 1: B, C1, C3)
Con los datos listos, entrenar árbol y neurona, imprimir ambos accuracy con etiqueta y escribir 2 líneas: cuál usarían y por qué (con sus números) y por qué 4 filas de test dan poca seguridad. `check_guiada()`. Revisión con una pareja al frente.

### Extras (sin tiempo, con pistas y `check_*`)
0a predecir una fila nueva con la neurona (`[[...]]`) · 1 entrenar la neurona con otro trío (con una columna floja) y comparar · 2 desafío: probar `random_state` 0–4 y anotar si el accuracy cambia.

### Ticket de Salida (Form + PPT local)
Colab: solo link `https://forms.gle/sjRpbgmQzrpkEBsH9` y tema «La neurona aprende sola». 3 preguntas A–D con respuestas repartidas: (1) qué línea cambia entre árbol y neurona; (2) qué son `coefs_`; (3) 0,75 con 4 filas de test, qué se concluye.

### Cierre (a viva voz)
Comprensión 1–5; «¿Qué te sorprendió hoy de la neurona y por qué?»; anticipo mini-LLM.

## Colega (detalle en la Guía Docente Voz)
Solo habla cuando Diego la activa: bienvenida, Haz Ahora como encargado, verificación tras el concepto 4 («¿por qué cambian los pesos con otra semilla?»). Nunca protagonista en práctica ni cierre.

## Slides animadas — `sitio-hub/clase-43-v2/`
Haz Ahora (pregunta + 3 columnas) · una slide por concepto 1–5 (neurona con diagrama animado paso a paso y una slide aparte para el nivel de activación; abrir la caja con botón de semilla) · «Para pensar» (¿cuál usarían?) · resumen. Etiqueta «Concepto N del cuaderno». Generadas con `construir_slides.py` (modelo: 42b).
