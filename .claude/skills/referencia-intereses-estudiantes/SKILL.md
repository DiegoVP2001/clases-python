---
name: referencia-intereses-estudiantes
description: Usa esta skill para contextualizar clases, ejercicios, Google Colabs, tickets de salida y proyectos de programación a partir de los gustos declarados por estudiantes. Prioriza ejemplos significativos, cercanos y accionables para cursos que transitan desde programación en bloques hacia Python.
---

# Skill: Contextualización de programación según intereses de estudiantes

## 1. Propósito de la skill

Esta skill ayuda a un agente IA a diseñar materiales de programación más pertinentes, significativos y motivadores para estudiantes, usando como base sus intereses declarados.

Debe utilizarse para transformar contenidos de programación —especialmente en Python y Google Colab— en experiencias conectadas con gustos reales del curso, tales como videojuegos, música, deportes, redes sociales, tecnología, IA, salud, finanzas, estudio y automatización.

El objetivo no es “decorar” ejercicios con temas juveniles, sino usar esos intereses como contexto auténtico para formular problemas, variables, condiciones, funciones, listas, ciclos, entradas/salidas, simulaciones y proyectos.

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

> “Calcula una suma sobre videojuegos” sin relación con el contenido.

Correcto:

> “Crea un sistema simple de puntaje para un videojuego, donde cada victoria suma monedas y cada derrota resta vidas.”

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

> “Tu programa debe pedir el nombre de una canción y guardarla en una playlist.”

Evitar:

> “Realiza una implementación algorítmica de una estructura de almacenamiento secuencial musical.”

---

## 4. Perfil de intereses del curso

### 4.1. Intereses de prioridad muy alta

Estos temas deben aparecer con mayor frecuencia en ejemplos, prácticas y proyectos.

#### Videojuegos 🎮

Aparecen intereses como:

- jugar en PC;
- PlayStation;
- Steam;
- Brawl Stars;
- Clash Royale;
- FC Mobile;
- juegos indie.

Usos recomendados en Python:

- rankings;
- puntajes;
- vidas;
- niveles;
- monedas;
- decisiones;
- mejoras de personaje;
- inventario;
- simuladores de partidas;
- torneos simples;
- registro de partidas.

Ejemplos de ejercicios:

- Crear una variable `vidas` y restar una vida cuando el jugador pierde.
- Guardar puntajes de tres jugadores y mostrar el mayor.
- Crear un ranking de juegos favoritos.
- Simular una tienda donde el jugador compra mejoras con monedas.
- Usar condicionales para decidir si un jugador pasa de nivel.

#### Música 🎧

Aparecen intereses como:

- Spotify;
- Apple Music;
- escuchar música;
- playlists;
- artistas;
- géneros musicales.

Usos recomendados en Python:

- recomendadores de canciones;
- listas de artistas;
- filtros por género;
- playlists según estado de ánimo;
- conteo de reproducciones;
- ranking de canciones favoritas.

Ejemplos de ejercicios:

- Crear una playlist con listas de Python.
- Recomendar una canción según el ánimo del usuario.
- Contar cuántas canciones hay en una lista.
- Filtrar canciones por género.
- Mostrar el artista más escuchado.

#### Redes sociales 📱

Aparecen intereses como:

- TikTok;
- Instagram;
- WhatsApp;
- YouTube;
- Discord.

Usos recomendados en Python:

- estadísticas de uso;
- contador de likes;
- simulador de publicaciones;
- mensajes automáticos;
- análisis de seguidores;
- comparación de vistas.

Ejemplos de ejercicios:

- Calcular el total de likes entre varias publicaciones.
- Simular una publicación y mostrar si se volvió viral.
- Comparar vistas de videos.
- Crear mensajes automáticos para un bot de Discord.
- Contar minutos diarios en redes sociales.

#### Tecnología, robots e IA 🤖

Aparecen intereses como:

- robots;
- asistentes personales;
- automatización;
- inteligencia artificial.

Usos recomendados en Python:

- bots simples;
- asistentes con condicionales;
- automatización tipo “si pasa X, hacer Y”;
- simuladores de robots;
- reglas de decisión;
- respuestas automáticas.

Ejemplos de ejercicios:

- Crear un asistente que responda según la necesidad del usuario.
- Simular un robot doméstico que decide si limpia, avisa o se detiene.
- Crear una IA ficticia que recomienda una acción.
- Automatizar una luz según una condición.
- Simular sensores con variables.

---

### 4.2. Intereses de prioridad alta

Estos temas deben usarse con frecuencia, especialmente en prácticas independientes y proyectos aplicados.

#### Deportes 🏀⚽🏐

Aparecen intereses como:

- básquetbol;
- fútbol;
- vóley;
- BMX;
- gimnasio;
- entrenamiento.

Usos recomendados en Python:

- registro de entrenamientos;
- cálculo de rendimiento;
- metas semanales;
- estadísticas deportivas;
- comparación de marcas;
- asistencia de entrenamiento.

Ejemplos de ejercicios:

- Pedir minutos de ejercicio y entregar una recomendación.
- Calcular promedio de goles, puntos o repeticiones.
- Registrar entrenamientos de una semana.
- Determinar si se cumplió una meta.
- Comparar rendimiento entre días.

#### Salud y bienestar 🏃

Aparecen intereses como:

- IMC;
- estado físico;
- actividad de trote;
- hábitos saludables.

Usos recomendados en Python:

- calculadoras simples de salud;
- seguimiento de actividad física;
- recomendaciones generales según actividad;
- registro de hábitos;
- metas de movimiento.

Cuidado pedagógico:

- Evitar emitir diagnósticos médicos.
- Evitar lenguaje normativo sobre cuerpos.
- Priorizar bienestar, hábitos y movimiento.
- No centrar actividades en calorías si no es necesario.
- Presentar resultados como información orientativa, no como evaluación de salud personal.

Ejemplos de ejercicios:

- Registrar minutos de actividad física.
- Recomendar descanso o hidratación según tiempo de ejercicio.
- Calcular si se cumplió una meta semanal de movimiento.
- Simular una app de bienestar.
- Clasificar intensidad de actividad: baja, media o alta.

#### Robots e IA aplicada

Este interés puede conectarse con hardware, mBot, sensores o automatización, aunque el ejercicio sea solo simulado.

Ejemplos:

- Si el sensor detecta un obstáculo, el robot se detiene.
- Si la temperatura es alta, el asistente recomienda hidratarse.
- Si el usuario aplaude, se prende una luz simulada.
- Si el robot detecta basura, activa modo limpieza.

---

### 4.3. Intereses de prioridad media

Estos temas pueden utilizarse como variación, desafío o proyecto específico.

#### Dinero y finanzas 💸

Aparecen intereses como:

- ahorro;
- inversión;
- trading;
- gestión de gastos.

Usos recomendados en Python:

- presupuesto mensual;
- simulador de ahorro;
- control de gastos;
- alertas si se supera un presupuesto;
- cálculo de metas.

Cuidado pedagógico:

- No entregar recomendaciones reales de inversión.
- No simular promesas de ganancia.
- Enmarcar como educación financiera básica.
- Usar datos ficticios.

Ejemplos de ejercicios:

- Sumar gastos semanales.
- Avisar si se supera un presupuesto.
- Calcular cuánto falta para una meta de ahorro.
- Clasificar gastos en categorías.
- Simular ahorro mensual con datos inventados.

#### Estudio y organización 📚

Uso recomendado:

- agendas;
- recordatorios;
- organización de materias;
- planificación de estudio;
- temporizadores simples.

Ejemplos:

- Crear una app de estudio que recomiende cuánto tiempo dedicar a una materia.
- Ordenar tareas según prioridad.
- Mostrar recordatorios.
- Calcular tiempo total de estudio semanal.

#### Clima 🌦️

Uso recomendado:

- alertas;
- recomendaciones;
- condicionales;
- simulaciones.

Ejemplos:

- Si hay lluvia, recomendar llevar paraguas.
- Si hace frío, recomendar abrigo.
- Si hace calor, recomendar agua.

#### Archivos y limpieza digital 🗂️

Uso recomendado:

- clasificar archivos;
- detectar archivos grandes;
- simular limpieza de memoria;
- organizar extensiones.

Ejemplos:

- Clasificar archivos según tipo: imagen, video, documento.
- Marcar archivos grandes para revisar.
- Simular eliminación de archivos basura.

---

## 5. Temáticas recomendadas para Google Colab

Al diseñar Colabs, priorizar actividades con una narrativa clara, breve y ejecutable.

### 5.1. Playlist inteligente

**Contenido Python sugerido:**

- variables;
- listas;
- condicionales;
- `input()`;
- `print()`.

**Ejemplo de consigna:**

> Crea un programa que pregunte el estado de ánimo del usuario y recomiende una canción o playlist.

**Extensión posible:**

- agregar géneros;
- agregar artistas;
- contar canciones;
- permitir que el usuario agregue una canción.

---

### 5.2. Ranking de videojuegos

**Contenido Python sugerido:**

- variables;
- listas;
- comparación;
- condicionales;
- actualización de puntajes.

**Ejemplo de consigna:**

> Guarda tres videojuegos favoritos con sus puntajes y muestra cuál fue el mejor evaluado.

**Extensión posible:**

- agregar ranking;
- sumar puntos extra;
- simular partidas;
- actualizar monedas o vidas.

---

### 5.3. Asistente de entrenamiento

**Contenido Python sugerido:**

- `input()`;
- operaciones matemáticas;
- condicionales;
- mensajes personalizados.

**Ejemplo de consigna:**

> Pide los minutos de ejercicio realizados hoy y entrega una recomendación general de entrenamiento.

**Extensión posible:**

- calcular meta semanal;
- comparar días;
- clasificar intensidad;
- generar mensaje motivador.

---

### 5.4. Gestor de gastos

**Contenido Python sugerido:**

- variables;
- suma;
- condicionales;
- comparación con presupuesto;
- acumuladores.

**Ejemplo de consigna:**

> Suma los gastos de la semana y avisa si se superó el presupuesto.

**Extensión posible:**

- separar gastos por categoría;
- calcular ahorro restante;
- simular una meta de compra;
- mostrar alerta.

---

### 5.5. App de estudio

**Contenido Python sugerido:**

- listas;
- diccionarios simples, si corresponde;
- condicionales;
- organización de datos.

**Ejemplo de consigna:**

> Organiza materias, tiempos de estudio y recordatorios para una semana.

**Extensión posible:**

- priorizar asignaturas;
- recomendar tiempo según dificultad;
- generar resumen de estudio.

---

### 5.6. Asistente personal con IA simulada

**Contenido Python sugerido:**

- condicionales;
- funciones;
- respuestas automáticas;
- entrada de texto.

**Ejemplo de consigna:**

> Según la necesidad escrita por el usuario, entrega una respuesta automática como si fuera un asistente personal.

**Extensión posible:**

- crear categorías de respuestas;
- agregar frases personalizadas;
- simular conversación.

---

### 5.7. Alerta de clima

**Contenido Python sugerido:**

- variables;
- condicionales;
- operadores lógicos;
- mensajes de salida.

**Ejemplo de consigna:**

> Si la temperatura es baja, alta o hay lluvia, entrega una recomendación.

**Extensión posible:**

- agregar viento;
- agregar probabilidad de lluvia;
- generar outfit recomendado.

---

### 5.8. Robot doméstico simulado

**Contenido Python sugerido:**

- condicionales;
- funciones;
- variables de estado;
- reglas de prioridad.

**Ejemplo de consigna:**

> Usa condiciones para decidir si el robot limpia, cocina, avisa o se detiene.

**Extensión posible:**

- agregar sensores simulados;
- agregar batería;
- definir prioridades;
- conectar con lógica de mBot.

---

### 5.9. Limpieza de archivos basura

**Contenido Python sugerido:**

- listas;
- condicionales;
- clasificación;
- conteo;
- filtros.

**Ejemplo de consigna:**

> Clasifica archivos según tamaño o tipo y marca cuáles podrían revisarse para liberar espacio.

**Extensión posible:**

- contar archivos por extensión;
- calcular memoria total;
- identificar archivos duplicados simulados.

---

### 5.10. Automatización con sonidos

**Contenido Python sugerido:**

- condicionales;
- variables booleanas;
- simulación de sensores.

**Ejemplo de consigna:**

> Simula que un aplauso prende una luz usando condiciones.

**Extensión posible:**

- agregar doble aplauso;
- apagar luz;
- conectar con domótica básica.

---

## 6. Uso de intereses según momento de la clase

### 6.1. Haz Ahora

Debe ser breve, visual o cercano.

Usar intereses para activar conversación o predicción.

Ejemplos:

- “¿Qué hace que un video de TikTok se vuelva viral?”
- “¿Cómo decide Spotify qué canción recomendar?”
- “¿Qué variables tendría un personaje de videojuego?”
- “¿Qué datos necesita una app para recomendarte una rutina?”
- “¿Qué condiciones debería revisar un robot antes de moverse?”

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

> “Este ejercicio trata de videojuegos”  
> pero luego solo sumar `a + b` sin relación con mecánicas reales de juego.

### 12.2. No infantilizar

Los estudiantes pueden tener intereses juveniles, pero el lenguaje debe ser respetuoso y académico-cercano.

Evitar:

> “Vamos a hacer jueguitos súper fáciles.”

Preferir:

> “Vamos a modelar una mecánica simple de puntaje usando variables.”

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

## 14. Ejemplos modelo

### Ejemplo 1: actualización de variables con videojuegos

```python
# Sistema simple de monedas en un videojuego

monedas = 100
print("Monedas iniciales:", monedas)

# El jugador gana una partida
monedas = monedas + 50
print("Después de ganar una partida:", monedas)

# El jugador compra una mejora
monedas = monedas - 30
print("Después de comprar una mejora:", monedas)
```

### Ejemplo 2: playlist con listas

```python
# Playlist simple

playlist = ["Canción 1", "Canción 2", "Canción 3"]

print("Tu playlist de hoy:")
print(playlist)
```

### Ejemplo 3: asistente de entrenamiento

```python
# Asistente simple de entrenamiento

minutos = int(input("¿Cuántos minutos entrenaste hoy? "))

if minutos >= 45:
    print("Buen trabajo. Hoy cumpliste una sesión larga.")
elif minutos >= 20:
    print("Buen avance. Fue una sesión media.")
else:
    print("Hoy fue una sesión breve. Puedes retomarlo mañana.")
```

### Ejemplo 4: simulador de robot

```python
# Robot doméstico simulado

bateria = 25
obstaculo = True

if bateria < 20:
    print("Robot detenido: necesita cargar batería.")
elif obstaculo == True:
    print("Robot detenido: hay un obstáculo.")
else:
    print("Robot en movimiento: puede limpiar.")
```

---

## 15. Verificación interna antes de responder

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

## 16. Regla final de uso

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
