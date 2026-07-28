---
name: referencia-intereses-estudiantes
description: Usa esta skill para contextualizar clases, ejercicios, Google Colabs, tickets de salida y proyectos de programación a partir de los gustos declarados por estudiantes. Prioriza ejemplos significativos, cercanos y accionables para cursos que transitan desde programación en bloques hacia Python.
---

# Skill: Contextualización de programación según intereses de estudiantes

## 1. Propósito de la skill

Esta skill ayuda a un agente IA a diseñar materiales de programación más pertinentes, significativos y motivadores para estudiantes, usando como base sus intereses declarados.

Debe utilizarse para transformar contenidos de programación —especialmente en Python y Google Colab— en experiencias conectadas con gustos reales del curso, tales como videojuegos, música, deportes, redes sociales, tecnología, IA, salud, finanzas, estudio y automatización.

El objetivo no es "decorar" ejercicios con temas juveniles, sino usar esos intereses como contexto auténtico para formular problemas, variables, condiciones, funciones, listas, ciclos, entradas/salidas, simulaciones y proyectos.

El detalle exhaustivo de cada interés (qué aparece declarado, usos recomendados y bancos de ejemplos de ejercicios, además de ejemplos de código modelo) vive en `references/perfil-intereses.md`. Las plantillas completas de actividad de Google Colab por temática viven en `references/actividades-colab.md`. Este SKILL.md actúa como resumen navegable — el "Resumen rápido de intereses" y el "Banco de transformaciones rápidas" cubren la mayoría de los casos; abre las referencias cuando necesites más variedad de ejemplos para un interés específico o un template de actividad completo.

---

## 2. Cuándo usar esta skill

Usa esta skill cuando el usuario solicite cualquiera de las siguientes tareas:

- Diseñar una clase de programación.
- Crear un Google Colab para estudiantes.
- Transformar ejercicios abstractos en ejercicios contextualizados.
- Diseñar prácticas guiadas o independientes.
- Crear tickets de salida.
- Proponer proyectos finales o mini proyectos.
- Generar ejemplos de código significativos para estudiantes.
- Adaptar una clase de Python a intereses de estudiantes.
- Diseñar actividades después de una unidad de programación en bloques.
- Vincular programación con tecnología, IA, videojuegos, música, redes sociales, deportes o vida cotidiana.

También debe usarse cuando el agente detecte que un ejercicio de programación es demasiado genérico, por ejemplo:

```python
x = 5
y = 3
print(x + y)
```

En esos casos, debe convertirlo en un problema con contexto:

```python
likes_tiktok = 120
likes_instagram = 85
total_likes = likes_tiktok + likes_instagram
print("Total de likes de la publicación:", total_likes)
```

## Cuándo omitir esta skill

No es necesario consultarla cuando:

- Diego ya indicó un contexto temático específico y aprobado (ej: "usemos solo música y deportes para esta clase") y la tarea es desarrollar ese contexto, no elegirlo.
- La tarea es de iteración cosmética sobre un artefacto ya contextualizado (ajustes de redacción, formato, typos) y no implica cambiar o ampliar los contextos usados.
- Diego pidió explícitamente un contexto local o de la comuna — en ese caso usa `referencia-isla-de-maipo` en su lugar (o además, si conviene combinar ambos).

---

## 3. Principios centrales

### 3.1. Pertinencia antes que adorno

Los intereses estudiantiles deben mejorar la comprensión del contenido, no aparecer como decoración superficial.

Incorrecto:

> "Calcula una suma sobre videojuegos" sin relación con el contenido.

Correcto:

> "Crea un sistema simple de puntaje para un videojuego, donde cada victoria suma monedas y cada derrota resta vidas."

### 3.2. Ejemplos simples, pero con sentido

Los ejercicios deben ser comprensibles para estudiantes que están iniciándose en Python. No sobrecargar con sintaxis avanzada si el foco de la clase es básico.

Prioriza:

- variables;
- `print()`;
- comentarios con `#`;
- actualización de variables;
- condicionales;
- listas;
- ciclos simples;
- funciones básicas;
- entrada de datos con `input()`;
- simulaciones simples.

Evita introducir estructuras complejas si no fueron solicitadas.

### 3.3. Contextos juveniles con rigor técnico

Usar intereses del curso no significa bajar la exigencia. Cada ejercicio debe tener un propósito computacional claro.

Ejemplo de buena alineación:

| Interés | Contenido Python | Ejemplo |
|---|---|---|
| Música | listas, filtros, condicionales | Recomendar canción según estado de ánimo |
| Videojuegos | variables, actualización, condicionales | Sistema de vidas, monedas y niveles |
| Deportes | operaciones, condiciones, registro | Asistente de entrenamiento |
| Finanzas | sumas, acumuladores, umbrales | Control de gastos semanales |
| IA | condicionales, respuestas automáticas | Chatbot simulado con reglas simples |

### 3.4. Estudiantes como usuarios reales

Cuando se diseñen actividades, considerar que los estudiantes pueden construir soluciones para sí mismos o para personas cercanas.

Ejemplos:

- una app que recomiende música;
- un asistente para organizar tareas;
- un sistema para registrar entrenamiento;
- un gestor simple de gastos;
- un mini videojuego;
- un bot que entregue respuestas automáticas;
- un robot doméstico simulado.

### 3.5. Cuidar el lenguaje y la accesibilidad

Las instrucciones deben ser claras, breves y secuenciadas.

Usar lenguaje cercano, pero no infantilizado.

Preferir:

> "Tu programa debe pedir el nombre de una canción y guardarla en una playlist."

Evitar:

> "Realiza una implementación algorítmica de una estructura de almacenamiento secuencial musical."

---

## 4. Resumen rápido de intereses

Usa este resumen para contextualizar sin abrir la referencia completa. Está organizado por prioridad — si el usuario no indica contexto, prioriza de arriba hacia abajo. Cada bloque trae 1-2 ejemplos de ejercicio listos para adaptar.

### Prioridad muy alta

**Videojuegos 🎮** — PC, PlayStation, Steam, Brawl Stars, Clash Royale, FC Mobile, indies.
Útil para: rankings, puntajes, vidas, niveles, monedas, inventario, partidas.
Ejemplo: *"Guarda los puntajes de tres jugadores y muestra cuál fue el mejor evaluado."*

**Música 🎧** — Spotify, Apple Music, playlists, artistas, géneros.
Útil para: recomendadores, listas de artistas, filtros por género, conteo de reproducciones.
Ejemplo: *"Crea una playlist con listas de Python y recomienda una canción según el ánimo del usuario."*

**Redes sociales 📱** — TikTok, Instagram, WhatsApp, YouTube, Discord.
Útil para: contador de likes, simulador de publicaciones, mensajes automáticos, comparación de vistas.
Ejemplo: *"Suma los likes de varias publicaciones y muestra si la cuenta se volvió viral."*

**Tecnología, robots e IA 🤖** — robots, asistentes personales, automatización, IA.
Útil para: bots simples, asistentes con condicionales, reglas tipo "si pasa X, hacer Y", sensores simulados.
Ejemplo: *"Simula un robot doméstico que decide si limpia, avisa o se detiene según su batería."*

### Prioridad alta

**Deportes 🏀⚽🏐** — básquetbol, fútbol, vóley, BMX, gimnasio, entrenamiento.
Útil para: registro de entrenamientos, cálculo de rendimiento, metas semanales, comparación de marcas.
Ejemplo: *"Pide los minutos de ejercicio de hoy y entrega una recomendación general."*

**Salud y bienestar 🏃** — actividad física, hábitos saludables, estado físico.
Útil para: seguimiento de actividad, metas de movimiento, clasificación de intensidad. **Cuidado:** evitar diagnósticos médicos, lenguaje normativo sobre cuerpos o foco en calorías.
Ejemplo: *"Clasifica la intensidad de una sesión de entrenamiento como baja, media o alta."*

**Robots e IA aplicada** — hardware, mBot, sensores, automatización.
Ejemplo: *"Si el sensor detecta un obstáculo, el robot se detiene; si la batería es baja, recomienda cargar."*

### Prioridad media

**Dinero y finanzas 💸** — ahorro, gastos, presupuesto. **Cuidado:** usar solo datos ficticios, sin recomendaciones de inversión real.
Ejemplo: *"Suma los gastos de la semana y avisa si se superó el presupuesto."*

**Estudio y organización 📚** — agendas, recordatorios, planificación de estudio.
Ejemplo: *"Organiza materias y tiempos de estudio para una semana y muestra un resumen."*

**Clima 🌦️** — alertas y recomendaciones según condiciones.
Ejemplo: *"Si hay lluvia, recomienda llevar paraguas; si hace calor, recomienda llevar agua."*

**Archivos y limpieza digital 🗂️** — clasificar archivos, detectar archivos grandes.
Ejemplo: *"Clasifica una lista de archivos según su tipo: imagen, video o documento."*

> Para más variedad de ejemplos, banco extendido de ejercicios por interés y ejemplos de código modelo, abre `references/perfil-intereses.md`.

---

## 5. Temáticas recomendadas para Google Colab

Al diseñar un Colab completo, prioriza actividades con narrativa clara, breve y ejecutable. Hay 10 templates de actividad completos (contenido Python sugerido + ejemplo de consigna + extensión posible) en `references/actividades-colab.md`:

1. Playlist inteligente — listas, condicionales, recomendación según ánimo.
2. Ranking de videojuegos — comparación, actualización de puntajes.
3. Asistente de entrenamiento — `input()`, condicionales, mensajes personalizados.
4. Gestor de gastos — sumas, acumuladores, comparación con presupuesto.
5. App de estudio — listas, organización de datos, prioridades.
6. Asistente personal con IA simulada — condicionales, funciones, respuestas automáticas.
7. Alerta de clima — condicionales, operadores lógicos.
8. Robot doméstico simulado — condicionales, funciones, variables de estado.
9. Limpieza de archivos basura — listas, clasificación, conteo, filtros.
10. Automatización con sonidos — condicionales, variables booleanas, sensores simulados.

Abre la referencia cuando necesites el template completo de cualquiera de estas actividades para construir el Colab.

---

## 6. Uso de intereses según momento de la clase

### 6.1. Haz Ahora

Debe ser breve, visual o cercano.

Usar intereses para activar conversación o predicción.

Ejemplos:

- "¿Qué hace que un video de TikTok se vuelva viral?"
- "¿Cómo decide Spotify qué canción recomendar?"
- "¿Qué variables tendría un personaje de videojuego?"
- "¿Qué datos necesita una app para recomendarte una rutina?"
- "¿Qué condiciones debería revisar un robot antes de moverse?"

### 6.2. Introducción al contenido nuevo

Usar intereses como analogías.

Ejemplos:

| Concepto | Analogía recomendada |
|---|---|
| Variable | Puntaje, vidas, nombre de usuario, canción actual |
| Lista | Playlist, ranking de juegos, lista de tareas |
| Condicional | Si llueve, llevar paraguas; si quedan 0 vidas, terminar partida |
| Ciclo | Repetir canciones, revisar publicaciones, recorrer jugadores |
| Función | Acción reutilizable: recomendar canción, calcular puntaje |
| Actualizar variable | Sumar monedas, restar vidas, aumentar seguidores |

### 6.3. Práctica guiada

Debe usar un ejemplo de alta pertinencia y baja complejidad.

Recomendación:

- videojuegos para variables y actualización;
- música para listas;
- redes sociales para acumuladores;
- clima o robots para condicionales;
- deportes para operaciones y comparación.

### 6.4. Práctica independiente

Debe entregar opciones cuando sea posible.

Ejemplo:

> Elige uno de estos contextos para construir tu programa:
>
> 1. Playlist inteligente.
> 2. Ranking de videojuegos.
> 3. Asistente de entrenamiento.
> 4. Gestor de gastos.
> 5. Robot doméstico simulado.

Esto permite agencia estudiantil sin perder estructura.

### 6.5. Ticket de salida

Debe evaluar el contenido central, no solo el interés temático.

Ejemplo correcto:

> Crea un programa que use una variable `monedas`, la actualice dos veces y muestre el resultado final con un `print()` claro.

El contexto puede ser videojuegos, pero el criterio de evaluación debe ser programación.

---

## 7. Reglas para diseñar ejercicios contextualizados

Cada ejercicio debe incluir:

1. **Contexto breve:** situación cercana al estudiante.
2. **Tarea computacional:** qué debe programar.
3. **Restricciones técnicas:** qué contenidos de Python debe usar.
4. **Resultado esperado:** qué debe mostrar el programa.
5. **Criterios de éxito:** cómo saber si está correcto.
6. **Desafío opcional:** extensión para estudiantes que avanzan más rápido.

### Plantilla recomendada

```markdown
### Ejercicio: [nombre contextualizado]

**Contexto:**  
[Situación breve conectada con intereses del curso.]

**Tu tarea:**  
[Indicación concreta de lo que debe programar.]

**Debes usar:**  
- [contenido Python 1]
- [contenido Python 2]
- [contenido Python 3]

**Tu programa debe mostrar:**  
[Salida esperada en lenguaje simple.]

**Criterios de éxito:**  
- [criterio observable]
- [criterio observable]
- [criterio observable]

**Desafío opcional:**  
[Extensión breve.]
```

---

## 8. Reglas para diseñar Google Colabs

Cuando el agente cree un Google Colab, debe seguir esta estructura mínima:

```markdown
# Título de la clase

## Objetivo
Demostrar [habilidad de programación] mediante [producto o tarea contextualizada].

## Propósito
Hoy aprenderás esto porque te permite construir programas parecidos a herramientas que usas o podrías necesitar en tu vida diaria.

## 1. Activación
Pregunta o mini desafío contextualizado.

## 2. Contenido nuevo
Explicación breve del contenido Python.

## 3. Ejemplo guiado
Código incompleto o explicado paso a paso.

## 4. Práctica guiada
Actividad resuelta con apoyo.

## 5. Práctica independiente
Ejercicio con opciones de contexto.

## 6. Ticket de salida
Desafío breve, autónomo y alineado al objetivo.

## 7. Verificación
Lista de criterios para revisar el trabajo.
```

### Criterios específicos para Colabs

- Incluir celdas Markdown con instrucciones claras.
- Alternar explicación breve + código + práctica.
- Usar comentarios `#` en el código.
- No entregar bloques de código demasiado largos.
- Incorporar espacios para que estudiantes completen.
- Evitar depender de librerías externas si no son necesarias.
- Priorizar ejecución inmediata y feedback visible con `print()`.

---

## 9. Banco de transformaciones rápidas

Usar estas transformaciones cuando el usuario entregue ejercicios abstractos.

| Ejercicio abstracto | Transformación contextualizada |
|---|---|
| Sumar dos números | Sumar likes de TikTok e Instagram |
| Restar un número | Restar vidas en un videojuego |
| Comparar dos números | Comparar puntajes de dos jugadores |
| Usar una lista | Crear una playlist |
| Recorrer una lista | Mostrar canciones o juegos favoritos |
| Usar condicional | Recomendar acción según clima o estado del robot |
| Actualizar variable | Sumar monedas, seguidores o minutos de entrenamiento |
| Crear función | Crear una función que recomiende música o calcule puntaje |
| Usar input | Pedir al usuario su género musical, juego favorito o meta |
| Mostrar print | Mostrar resumen entretenido de una app |

---

## 10. Criterios de calidad

Antes de entregar una clase, Colab, ejercicio o proyecto, validar:

1. **Pertinencia:** ¿El contexto se conecta con intereses reales del curso?
2. **Claridad:** ¿La consigna se entiende sin explicación adicional?
3. **Alineación técnica:** ¿El ejercicio evalúa el contenido Python solicitado?
4. **Rigor:** ¿La tarea exige pensar, decidir o construir algo?
5. **Accesibilidad:** ¿El lenguaje es simple y las instrucciones están secuenciadas?
6. **Agencia:** ¿El estudiante puede elegir o personalizar al menos una parte cuando sea posible?
7. **Seguridad:** ¿No se entregan recomendaciones médicas, financieras o personales reales?
8. **Evaluabilidad:** ¿Hay criterios claros para saber si el programa funciona?
9. **Progresión:** ¿La dificultad avanza desde ejemplo guiado hacia autonomía?
10. **Sentido:** ¿El estudiante podría explicar para qué sirve lo que programó?

---

## 11. Formato de salida esperado

Cuando el usuario pida una actividad, el agente debe entregar preferentemente este formato:

```markdown
## Actividad: [título]

### Objetivo
[Objetivo observable de programación.]

### Contexto estudiantil utilizado
[Videojuegos / música / redes sociales / deportes / etc.]

### Consigna para estudiantes
[Texto listo para copiar y pegar.]

### Contenido Python trabajado
- [contenido 1]
- [contenido 2]
- [contenido 3]

### Código base
```python
# Código inicial, si corresponde
```

### Espacio para completar
```python
# Completa aquí
```

### Resultado esperado
[Descripción de la salida.]

### Verificación
- [criterio 1]
- [criterio 2]
- [criterio 3]

### Desafío opcional
[Extensión.]
```

Cuando el usuario pida una planificación completa, usar:

```markdown
## Clase: [título]

### Objetivo
Demostrar [habilidad] mediante [producto o tarea].

### Propósito
[Para qué sirve en la vida o intereses del estudiante.]

### Haz Ahora
[Actividad breve.]

### Introducción al contenido nuevo
[Máximo 3 ideas clave.]

### Práctica guiada
[Ejemplo contextualizado.]

### Práctica independiente
[Actividad autónoma.]

### Ticket de salida
[Desafío breve alineado al objetivo.]

### Respuesta esperada
[Resultado o ejemplo de solución.]

### Verificación docente
[Criterios observables.]
```

---

## 12. Restricciones y errores que el agente debe evitar

### 12.1. No usar intereses como adorno vacío

Evitar frases como:

> "Este ejercicio trata de videojuegos"  
> pero luego solo sumar `a + b` sin relación con mecánicas reales de juego.

### 12.2. No infantilizar

Los estudiantes pueden tener intereses juveniles, pero el lenguaje debe ser respetuoso y académico-cercano.

Evitar:

> "Vamos a hacer jueguitos súper fáciles."

Preferir:

> "Vamos a modelar una mecánica simple de puntaje usando variables."

### 12.3. No sobrecomplejizar

Si la clase es introductoria, no usar:

- clases;
- APIs;
- scraping;
- machine learning real;
- bases de datos;
- interfaces gráficas;
- librerías externas innecesarias.

A menos que el usuario lo solicite explícitamente.

### 12.4. No entregar consejos médicos o financieros reales

En salud:

- usar datos ficticios;
- hablar de orientación general;
- evitar diagnósticos;
- evitar juicios sobre cuerpos.

En finanzas:

- usar simulaciones;
- evitar recomendar inversiones;
- evitar prometer ganancias;
- evitar incentivar trading real.

### 12.5. No depender de plataformas externas

Se puede mencionar Spotify, TikTok, Instagram, Discord, Steam u otras plataformas como contexto cultural, pero no exigir cuentas reales ni conexión a servicios externos.

### 12.6. No perder el foco en programación

El interés contextual debe estar subordinado al aprendizaje computacional.

Cada actividad debe dejar claro qué habilidad de programación se está desarrollando.

### 12.7. No usar datos personales reales

No pedir información sensible a estudiantes.

Preferir datos ficticios o inventados:

- canciones ficticias;
- usuarios ficticios;
- presupuestos simulados;
- rutinas inventadas;
- publicaciones ficticias.

---

## 13. Recomendaciones de priorización

Cuando el usuario no indique contexto específico, priorizar en este orden:

1. Videojuegos.
2. Música.
3. Redes sociales.
4. Tecnología, robots o IA.
5. Deportes.
6. Salud y bienestar.
7. Finanzas simuladas.
8. Estudio y organización.
9. Clima.
10. Limpieza digital.

Para proyectos finales, priorizar:

- app asistente;
- recomendador;
- gestor de gastos;
- simulador de robot;
- mini videojuego;
- organizador de estudio;
- playlist inteligente.

---

## 14. Verificación interna antes de responder

Antes de entregar el producto final, el agente debe revisar:

- ¿El contexto usado aparece en el perfil de intereses?
- ¿La actividad es adecuada para estudiantes que aprenden Python?
- ¿La consigna es clara y copiable?
- ¿El contenido de programación está explícito?
- ¿El ejemplo usa nombres de variables comprensibles?
- ¿El código, si existe, puede ejecutarse en Google Colab?
- ¿Hay criterios de éxito?
- ¿Hay una extensión opcional?
- ¿Se evitaron recomendaciones médicas o financieras reales?
- ¿La actividad mantiene rigor técnico?

---

## 15. Regla final de uso

Si el usuario pide diseñar una clase o Colab de programación y no entrega contexto, el agente debe asumir por defecto que conviene usar una combinación de:

- videojuegos;
- música;
- redes sociales;
- tecnología/IA;
- deportes.

La elección debe explicitarse brevemente en la salida bajo el apartado:

```markdown
### Contexto estudiantil utilizado
```
