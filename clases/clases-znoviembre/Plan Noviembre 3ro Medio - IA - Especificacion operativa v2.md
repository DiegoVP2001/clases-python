# Plan noviembre 2026 · 3.º medio · Inteligencia artificial

**Versión 2 · Especificación operativa para Claude Code · Actualizada el 31 de octubre de 2026**

## 1. Propósito, fuentes y estado

Este documento organiza el bloque de noviembre y especifica qué deberá construir un agente que prepara las clases. El docente trabaja principalmente con Claude Code. La prioridad es comprender la IA mediante experiencias aplicadas, programar elementos esenciales y explicar los resultados con criterio.

**Alcance de esta entrega:** únicamente este Markdown. HTML, Colabs, controles, rúbricas y solucionarios se describen como trabajo futuro; no se generan en esta etapa. Conservar el archivo original y crear versiones nuevas de los materiales.

Fuentes disponibles: solicitud actual y conversación «Plan De Evaluación Noviembre», recuperada mediante su identificador `6ae60cbf-1304-83e9-92c7-23316b97e848`. Las decisiones explícitas más recientes del docente prevalecen sobre propuestas anteriores.

**Limitación de procedencia:** el archivo «Plan Noviembre 3ro Medio - IA - Contexto completo para asesoría.md» no estuvo accesible en esta sesión. Esta versión conserva el contexto recuperable de la conversación y de la solicitud, pero no acredita una comparación íntegra con el original. Cuando esté disponible, incorporar antecedentes relevantes que falten sin reabrir las decisiones cerradas de este documento. No inventar características del establecimiento, cantidad de estudiantes, horarios, políticas, materiales existentes ni definiciones del marco 4D.

## 2. Contexto pedagógico y decisiones cerradas

- Curso: 3.º medio. Bloque: noviembre de 2026, del lunes 2 al jueves 26.
- **11 sesiones efectivas**, incluidas las tres evaluaciones. El martes 17 no hay clase por ausencia docente y no se asigna una sesión sustitutiva obligatoria.
- Alta inasistencia: cada actividad debe tener una entrada autónoma y permitir incorporarse sin haber completado el archivo de la clase anterior.
- Trabajo y evidencia individuales. La conversación colectiva y el apoyo entre compañeros no reemplazan la producción verificable de cada estudiante.
- La conversación recuperada señala experiencia limitada con listas y ausencia de dominio de pandas. Usar Python simple, listas y andamiaje; no introducir pandas como requisito.
- Primera sesión: diagnóstico oral, ejemplos prácticos, panorama de todo el bloque y HTML interactivo de mapa de IA + pipeline, con ticket de salida desbloqueado por contraseña.
- Desde el 3 de noviembre: Colabs de aplicación. Los estudiantes escriben, ejecutan y modifican código significativo, incluso si el modelo está simplificado. No basta ejecutar todo sin tomar decisiones.
- Priorizar dos experiencias conectadas: programar el cálculo de una neurona el 5 y entrenar una red con `MLPClassifier` el 9. Enseñar `accuracy` dentro de esta segunda experiencia.
- Sin clase especial de clasificación multiclase ni matriz de confusión. Mantener clasificación binaria para reducir carga.
- Mini-LLM el 10: se evalúa en **E2**, aunque se enseñe antes de E1.
- E1 y E2 al inicio de sus sesiones, seguidas de revisión general y avance introductorio. E3 también al inicio, con cierre posterior.
- Dos notas sumativas: promedio simple de las **calificaciones** de E1 y E2, y calificación de E3.

## 3. Calendario maestro

Cada fila fija un objetivo, los contenidos nuevos imprescindibles y una evidencia observable. Es una especificación general, sin guiones minuto a minuto ni actividades completas.

| Sesión y fecha | Objetivo | Contenidos nuevos esenciales | Aplicación y producto verificable individual |
|---|---|---|---|
| **1 · Lun 2 nov** — Mapa IA + pipeline | Reconocer usos de IA, distinguir conceptos básicos y explicar el recorrido desde datos hasta evaluación; conocer el bloque completo. | IA, ML, DL e IA generativa; reglas frente a aprendizaje; datos, variables, etiquetas, entrenamiento, prueba, predicción y evaluación a nivel panorámico. | HTML: ubicar ejemplos en el mapa, ordenar el pipeline y resolver ticket desbloqueado al cierre. Evidencia exportable o copiable con respuestas; diagnóstico oral inicial sin nota sumativa. |
| **2 · Mar 3 nov** — Primer clasificador ML | Entrenar un clasificador binario y usarlo con entradas nuevas. | Entradas y etiquetas en listas; `fit()` como entrenamiento y `predict()` como predicción. | Colab con datos pequeños simulados, entrenamiento y al menos tres predicciones nuevas; modificar una entrada y explicar un resultado. No exigir todavía el cálculo autónomo de `accuracy`. |
| **3 · Jue 5 nov** — Construir una neurona | Explicar cómo entradas, pesos y sesgo producen una salida. | Suma ponderada, sesgo y activación simple; idea de error y ajuste de pesos. | Colab: escribir el cálculo de una neurona, cambiar pesos y comparar salidas; explicar qué cambió. Ajuste manual exploratorio, sin implementar retropropagación. |
| **4 · Lun 9 nov** — Entrenar red y medir aciertos | Entrenar una red sencilla y evaluar sus predicciones con datos separados. | `MLPClassifier`; separación entrenamiento/prueba; aprendizaje como ajuste de pesos; `accuracy` = aciertos / total evaluado. | Colab con `fit()`, `predict()`, cálculo de `accuracy` sobre prueba y comparación de un cambio controlado. Explicar un error y por qué ese resultado no garantiza desempeño futuro. |
| **5 · Mar 10 nov** — Mini-LLM | Explorar generación probabilística de texto y reconocer los límites de una demostración. | Tokens, siguiente token, probabilidades y errores de generación; relación con respuestas plausibles pero incorrectas. | Colab con generador de juguete: completar fragmentos breves, modificar corpus o una opción de generación y comparar resultados. Explicar una limitación. Contenido de E2. |
| **6 · Jue 12 nov** — E1, 45 min | Demostrar comprensión de fundamentos de IA/ML y redes neuronales. | Durante el control, ningún contenido nuevo. Después: introducción a instrucciones claras para un asistente. | Control individual en Colab con interpretación y código acotado. Después de entregar: revisión de errores frecuentes y primer bosquejo de prompt, sin incorporarlo a la nota E1. |
| **7 · Lun 16 nov** — Prompting con ChatGPT | Formular, probar y mejorar instrucciones y evaluar la respuesta obtenida. | Rol cuando aporte, tarea, contexto, formato, restricciones; iteración y verificación. | Colab de registro con prompt inicial, respuesta real, mejora, nueva respuesta y juicio justificado; conversación real con ChatGPT si se cumplen las condiciones de acceso. Pequeña operación en Python para organizar o comparar evidencia, sin convertir longitud en indicador de calidad. |
| **Mar 17 nov · Sin clase** | Ausencia docente. | — | No cuenta como sesión efectiva ni requiere avance obligatorio para el 19. |
| **8 · Jue 19 nov** — E2, 45 min | Explicar el mini-LLM y usar ChatGPT con prompting y criterio crítico. | Durante el control, ningún contenido nuevo. Después: introducción a un dilema ético. | Control individual: conversación real, iteraciones, análisis y enlace compartido revisado; registro en Colab de la evidencia requerida. Después de entregar: revisión general e introducción a ética. Aplicar la contingencia de acceso descrita abajo cuando corresponda. |
| **9 · Lun 23 nov** — Ética y 4D | Justificar una decisión sobre uso de IA mediante el marco 4D del curso. | Privacidad, sesgos, responsabilidad y aplicación de las 4D; denominaciones y definiciones exactas pendientes de cotejo con el original. | Colab: caso con datos ficticios y código simple para observar una consecuencia; decisión individual argumentada con las 4D y evidencia del caso. No exige entrenar un modelo nuevo. |
| **10 · Mar 24 nov** — Integración | Conectar funcionamiento, evaluación y uso responsable de IA. | Sin ampliar el temario; consolidación de relaciones y errores frecuentes. | Colab autocontenido de práctica sin nota: completar o modificar código, interpretar desempeño, mejorar un prompt y justificar una decisión ética. Respuestas y ejecución guardadas. |
| **11 · Jue 26 nov** — E3, 60–65 min | Integrar fundamentos técnicos, uso crítico y ética. | Ningún contenido nuevo durante la evaluación. | Evaluación individual en Colab: código breve, interpretación, análisis de prompting y decisión con 4D. Evidencia entregada y cierre del bloque. |

## 4. Primera clase: requisitos destacados

La clase del lunes 2 debe orientar y activar la participación. No comenzar con una exposición extensa de definiciones. El mapa y el pipeline se comprenden mediante ejemplos y manipulación, sin anticipar la matemática de redes.

### Recorrido obligatorio

1. **Escuchar lo que saben y han escuchado.** Preguntar oralmente: «¿Dónde han escuchado hablar de IA?», «¿Qué creen que hace?», «¿Qué han probado?», «¿Cómo creen que aprende?» y «¿Qué dudas o riesgos les genera?». Permitir respuestas tentativas; registrar ideas iniciales y confusiones para retomarlas al cierre. No solicitar relatos personales sensibles ni hacer de la experiencia previa una ventaja evaluativa.
2. **Mostrar muchos ejemplos breves y concretos.** Incluir, por ejemplo, recomendaciones de música, filtro de spam, reconocimiento de imágenes, predicción de riego con datos ficticios, traducción y generación de texto o imágenes. Agregar un sistema de reglas como contraste y un caso dudoso para conversar. Aclarar qué recibe cada sistema y qué produce; no afirmar que un producto usa una técnica específica sin evidencia. Los ejemplos son propuestas para construir el material.
3. **Presentar el recorrido de todo noviembre.** Mostrar el calendario resumido: ubicar IA → entrenar clasificador → construir neurona → entrenar red y medir aciertos → generar texto → usar ChatGPT → analizar ética → integrar. Explicar qué harán personalmente, cuándo se evalúa y cómo se forman las dos notas.
4. **Construir el mapa interactivo.** Mover bloques de conceptos y ejemplos, comprobar, recibir retroalimentación y corregir. Usar la relación IA ⊃ ML ⊃ DL. Presentar IA generativa como categoría por lo que produce, relacionada con esas técnicas; ChatGPT sirve como ejemplo de generación basada en aprendizaje profundo. No enseñar como ley universal la cadena IA ⊃ ML ⊃ DL ⊃ IA generativa.
5. **Ordenar y aplicar el pipeline.** Con un mismo caso sencillo: definir problema → reunir/preparar datos e identificar variables y etiquetas → separar entrenamiento/prueba → entrenar → predecir sobre prueba → evaluar → usar en casos nuevos y revisar. Distinguir entrenar de predecir y conservar el conjunto de prueba fuera del entrenamiento. Es una primera vista; la implementación se retoma en los Colabs.
6. **Cerrar y comprobar comprensión.** Volver a alguna idea del diagnóstico, pedir una explicación breve y anticipar el clasificador del día siguiente. Entregar la contraseña del ticket al cierre. El ticket debe comprobar una relación del mapa, una decisión del pipeline y una aplicación o duda. Su función es formativa y no añade una tercera nota.

### Condiciones del HTML que se construirá después

- Un único archivo HTML autocontenido, con CSS y JavaScript incluidos, que funcione sin cuenta y sin conexión una vez descargado; evitar servicios externos, rastreadores y bibliotecas remotas.
- Incluir orientación del bloque, mapa, pipeline y ticket dentro del mismo archivo, con instrucciones cortas y progreso visible.
- Permitir arrastrar bloques y también seleccionar/ubicar mediante botones o teclado. No depender solo del color; cuidar legibilidad y contraste.
- Retroalimentación explicativa y posibilidad de reintento en actividades formativas. Separar claramente actividad de práctica y ticket.
- Ticket bloqueado hasta introducir una contraseña configurable por el docente. **La contraseña en HTML/JavaScript controla el ritmo de clase; no ofrece seguridad real ni impide inspeccionar el archivo.** Nunca reutilizar una contraseña personal ni prometer protección de examen.
- Definir una salida que el estudiante pueda descargar o copiar y entregar por el canal institucional que se confirme. No afirmar que el HTML envía o registra respuestas automáticamente si no existe esa función.
- Minimizar identificación; preferir el código que indique el docente. Si se agrega guardado local, informar dónde se guarda, permitir reiniciar y advertir del uso de equipos compartidos.
- Criterio de aceptación: poder completar mapa y pipeline, corregir, desbloquear ticket con clave válida, conservar las respuestas al desbloquear y exportar/copiar evidencia. Verificar también clave incorrecta y uso sin arrastre.

## 5. Condiciones comunes de los Colabs

### Diseño para aprender y retomar

Cada cuaderno futuro debe incluir objetivo, requisitos mínimos, recapitulación breve, datos incluidos, instrucciones de ejecución, bloques «Escríbelo tú», experimentación y una conclusión individual. El estudiante debe poder comenzar sin archivos ni resultados privados de sesiones anteriores. Reutilizar un caso conocido es útil; depender de haberlo entregado antes no lo es.

Preparar importaciones y partes complejas para concentrar la escritura en conceptos nuevos. Conservar al menos una modificación significativa hecha por el estudiante y una explicación apoyada en la salida. En prompting y ética, el código puede servir para registrar, explorar o comparar evidencia; no forzar una nueva técnica de ML en esas sesiones.

Usar nombres claros en español, Python sencillo y datos pequeños, ficticios o debidamente anonimizados. Evitar descargas frágiles, grandes entrenamientos, GPU, claves API y pagos obligatorios. No exigir pandas. Si se usan dependencias adicionales, explicitar instalación y comprobarla en un entorno limpio.

El cuaderno debe poder ejecutarse de arriba abajo desde una sesión nueva. Usar semillas cuando corresponda, dejar resultados comprensibles y explicar si la generación es aleatoria. Separar versión estudiante y solución docente cuando se autorice producirlas; no dejar respuestas evaluativas ocultas dentro de la copia del estudiante.

### Precisión de los conceptos

- El 5 se programa el cálculo de una neurona y se exploran pesos manualmente. Eso no equivale a implementar el entrenamiento de una red.
- El 9 la biblioteca ajusta pesos al entrenar. Preparar lo necesario para escalar entradas si el caso lo requiere, sin convertirlo en un nuevo eje del temario ni usar prueba para ajustar el preprocesamiento.
- Calcular `accuracy` en prueba; mostrar aciertos y total además del valor. No confundirla con certeza individual, comprensión o garantía de confiabilidad. No seleccionar cambios sucesivos usando prueba como si fuera entrenamiento.
- Un resultado menor no debe penalizar por sí mismo una ejecución técnicamente correcta y bien interpretada. Evitar conjuntos que den aciertos perfectos triviales o que hagan imposible una partición útil.
- «Mini-LLM» es un nombre didáctico para un generador de juguete. Especificar qué implementa realmente: no presentar un generador por frecuencias o transiciones como un transformer o un LLM entrenado a escala. No simular respuestas como si provinieran de ChatGPT.

### Evidencia y contingencias

Definir en cada cuaderno qué celdas se completan y qué archivo o enlace se entrega. No asumir que guardar en Drive equivale a entregar al docente. El canal institucional está pendiente de confirmación.

Ofrecer una recapitulación y datos iniciales listos para quienes faltaron. Los apoyos pueden reducir la carga de sintaxis sin eliminar el objetivo. Ante fallas técnicas, conservar evidencia y aplicar la recuperación acordada por el docente; no convertir automáticamente una falla de acceso o una ausencia en una calificación mínima.

## 6. Evaluación: tres instrumentos, dos notas

| Instrumento | Alcance cerrado | Evidencia central | Tiempo |
|---|---|---|---|
| **E1 · 12 nov** | Mapa IA, pipeline, clasificación, `fit/predict`, neurona, pesos, entrenamiento de red y `accuracy`. **No incluye mini-LLM ni prompting.** | Respuestas breves de aplicación, lectura/modificación acotada de código y explicación de predicciones y aciertos. | 45 min |
| **E2 · 19 nov** | Mini-LLM, tokens, probabilidades, limitaciones, ChatGPT, prompting, iteración y criterio. No exigir el marco 4D antes de enseñarlo. | Conversación real iniciada para la actividad, enlace compartido revisado, iteraciones y análisis individual; preguntas sobre el generador de juguete. | 45 min |
| **E3 · 26 nov** | Integración de los contenidos efectivamente enseñados, incluidas ética y 4D. | Código esencial, interpretación de resultados y decisión justificada. Evitar depender exclusivamente de acceso en vivo a ChatGPT; puede analizar evidencia provista. | 60–65 min |

**Cálculo de notas:**

`Nota sumativa 1 = (calificación E1 + calificación E2) / 2`

`Nota sumativa 2 = calificación E3`

Convertir cada instrumento a calificación antes de promediar E1 y E2; no sumar sus puntajes brutos si tienen máximos distintos. No incorporar ticket ni práctica del 24 a estas fórmulas. Escala, porcentaje de exigencia, redondeo y tratamiento de pendientes deben seguir la política del establecimiento, aún no disponible; el agente no los decide.

### Organización de los días evaluados

El control comienza después de instrucciones y preparación mínima, sin una clase nueva previa. Para E1 y E2, reservar 45 minutos efectivos; luego revisar errores generales o ejemplos análogos y avanzar a prompting el 12 y ética el 19. La conversación recuperada propuso un marco de 80 minutos (5 instrucciones + 45 control + 10 revisión + 20 introducción); usarlo como referencia de diseño y confirmar la duración real del bloque antes de cerrar materiales.

E3 dispone de 60–65 minutos efectivos y cierre posterior. Al ser la última sesión, no requiere introducir una clase siguiente. No reducir sus minutos para hacer caber contenido adicional.

No publicar solucionarios exactos mientras queden recuperaciones pendientes. La revisión inmediata puede trabajar conceptos y errores sin exponer respuestas del instrumento. Preparar recuperación equivalente en objetivos y dificultad, según las reglas del establecimiento.

### Requisitos de rúbricas y respuesta del corrector

Construir los instrumentos desde criterios observables y compartirlos antes de evaluar. Criterios mínimos: comprensión conceptual, aplicación/código cuando corresponda, interpretación de evidencia y justificación crítica. E2 debe valorar la mejora razonada del prompt y la revisión de la respuesta; E3 incorpora la decisión ética mediante el marco 4D confirmado.

Definir puntajes y descriptores antes de generar ítems; no inventar ponderaciones ya acordadas. Admitir soluciones distintas que satisfagan el objetivo y puntaje parcial por evidencia válida. No calificar por coincidencia literal con el solucionario, sofisticación del código, uso de una cuenta pagada ni extensión de las respuestas.

La respuesta del corrector, humano o asistido por IA, deberá contener por criterio: **evidencia observada → nivel/puntaje según descriptor → razón breve → mejora concreta**, seguida del total y la conversión autorizada. Si falta evidencia, indicarlo sin inventarla. Distinguir error conceptual, error de sintaxis y falla técnica. La IA puede apoyar la corrección, pero el docente revisa y decide la calificación; no subir trabajos identificables a servicios externos sin autorización aplicable.

## 7. ChatGPT: edad, permisos, privacidad y acceso

### Antes de la práctica del 16 y de E2

No deducir edad ni autorización por estar en 3.º medio. Verificar con el docente las edades, el consentimiento requerido, la autorización institucional, las reglas de tratamiento de datos, disponibilidad de cuentas y acceso a enlaces. El agente no debe crear cuentas, aceptar condiciones, publicar conversaciones ni compartir credenciales por iniciativa propia.

La orientación oficial consultada el 31 de octubre de 2026 indica que ChatGPT no está destinado a menores de 13 años y requiere consentimiento parental para usuarios menores de 18 en el tramo señalado por su guía educativa. Verificar también los términos vigentes y requisitos locales antes de la actividad; la autorización escolar no sustituye automáticamente el consentimiento requerido. La guía advierte que las respuestas pueden ser inadecuadas para algunas edades. [Fuente oficial: uso de ChatGPT y edades](https://help.openai.com/en/articles/8313401-is-chatgpt-safe-for-all-ages).

Usar situaciones ficticias y adecuadas para la edad. No introducir nombres completos de compañeros, datos de salud, información familiar, contraseñas, fotografías identificables ni antecedentes escolares sensibles. No pedir a estudiantes que revelen conversaciones personales ni usar una cuenta compartida como solución improvisada.

### Conversación real y enlace de E2

La ruta principal acordada es una conversación real individual con ChatGPT y enlace compartido. Crear una conversación nueva dedicada a la evaluación, conservar las iteraciones y revisar el contenido y la audiencia antes de compartir. Entregar el enlace únicamente por el canal confirmado.

Un enlace de cuenta personal puede ser visto por cualquiera que lo tenga; los espacios administrados tienen restricciones propias. Archivos o imágenes pueden aparecer en el contenido compartido. Comprobar que el enlace muestre las iteraciones necesarias y que el docente pueda abrirlo; no compartir solo la última respuesta por error. No prometer que el enlace es privado, permanente o accesible desde cualquier cuenta. [Fuente oficial: compartir conversaciones](https://help.openai.com/en/articles/7925741-sharing-conversations-and-scheduled-tasks-in-chatgpt).

### Si faltan permisos o falla el servicio

Confirmar antes de E2 una contingencia con el docente: actividad individual equivalente con conversación real previamente obtenida y anonimizada por el docente, análisis de iteraciones y rediseño de prompts, o recuperación supervisada cuando el acceso esté habilitado. Esta ruta debe conservar los criterios que sí permite observar y no atribuir al estudiante una interacción que no realizó. Si se debe evaluar interacción en vivo, queda pendiente esa evidencia para recuperación.

No cambiar silenciosamente la modalidad principal, exigir pagos ni eludir restricciones de edad o del establecimiento. Dejar registrada la contingencia, la evidencia disponible y lo que requiere revisión docente.

## 8. Instrucciones de operación para Claude Code

1. Leer este documento y los materiales existentes que entregue el docente. Si aparece el original, cotejarlo y conservar sus antecedentes útiles; registrar diferencias sin sobrescribirlo.
2. Mantener calendario, alcance de E1/E2/E3, dos notas y enfoque aplicado. Las propuestas descartadas de la conversación no son tareas pendientes.
3. Resolver decisiones rutinarias de implementación dentro del encargo. Preguntar solo por información que cambie evaluación, acceso, seguridad o fidelidad al curso; avanzar en lo independiente mientras se resuelve.
4. Cuando el docente encargue producir materiales, trabajar por prioridad y dependencias del checklist. No interpretar este Markdown como una orden de generar ahora todos los archivos.
5. En cada entrega futura, informar material listo, objetivo cubierto, comprobación realizada y pendiente concreto. No afirmar que se probó en Colab, que se publicó o que se registraron respuestas si no ocurrió.
6. Mantener versiones del estudiante sin respuestas evaluativas y materiales docentes separados. No publicar, distribuir, conectar servicios ni procesar datos reales sin la autorización correspondiente.
7. Pedir o recuperar las denominaciones y definiciones exactas de **4D**. No elegir un marco homónimo ni redactar su rúbrica específica como si estuviera confirmado.

## 9. Checklist priorizado de producción futura

Las casillas son tareas pendientes; esta entrega no las declara realizadas. El orden prioriza la clase inmediata y la alineación evaluativa. Los entregables indicados se crearán solo en etapas posteriores.

| ID / prioridad | Tarea concreta | Depende de | Criterio de listo / entregable futuro |
|---|---|---|---|
| **A · P0** | Cotejar el original cuando se adjunte; recuperar duración real, materiales previos y marco 4D. | Disponibilidad del original/docente. | Antecedentes incorporados con procedencia; sin cambiar acuerdos cerrados. No bloquea el esquema del HTML ni los primeros Colabs. |
| **B · P0** | Confirmar canal de entrega, acceso a Colab, política de notas y recuperación; verificar edades, permisos y acceso a ChatGPT. | Información institucional/docente. | Condiciones registradas; contingencia de E2 definida antes del 16. Bloquea uso real y publicación, no la preparación con datos ficticios. |
| **C · P0** | Preparar primero el HTML del 2 y una orientación docente breve. | Este documento; canal para cerrar entrega de evidencia. | Diagnóstico, ejemplos, panorama completo, mapa correcto, pipeline, cierre y ticket; funcionamiento local y exportación/copia comprobados. |
| **D · P0** | Alinear E1 y E2: criterios, evidencia, puntajes y conversión. | Alcances de §6; política de B para conversión. | Matriz breve de criterios que guía Colabs y controles, sin incorporar mini-LLM a E1. |
| **E · P1** | Construir Colabs del 3, 5 y 9 en ese orden. | Criterios D; cada cuaderno incluye su propio inicio. | Clasificador, neurona y red con `accuracy`; ejecución limpia y modificación significativa del estudiante. |
| **F · P1** | Construir mini-LLM del 10 y E1 del 12 con solución/rúbrica docente. | E y D. | Generador descrito con precisión; E1 resoluble en 45 min y separado de su solucionario; revisión y avance posterior previstos. |
| **G · P1** | Preparar Colab del 16 y E2 del 19 con rúbrica y contingencia. | F, D y condiciones de B. | Práctica real, iteración, criterio, registro y enlace comprobable; sin depender de cuenta pagada. |
| **H · P2** | Construir ética del 23 y práctica integradora del 24. | Definiciones 4D de A y contenidos previos. | Caso ficticio, aplicación individual y práctica sin nota; no agrega temario antes de E3. |
| **I · P2** | Construir E3, solución y rúbrica. | H; criterios y política de evaluación. | Integración de lo enseñado, duración 60–65 min y corrección por evidencia; alternativa a fallas técnicas. |
| **J · Transversal** | Revisar cada material antes de entregarlo. | Material correspondiente. | Acceso, ejecución, claridad, accesibilidad, privacidad, producto verificable y separación de respuestas comprobados; fallos pendientes declarados. |

### Datos pendientes que no deben rellenarse por inferencia

- Archivo original y sus antecedentes no recuperados.
- Definición, denominaciones y ejemplos del marco 4D utilizado por el docente.
- Duración efectiva de los bloques, cantidad de estudiantes y equipamiento disponible.
- Canal y permisos de entrega; mecanismo concreto para recibir el ticket.
- Escala de notas, exigencia, redondeo y recuperación por ausencias.
- Edades, consentimientos, autorización institucional y condiciones reales de cuentas/enlaces de ChatGPT.

La preparación de la primera clase y de los Colabs técnicos puede avanzar con lo definido. La interacción real con ChatGPT, el cierre de las rúbricas 4D y la conversión de puntajes requieren resolver sus datos específicos antes de aplicarse.
