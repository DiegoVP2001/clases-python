# Prompt de sesión — Clase N°21.5: continue y break

**Fecha programada:** martes 2026-08-11
**Clase Picuino de referencia:** N°15 — Sentencia `continue` + N°16 — Sentencia `break` (combinadas en una sola clase de 80 min)
**Estado:** sin propuesta aún.

## Contexto acordado (planificación del 2026-08-04)

- Resuelve el pendiente anotado el 2026-07-28: al diseñar Clase 20 (For Anidado), Diego dejó continue/break fuera de su alcance ("accesorios" frente a la lógica de anidamiento), sin fecha ni número asignado. Ver `Clase 20 - For Anidado - Historial.md`.
- **Numeración:** se inserta como **N°21.5** (folder `clase-21b-continue-break`, mismo patrón que ya usó el proyecto con N°19.5/`clase-19b-...`), no como N°22 — así no se corre en cascada toda la numeración posterior (while se queda en N°22, funciones en N°23, etc.). Al guardar la spec, agregar la fila correspondiente en `Historial-Curricular.md` entre la fila 21 y la fila 22.
- **Contenidos previos asumidos:** todo hasta N°21 inclusive — for, range(), for anidado, ya ejercitados en la ayudantía del lunes 2026-08-10.
- Se dicta el martes 2026-08-11, es decir DESPUÉS de la ayudantía N°21 (que no alcanza a cubrir continue/break) y ANTES de la clase de while (N°22, jueves 2026-08-13) — el patrón `while True: ... break` de esa clase se apoya en lo que aquí se enseña.

## Foco de contenido (discutido y acordado con Diego el 2026-08-04)

- **`continue`:** salta el resto del cuerpo del bucle y sigue con la próxima iteración — típico para filtrar sin anidar un `if` extra. Ejemplo de referencia (contrastar contra la versión "solo con `if`" para que quede claro que es una herramienta de legibilidad, no una capacidad nueva):
  ```python
  for numero in range(1, 21):
      if numero % 3 == 0:
          continue
      print("Número:", numero)
  ```
- **`break`:** corta el ciclo de inmediato — sí agrega capacidad real (sin él se necesitaría una variable bandera). Dos patrones de referencia:
  - Búsqueda que se detiene al encontrar algo (ej. primer divisor de un número, para decidir si es primo).
  - Intentos limitados (ej. clave con máximo de intentos, usando `for intento in range(1, N)`).
- **Sugerencia de diseño, a validar en el gate de objetivo:** dejar `for...else` fuera de esta clase — la propia ficha Picuino lo marca como "uso avanzado, requiere ejemplo visual", mismo criterio que ya usó Clase 20 para recortar alcance.
- **Práctica Independiente sugerida:** un ejercicio de filtrado (`continue`) y uno de búsqueda o intentos (`break`), para que ambos queden ejercitados por separado.

## OAs sugeridos

OA1, OA3 (mismos que el resto del bloque de Ciclos).

## Prompt para iniciar la sesión

> Vamos con la clase de continue y break (Picuino N°15 y N°16), para el martes 2026-08-11. Va como N°21.5 en `Historial-Curricular.md` (carpeta `clase-21b-continue-break`, mismo patrón que N°19.5). Contenidos previos: todo hasta N°21 (for, range, for anidado, ya ejercitados en la ayudantía del lunes). Actívate con `disenar-clase`.
