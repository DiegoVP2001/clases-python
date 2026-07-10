# Prompt — Sesión 2: Actividad en parejas (Colab)

## Contexto para Claude

Genera un Jupyter notebook (Colab) para una actividad de recordatorio en parejas. Las parejas son sorteadas aleatoriamente al inicio de la clase. Hay 3 ejercicios integradores de dificultad creciente, todos con conceptos ya vistos. Al final, se revisan en conjunto (el profesor proyecta y distintas parejas comparten cada ejercicio).

El notebook va a Google Classroom como siempre.

## Estructura de la clase

| Bloque | Duración |
|---|---|
| Sorteo aleatorio de parejas | 3 min |
| Trabajo autónomo en Colab | 30 min |
| Revisión proyectada en clase | 20 min |
| Cierre / ticket de salida | 7 min |

## Los 3 ejercicios

### Ejercicio 1 — Carnet de conducir

**Conceptos:** `input`, comparación (`>=`), `if / else`

El programa pide el nombre y la edad de la persona. Dice si ya puede sacar el carnet de conducir (edad ≥ 18) o cuántos años le faltan.

Output esperado (si tiene 16 años):
```
Nombre: Valentina
Edad: 16
Valentina, te faltan 2 años para poder sacar el carnet.
```

Output esperado (si tiene 18 o más):
```
Nombre: Rodrigo
Edad: 19
Rodrigo, ¡ya puedes sacar el carnet!
```

---

### Ejercicio 2 — Promedio de notas

**Conceptos:** `input`, operaciones aritméticas, comparación, `if / else`

El programa pide dos notas (escala 1.0 a 7.0). Calcula el promedio y dice si aprueba (≥ 4.0) o reprueba. Muestra también cuánto le faltó o cuánto le sobró respecto al 4.0.

Output esperado (reprueba):
```
Nota 1: 3.5
Nota 2: 4.0
Promedio: 3.75
Resultado: Reprueba. Le faltó 0.25 para llegar al 4.0.
```

Output esperado (aprueba):
```
Nota 1: 5.0
Nota 2: 6.0
Promedio: 5.5
Resultado: Aprueba. Le sobró 1.5 sobre el mínimo.
```

---

### Ejercicio 3 — Saldo BIP

**Conceptos:** `input`, `and`, condición compuesta, `if / else`

El programa pide el precio del pasaje y el saldo actual de la tarjeta BIP. Si el saldo alcanza, muestra cuánto queda después de pagar. Si no alcanza, muestra cuánto falta para poder pagar.

Output esperado (no alcanza):
```
Precio del pasaje: 800
Saldo BIP: 650
No alcanza. Te faltan $150 para el pasaje.
```

Output esperado (alcanza):
```
Precio del pasaje: 800
Saldo BIP: 1200
¡Alcanza! Después de pagar te quedan $400 en la tarjeta.
```

---

## Restricciones del notebook

- Variables en español snake_case (`edad_usuario`, `promedio_notas`, `saldo_bip`).
- Outputs con etiqueta descriptiva — nunca `print(resultado)` a secas.
- Soluciones al final en sección "📋 Soluciones" con `<details>` individuales, agrupadas, no intercaladas.
- No usar `elif`, funciones, listas, ciclos ni contenido no visto.
- Celdas de texto con instrucciones claras para la pareja antes de cada ejercicio.
- Al inicio del notebook: celda de bienvenida con instrucciones de la dinámica (trabajar en pareja, un Colab compartido, un integrante escribe y el otro revisa).
- Ticket de salida al final: una celda de texto con la pregunta "¿Qué concepto se te hizo más fácil recordar y cuál más difícil? Escríbelo como comentario en Python (`#`)".
