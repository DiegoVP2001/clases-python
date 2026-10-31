# Historial — Clase 41 · Mapa de la IA + pipeline

## 2026-10-31 — Spec aprobada (v2)

- Fuente: `clases-znoviembre/Plan Noviembre 3ro Medio - IA - Especificacion operativa v3.md` (v2 de ChatGPT + sección 10 de integración).
- Flujo liviano: Colab guía + HTML interactivo + guía de la voz. Sin PPT, sin Ejercicios.ipynb, sin Ticket por Form.
- **Actitud:** Curiosidad (elegida por Diego). **Sin 4D** en esta clase (pasan a la clase de ética, 23-nov).
- **Sin sección «Propósito»; «¿Para qué sirve?» pasa a «¿Por qué lo veremos?»** (regla nueva para todas las clases).
- **Definiciones resumidas** a pedido de Diego: IA y ML; regla y patrón definidos aparte, fuera del diagrama.
- **Ticket:** 4 preguntas (C, A, B, D), solo en el HTML; descartado el PPT.
- **Dinámica:** el Colab dice «vamos a la actividad X de la página»; cada actividad (M1–M3, P1–P4, TK) se abre con un código de 3 números que entrega Diego.
- **Diagramas:** el mapa y el pipeline van como PNG (para proyectar y subir) y dentro del HTML (con pantalla completa).

## 2026-10-31 — Materiales generados (pendiente de aprobación de Diego)

- `Clase 41 - Mapa IA - Interactivo.html` (autocontenido; generado por `fuentes/construir.py`).
- `diagramas/Diagrama 1 - El mapa de la IA.png` y `Diagrama 2 - El pipeline.png` (1920×1080).
- `Clase 41 - Mapa IA - Clase.ipynb` (generado por `generar_clase.py`; 22 celdas).
- `Clase 41 - Mapa IA - Guía Docente Voz.md`.
- Copia para el hub en `sitio-hub/clase-41/` (todavía **sin desplegar**).

**Verificación hecha (Chrome, servidor local):** carga sin errores de consola; 8 actividades; código incorrecto no abre y el correcto sí; comprobación con respuestas malas y buenas en las 8 actividades; progreso 8 de 8; arrastrar y soltar con eventos reales en M2 y P1; ancho de 390 px sin desborde; formulario del código se oculta al abrir. **No verificado:** el Colab dentro de Google Colab (solo se auditó el JSON), ChatGPT Voice y el despliegue en Vercel.

**Correcciones durante la verificación:** (1) el formulario del código seguía visible tras abrir (CSS `display:flex` pisaba `hidden`); (2) la etiqueta «ML» del Diagrama 1 se montaba sobre el borde del círculo; (3) relleno sobrante en el encabezado fijo.

## 2026-10-31 — Cambios pedidos por Diego tras la primera revisión

- **Se quitó la sección «Cómo funciona»** del HTML.
- **El HTML pasa a 3 páginas:** M3 → P1 y P4 → ticket son cambios de página con código. Página 2 = **172** (abre también P1), página 3 = **725** (abre también el ticket). P2, P3 y P4 conservan sus códigos (884, 306, 591).
- **Diagrama 2 rediseñado:** set de entrenamiento («aquí la computadora aprende») separado del set de prueba («aquí vemos si es capaz de predecir»), con el modelo en medio.
- **Dos ejemplos:** explicación y PPT con el riego automatizado de una viña de Isla de Maipo (como Santa Ema); actividades y ticket con la climatización de las bodegas de fermentación. M1 y M2 también cambiaron los ítems de riego por ítems de la bodega (y M1 suma «riego que abre válvulas a las 7:00» como regla).
- **PPT paso a paso del pipeline:** `Clase 41 - Mapa IA - Presentación.pptx` (14 diapositivas con notas; imágenes generadas desde SVG por `fuentes/construir.py`).
- Colab y guía de voz actualizados (cambio de página en P1 y ticket; terminología de sets).
- Pendiente: aprobación de Diego, deploy en Vercel y push.

## 2026-10-31 — Aprobado y desplegado

- Diego aprobó los materiales y pidió el deploy.
- **Producción:** https://clases-ia-mario-bertero.vercel.app/ (portada) y https://clases-ia-mario-bertero.vercel.app/clase-41/ (interactivo). Verificado con `curl`: 200 en la portada, en `/clase-41/` y en los diagramas; el HTML en producción trae los códigos de página 172 y 725 y no trae «Cómo funciona».
- El Colab ya apunta a `https://clases-ia-mario-bertero.vercel.app/clase-41/` (no hizo falta regenerarlo).
- Efecto secundario revertido: `vercel link` conectó el repo de GitHub al proyecto; se desconectó con `vercel git disconnect`.
- **No pusheado a GitHub** (pendiente de autorización de Diego).

## 2026-10-31 — Cierre de etapa: subido a GitHub

- Commits `13cc600` (clase, hub, plan, traspaso, CLAUDE.md, Historial-Curricular) y `a9e2c86` (generadores sin «Propósito») en `master` de `DiegoVP2001/clases-python`.
- Verificado después del push: el sitio de Vercel sigue en producción (un solo deploy, no se creó otro) y el Colab responde desde GitHub.
- Link de Colab: https://colab.research.google.com/github/DiegoVP2001/clases-python/blob/master/clases/clase-41-mapa-ia-pipeline/Clase%2041%20-%20Mapa%20IA%20-%20Clase.ipynb
- `construir.py` ahora exporta las imágenes temporales a la carpeta temporal del sistema. Quedó una carpeta `fuentes/_slides/` bloqueada por permisos (ignorada por git).
