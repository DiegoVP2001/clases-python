# Clase 43 v2 — La neurona aprende sola · Historial

## 2026-11-10 — Diseño y generación

- **Origen:** reformulación del calendario v6. La v1 (`Clase 43 - Neurona - *`, ajuste manual de pesos) queda archivada sin dictar. La v2 usa los **mismos datos del wifi de la 42b ya cargados** y la misma receta del árbol; solo cambia la línea que crea el modelo.
- **Decisiones de Diego:** mostrar los pesos (`coefs_`, `intercepts_`) y reiterar `random_state`; no usar `lbfgs`; `import` siempre en la primera celda ejecutada primero (regla desde hoy para todos los cuadernos y pruebas); **actitud: Sorpresa** («lo que está a la frontera del conocimiento»); alinear la guiada con la Prueba 1.
- **Verificado (scikit-learn 1.9.1):** árbol 1,0 (4/4); neurona 0,75 (3/4, falla la fila 18); semillas 0–4: test 0,75 ×4 y 0,5 (semilla 4); train 0,875 / 0,75 / 0,875 / 0,875 / 0,5.
- **Generado** con `generar_clase_v2.py`, `construir_slides.py` y `crear_ticket_ppt_v2.py`: `Clase.ipynb` (47 celdas), `Solucionario.ipynb` (ejecutado de punta a punta con nbclient; todos los `check_*()` dan ✅), `Ticket de Salida Respuestas.json` (B, D, A), `Ticket de Salida.pptx` (8 slides, solo local), Guía Docente Voz y slides animadas en `sitio-hub/clase-43-v2/` (8 slides; probadas contra un DOM simulado).
- **Verificadores probados con errores típicos:** sin modelo, neurona con otros argumentos, predicciones del `train` en vez del `test`.
- **Decisión de diseño:** `check_icn()` (concepto 3) no exige el árbol; `check_comparar()` (concepto 5) sí. Guiada = único obligatorio; extras 0a (fila nueva), 1 (otras columnas: árbol 0,25 y neurona 0,25) y 2 (desafío de semillas).
- Pendiente: gate (Diego), commit con pathspec, push (sin el `.pptx`), deploy del hub y link de Colab.

## 2026-11-10 (2.ª ronda) — Ajustes de Diego (aplicados)

- **Haz Ahora, pregunta 1:** ahora es de **ponderación** de las 3 columnas (nota de 0 a 10 a cada una, con justificación). La slide 1 trae deslizadores.
- **Diagramas en el concepto 2:** la neurona (datos × peso → suma → nivel de activación → decisión) y la curva del **nivel de activación** (umbral 0,5, filas 17–20), con los pesos reales de `random_state=0`; generados con `diagramas/construir_diagramas.py` e incrustados en el Colab. En las slides: la 3 anima el diagrama paso a paso y la nueva 4 muestra la curva (ahora son 9 slides).
- **`hidden_layer_sizes=()`:** el desplegable pasó del concepto 2 a **justo debajo del bloque de código del concepto 3**.

## 2026-11-10 — Cierre de etapa

- Gate aprobado por Diego (Colab, Solucionario, Guía del colega, diagramas y slides animadas). Commit + push de la carpeta (sin los `Ticket de Salida.pptx`, que se suben después de dictar la clase) y de `sitio-hub/`; deploy del hub a Vercel.
