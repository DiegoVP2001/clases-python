# Plan Noviembre 3ro Medio — IA y Aplicaciones

> **Estado: idea registrada, sin diseñar.** Este documento es un memo para retomar cuando corresponda planificar noviembre en detalle — no reemplaza el flujo de `disenar-clase` ni fija fechas/estructura de 5 pasos. Fecha de registro: 2026-09-23.

> **Ver también (2026-10-22):** brainstorm ampliado y checklist de decisiones en `Plan Noviembre 3ro Medio - IA - Brainstorm y Checklist.md`.

## 1. Contexto y audiencia

- Desde la semana del **2 de noviembre**, 4to medio ya egresó. El curso queda solo con **3ro medio**.
- Tramo: **2 al 26 de noviembre**, ritmo lunes/martes/jueves de 80 min (a confirmar que se mantiene — ver `Plan Cierre 4to Medio y Continuidad 3ro - Agosto a Noviembre 2026.md` §7, riesgo 4).
- **Cambio de foco respecto al resto del año:** Python/Colab deja de ser el eje de la clase. El foco pasa a explorar IA (conceptual + impacto) y software para montar aplicaciones. Python se sigue usando, pero como apoyo cuando las herramientas o los conceptos lo demanden — no como el vehículo principal como en los Colabs regulares.
- Esta idea **reemplaza/reequilibra** lo que el `Plan Cierre...` §6 tenía asignado a noviembre (Picuino N°29–33, búsqueda y ordenación) — ver punto 5.

## 2. OAs restantes a cubrir

Referencia: `clases/OAs-referencia.md`.

| OA | Tema | Dónde encaja en este plan |
|---|---|---|
| OA4 | Aplicaciones y análisis (procesadores simbólicos, geometría dinámica, análisis estadístico) | Bloque E — software para montar aplicaciones |
| OA5 | Apps para dispositivos móviles / sensores | Bloque E — software para montar aplicaciones |
| OA6 | Uso responsable de TIC | Bloque D — impacto y consecuencias de la IA |
| OAk | Impacto de las TIC en contextos sociales/económicos/culturales | Bloque D — impacto y consecuencias de la IA |
| OA1 | Análisis de soluciones alternativas, abstracción | Bloque B — entrenar una mini red neuronal |

## 3. Bloques temáticos propuestos (sin fechas firmes)

### A. Cómo se entrena una IA (conceptual)

- Base: video de 3Blue1Brown **"Large Language Models explained briefly"** — https://www.youtube.com/watch?v=LPZh9BOjkQs
- **Antes de ver el video: explicar el concepto de token.** Es prerrequisito para que el video tenga sentido.
- Pendiente (retomar): elegir los conceptos más importantes del video para simplificar — candidatos a evaluar cuando se revise:
  - Tokens y tokenización
  - Predicción de la siguiente palabra / probabilidades
  - Parámetros y pesos de la red
  - Entrenamiento con grandes cantidades de datos (preentrenamiento)
  - Ajuste posterior (RLHF) a alto nivel
  - Idea intuitiva de "atención"/transformer, sin entrar en la matemática
- Pendiente: sacar capturas de pantalla de las partes esenciales del video (con timestamp) para usar en la presentación — el video es denso, así que la clase debe apoyarse en fragmentos elegidos, no mostrarlo completo.

### B. De la teoría a Python: mini red neuronal

- Objetivo: pasar de la teoría (bloque A) a algo concreto y ejecutable en Python, para inspirar y mostrar el potencial del lenguaje.
- Entrenar una red neuronal **muy simple** usando una librería (candidatos a evaluar: `scikit-learn` `MLPClassifier`, o Keras/TensorFlow si se quiere algo más visual) — nivel introductorio, no requiere que dominen la matemática detrás.
- Idea fuerte: usar como dataset de ejemplo la **base de datos de uno de los proyectos de los propios estudiantes** (del Proyecto OA4 de octubre) — a elegir por Diego. Refuerza que lo que construyeron antes sirve de insumo real.
- Posible extensión (a definir): que cada grupo entrene su propia red con su propio dataset.

### C. Frameworks y herramientas de IA

- Foco: qué herramientas existen, qué capacidades entregan, cómo usarlas con criterio — no solo teoría de entrenamiento.
- Marco de referencia sugerido: **4D de AI Fluency** (Delegación, Descripción, Discernimiento, Diligencia) — curso *AI Fluency for pK–12 educators* (Anthropic + Teach For America): https://academy.claude.com/courses/ai-fluency-for-k-12-educators

### D. Impacto y consecuencias de la IA

Casos reales para reflexionar sobre uso, impacto y consecuencias (privacidad, sesgo/daño social, trabajo humano invisible, mercado laboral):

- **Privacidad / vigilancia de conversaciones** — Project Lily, personas leyendo chats de ChatGPT: https://www.404media.co/inside-project-lily-the-humans-reading-your-chatgpt-chats/
- **Algoritmos y violencia real** — Facebook y la violencia contra los rohinyá en Myanmar: https://www.amnesty.org/es/latest/news/2022/09/myanmar-facebooks-systems-promoted-violence-against-rohingya-meta-owes-reparations-new-report/
- **Trabajo humano detrás de la IA** — BBC África (moderación de contenido): https://www.bbc.com/news/world-africa-67275219
- **Impacto en el mercado laboral** — investigación de Anthropic: https://www.anthropic.com/research/labor-market-impacts

### E. Software para montar aplicaciones (OA4/OA5)

- Pendiente: elegir qué herramientas usar (no definido aún).
- Python se usa como apoyo solo si la herramienta elegida lo demanda — no es el eje de este bloque.

## 4. Caminos de evaluación (por definir — notas independientes entre sí)

Ideas que surgieron y que se pueden separar en evaluaciones/notas independientes:

1. **Construir/entrenar su propia red neuronal simple** — proceso + explicación de qué hicieron (conecta con bloque B).
2. **Análisis de un caso de impacto de IA** — usando el marco 4D o preguntas guía sobre uno de los casos del bloque D (o uno propio).
3. **App/prototipo con el software del bloque E** — conecta con OA4/OA5.
4. Alternativa liviana sin nota: producto reflexivo (ej. guía de uso responsable de IA elaborada por el curso).

## 5. Relación con Picuino N°29–33 (búsqueda y ordenación)

El `Plan Cierre 4to Medio y Continuidad 3ro - Agosto a Noviembre 2026.md` §6 tenía noviembre completo asignado a terminar el Tutorial Picuino (búsqueda lineal/binaria, desplazamiento, ordenación por selección/inserción). Esta idea de IA + aplicaciones **no lo descarta del todo**, pero lo deja en pausa/opcional: prioridad a explorar otras cosas fuera de Python-Colab. Decisión pendiente: si Picuino 29–33 se hace parcialmente, se deja para diciembre (tramo bonus), o se descarta para este año.

## 6. Pendientes para retomar esta planificación

- [ ] Elegir las herramientas del bloque E (software para montar aplicaciones).
- [ ] Seleccionar los conceptos esenciales del video 3Blue1Brown + sacar las capturas con timestamp.
- [ ] Elegir qué base de datos de proyecto de estudiante se usa como ejemplo en el bloque B.
- [ ] Decidir qué pasa con Picuino N°29–33 (pausa, diciembre, o se descarta).
- [ ] Confirmar ritmo lunes/martes/jueves y feriados propios de noviembre (ver `Plan Cierre...` §7, riesgos 4 y 5).
- [ ] Definir cuáles de los caminos de evaluación de la sección 4 se usan, y si van con o sin nota.
- [ ] Una vez resuelto lo anterior, recién ahí pasar por el flujo formal (`disenar-clase` u otro) para las clases concretas.
