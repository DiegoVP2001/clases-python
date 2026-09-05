# Prompt de sesión — Clase N°33: Strings — búsqueda de texto (in, find())

**Fecha programada:** martes 2026-09-08
**Clase Picuino de referencia:** N°23 — Métodos de cadenas de texto (**parcial** — la mitad de búsqueda, complementaria a la Clase 32)
**Estado:** clase nueva, creada 2026-08-26 al dividir la antigua "Clase 30 — Strings: métodos y f-strings". Diseño no iniciado — sin propuesta de objetivo/actitud/estructura todavía.

## Por qué existe esta clase (contexto de la sesión 2026-08-26 que la creó)

Durante el diseño de la Clase 32 (métodos de texto), Diego determinó que **modificar/separar texto** y **buscar dentro de un texto** son habilidades distintas que no deben mezclarse en la misma sesión: una transforma el dato, la otra solo lo consulta. Se decidió separar la búsqueda (`in`, `find()`) en esta clase nueva, dictada **después** del lunes estándar de control de Strings (N°31) — ese control no cubre ni la Clase 32 (métodos) ni esta clase (búsqueda): su foco quedó acotado solo a N°28 y N°29. Ver `Historial-Curricular.md`, nota "Renumeración 2026-08-26 (segunda pasada)" y nota "Renumeración 2026-09-03", y `clase-32-strings-metodos/Prompt.md` para el detalle completo de la división y de la renumeración posterior.

De paso, en la misma sesión se decidió sacar el formateo con f-strings (Picuino N°24) del currículo cercano por completo — no tiene relación con esta clase, quedó pendiente sin fecha ni número (ver nota de renumeración).

## Contenido acordado (sin cerrar en gate formal — a confirmar al diseñar)

- **`in`** — verificar si un texto está dentro de otro (`"maní" in nota_pedido`). Sensible a mayúsculas/minúsculas — se usa junto con `.lower()` para normalizar antes de comparar.
- **`find()`** — igual que `in`, pero además dice en qué posición empieza el texto buscado (o `-1` si no está).
- **Contexto sugerido, sin confirmar formalmente:** continuar con Los Mellis (mismo universo narrativo que la Clase 32) — revisar si una nota especial de un pedido contiene una palabra de alerta o alergia (ej. "sin maní", "sin gluten"), similar al ejercicio de Picuino "detector de palabras tabú" pero aplicado a un caso real de local de comida. Confirmar con Diego si sigue el mismo criterio de "Los Mellis como escenario único de toda la clase" que se usó en la Clase 32, o si acá conviene diversificar.
- **Contenidos previos asumidos:** todo hasta N°32 inclusive (Strings: indexing/slicing, recorrido con `for`, métodos para modificar/separar texto, y el lunes estándar de control N°31 — que en la práctica solo repasó N°28 y N°29, no los métodos).

## Qué falta para la especificación completa

Esta clase no pasó por sesión de diseño todavía. Al retomar, `disenar-clase` parte desde su Paso 1 completo: confirmar contenidos previos contra `Historial-Curricular.md` (verificar que N°32 y N°31 ya tengan su Spec/Control aprobados antes de asumir que se vieron), ofrecer opciones de actitud, y proponer objetivo + estructura de 5 pasos. Solo 2 constructos nuevos (`in`, `find()`), pero con narrativa rica alcanza para una clase completa — mismo caso que tuvo Clase 21.5 (`continue`/`break`).

## OAs sugeridos

OA2, OA3.

## Prompt para iniciar la sesión

> Vamos con la Clase 33 (Strings — búsqueda de texto: `in`, `find()`), Picuino N°23 parcial. Es clase nueva, creada al dividir la antigua Clase 30 (esa clase es hoy la N°32). Contenidos previos: todo hasta N°32 inclusive, incluyendo el Lunes estándar Control Strings N°31 (cuyo foco fue solo N°28 y N°29, no los métodos). Contexto sugerido: continuar con Los Mellis revisando notas de pedido por palabras de alerta — ver `Prompt.md` para el detalle de por qué se separó de la Clase 32. Actívate con `disenar-clase`.
