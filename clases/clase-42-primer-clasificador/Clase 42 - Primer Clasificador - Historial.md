# Clase 42 — Primer clasificador · Historial

## 2026-11-03 — Spec aprobada (gate 1)

- Actitud elegida por Diego: **Pensamiento crítico**.
- Algoritmo: `DecisionTreeClassifier(max_depth=3, random_state=0)` + `export_text` (verificado con scikit-learn 1.9.1; árbol estable).
- Historia continua de Isla de Maipo: **la micro a Santiago** (La Islita). Reemplaza al riego de la viña en esta clase; la N°43 se decide en su spec.
- Solo Colab por ahora; el HTML `/clase-42/` se decide después de ver el Colab terminado.
- ICN con formato «Escríbelo tú» y dataset (16 filas) ya escrito en el Colab.
- **Feedback de Diego:** el objetivo queda solo como «entrenar un árbol de decisión con datos en listas y usarlo para predecir casos nuevos, con pensamiento crítico» (se quitó el «juzgando si cada predicción cuadra con los datos»). Dataset, casos nuevos, escenarios de la independiente, reparto de tiempos: aprobados sin cambios.
- Pendiente: confirmar OAs contra `OAs-referencia.md` al generar el Colab.

## 2026-11-03 — Colab, Solucionario y Guía Voz generados (a la espera del gate 2)

- `generar_clase.py` crea `Clase.ipynb` (58 celdas) y `Solucionario.ipynb`; los resultados esperados se calculan ejecutando las soluciones.
- **Verificado:** el Solucionario se ejecutó de arriba abajo con `py -3` sin errores; los 4 `check_*()` dan ✅ con la solución y ⚠️ con los 5 errores típicos probados (sin modelo, no es árbol, sin `fit`, otros datos, etiquetas/profundidad que no calzan); `check_ticket()` da 4/4 con C, A, D, B y ⚠️ con respuestas erróneas. `predict([0, 2, 12])` falla de verdad con `ValueError`.
- Árbol de la clase idéntico al de la spec. Datasets nuevos (verificados): Guiada = árbol de profundidad 1 sobre `minutos_espera` (ignora lluvia y taco; el día 3 con 9 km de taco queda «puntual»); Ej. 1 = lluvia → minutos de espera; Ej. 2 = minutos de atraso de salida; Ej. 3 = minutos de salida → cajas (ignora la lluvia: subir la lluvia no cambia nada, subir las cajas de 30 a 46 sí).
- **OAs propuestos:** OA1, OA3 | OAd (la spec decía OA1, OA6 | OAk; OA6 es ética digital y no se trabaja hoy). *Pendiente de confirmar por Diego.*
- Decisiones técnicas: los autochequeos buscan el árbol en la variable `modelo`; el ticket vive en el Colab con letras como huellas SHA-256 y justificación en base64 (ofuscación ligera, es práctica sin nota).
- Pendiente: gate 2 (Diego), commit con pathspec, push, actualizar checklist e `Historial-Curricular.md`, decidir el HTML.

## 2026-11-03 — Feedback de Diego sobre el Colab (aplicado)

- **Diagramita de un árbol de decisión** (`diagramas/construir_diagrama.py` → PNG incrustado) antes del concepto 1: preguntas sí/no, ramas, respuestas finales y un camino resaltado con un día nuevo. Es un árbol inventado (umbrales distintos al real) para no adelantar el hallazgo del concepto 4.
- **ICN acumulativo, patrón de la Clase 37:** cada concepto arranca con el código ya construido del anterior y el estudiante solo escribe la línea nueva (c1: datos → c2: + modelo → c3: + `fit` → c4: + `predict`; la celda «humano vs. voz vs. modelo» también arranca armada).
- **Estructura y emojis de la Clase 37:** `# 🐍` encabezado con curso/duración/plataforma, 🎯 Objetivo, 🔎 ¿Por qué lo veremos?, 1️⃣ Haz Ahora + «Mis respuestas», 2️⃣ ICN con `### 💡`, 📌 resumen, ⚠️ errores típicos (tabla Error | Qué ocurre | Cómo corregirlo), 3️⃣ Guiada, 4️⃣ Independiente con `#@title 🔧 Verificador automático` + 🎯 por ejercicio, 🎫 Ticket de Salida, 🎯 Cierre + 📝 Mis respuestas.
- Se quitó `check_guiada()` (la spec pedía autochequeo solo en Ej. 1–3).

## Siguiente

- Gate 2 → commit/push → decidir el HTML `/clase-42/` viendo el Colab.
