# Clase 18 — Reforzamiento Condicionales — Dinámica para el profesor

**Duración:** 80 min (bloque completo de la clase).
**Modalidad:** mismas parejas de Clase 17.
**Material necesario:** ninguno nuevo. Solo lo que ya existe:
- Los Colabs entregados por cada pareja en Clase 17 (vía Classroom).
- `clase-17-ejercitacion-condicionales/old/Clase 17 - Ejercitación Condicionales - Solucionario.ipynb`.

**Nombre de la dinámica:** *"Quien terminó, enseña — quien no, corrige en vivo"*.

**Por qué esta dinámica y no otra:** las parejas quedaron con avance muy disparejo (algunas resolvieron casi todo, otras poco) y las preguntas ya están públicas en cada Colab desde el jueves — no hay nada que "spoilear". En vez de tratar la disparidad de avance como un problema a resolver con más material, se usa como el motor de la clase: las parejas avanzadas explican, las atrasadas terminan mientras escuchan.

---

## Antes de que lleguen los estudiantes (2-3 min, en tu escritorio)

Revisa rápidamente en Classroom qué pareja llegó más lejos en cada uno de los 4 ejercicios (delivery, gimnasio, furgón escolar, festival). No necesitas anotar nada formal — solo tener en la cabeza, para cada ejercicio, **una pareja candidata a pasar primero** si nadie se ofrece. Esto evita perder tiempo en clase decidiendo a quién preguntar.

---

## Apertura (1 min)

Encuadre breve, en voz alta: *"Hoy retomamos los ejercicios del jueves. Las parejas que ya los tienen resueltos nos van a explicar cómo lo pensaron, y las que no alcanzaron a terminar los completan mientras escuchan."*

No hay Haz Ahora ni ICN — se entra directo al bloque de revisión.

---

## Bloque único: revisión ejercicio por ejercicio (75 min aprox., el resto de la clase)

Recorre los 4 ejercicios **en orden** (1 → Delivery, 2 → Gimnasio, 3 → Furgón escolar, 4 → Festival). Para cada uno:

### 1. Pregunta abierta al curso (10-15 seg)
*"¿Qué pareja tiene este resuelto y lo puede mostrar?"*

- **Si una o más parejas levantan la mano:** elige una y proyecta su pantalla tal cual está — sin que la prepare ni la limpie antes. Ella explica su propio código, ambos integrantes participan (uno puede leer el código, el otro explicar la lógica en palabras).
- **Si nadie se ofrece pero tú ya sabes (por tu revisión previa) que alguna pareja lo tiene:** invítala directamente por nombre, sin esperar que se ofrezca — ahorra tiempo.
- **Si nadie en el curso llegó a ese ejercicio:** pasa directo al punto 3 (resolver tú en vivo).

### 2. Mientras la pareja explica (2-4 min por ejercicio)

Las parejas que **no** llegaron a ese ejercicio lo van completando en sus propios Colabs a la vez que escuchan — no esperan a que termine la explicación para empezar a escribir. El objetivo es que copien la **lógica**, no el código exacto letra por letra.

**Caso especial — dos parejas resolvieron el mismo ejercicio con estructuras distintas** (por ejemplo, una anidó `if` dentro de `if` y otra usó `elif` con un `if` adentro, como el patrón de la Guiada): si el tiempo alcanza, muestra ambas seguidas y pregunta al curso cuál les parece más clara de leer. Esto conecta directo con el objetivo de la clase original — elegir la estructura correcta, no solo que el código funcione. Si vas atrasado en el tiempo, omite este paso sin culpa; no es obligatorio.

### 3. Si nadie resolvió el ejercicio: lo resuelves tú (2-3 min)

Abre directamente el Solucionario ya generado (`Clase 17 - Ejercitación Condicionales - Solucionario.ipynb`, en `old/`) y proyecta la solución, explicando en voz alta el razonamiento — no hace falta prepararlo antes, el archivo ya existe.

---

## Parejas muy avanzadas (las que ya terminaron los 4 ejercicios)

No las dejes esperando sentadas. En cuanto detectes que una pareja terminó todo (por tu revisión previa, o porque ya pasó a explicar sus 4 ejercicios), asígnale el rol de **"consultora"**: se levanta y ayuda a la pareja más cercana físicamente que sigue atascada, en paralelo a que tú sigues conduciendo la revisión con el resto del curso. Esto reemplaza tu rol de circular mesa por mesa — deja que las parejas avanzadas hagan ese trabajo.

No hace falta anunciar esto formalmente al curso completo; basta con decírselo en voz baja a cada pareja avanzada apenas termina.

---

## Cierre (2-3 min, si queda tiempo)

No hay Ticket de Salida formal en esta clase (es reforzamiento, no evaluación). Si queda tiempo, cierra con una pregunta rápida a viva voz: *"¿Cuál de los 4 ejercicios les costó más decidir qué estructura usar?"* — sin necesidad de registrar respuestas, solo para dejar la reflexión activa antes de la evaluación del 21 de julio.

Si no queda tiempo, se puede omitir sin problema — el valor de la clase está en la revisión misma, no en un cierre formal.

---

## Qué hacer si el tiempo no alcanza para los 4 ejercicios

Prioriza en este orden, igual que en la revisión proyectada original de Clase 17: **Ejercicio 2 (gimnasio, if anidado con else en cada nivel)** y **Ejercicio 4 (festival, el patrón elif + if anidado)** son los más propensos a errores de indentación y los que más vale la pena revisar en vivo. Si el tiempo se acota, sacrifica primero el Ejercicio 1 (delivery, el más simple, sirvió de calentamiento) o reduce el tiempo de discusión de estructuras alternativas del punto 2.
