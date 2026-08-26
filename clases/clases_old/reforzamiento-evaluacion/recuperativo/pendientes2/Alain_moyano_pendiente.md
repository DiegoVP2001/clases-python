# 02_evaluacion_recuperativa

> **Criterio de transcripción:** se conserva el contenido visible, incluidos errores de sintaxis, fragmentos duplicados y texto sin comillas. No se corrigió el código. Las partes no fotografiadas o cortadas se señalan explícitamente.

---

## Ejercicio 1 — Promedio de tiempos de entrenamiento

> El encabezado completo y el puntaje no aparecen en las fotografías. El título se recupera del comentario de la celda de código.

Define 3 variables con tiempos de entrenamiento en minutos y calcula el promedio.

**El programa debe imprimir con `print()`:**

```text
Tiempo 1: 32
Tiempo 2: 28
Tiempo 3: 35
Promedio de minutos: 31.666666666666668
```

*Los valores de los tiempos pueden ser distintos.*

### Código visible en la celda

```python
# Ejercicio 1 — Promedio de tiempos de entrenamiento
# Escribe tu código aquí
tiempo1 = 32
tiempo2 = 28
tiempo3 = 35

promedio = (tiempo1 + tiempo2 + tiempo3) / 3

print(Tiempo 1:, tiempo1)
print(Tiempo 2:, tiempo2)
print(Tiempo 3:, tiempo3)
print(Promedio de minutos:, promedio)tiempo1 = 32
tiempo2 = 28
tiempo3 = 35

promedio = (tiempo1 + tiempo2 + tiempo3) / 3

print(Tiempo 1:, tiempo1)
print(Tiempo 2:, tiempo2)
print(Tiempo 3:, tiempo3)
print(Promedio de minutos:, promedio)
```

---

## Ejercicio 2 — Reporte de inventario del kiosco ⭐ (10 pts)

> El enunciado y la salida esperada del ejercicio no aparecen completos en las fotografías. Solo se observa el título y la celda de código.

### Código visible en la celda

```python
# Los datos ya están definidos — escribe los print() correctos

producto_1 = Jugos
stock_1 = 24
precio_1 = 750

producto_2 = Galletas
stock_2 = 18
precio_2 = 600

producto_3 = Barritas
stock_3 = 30
precio_3 = 850

valor_total = (stock_1 * precio_1) + (stock_2 * precio_2) + (stock_3 * precio_3)

# Escribe aquí los print() para mostrar el reporte

print(📦 INVENTARIO DEL KIOSCO)
print(Producto, Stock, Precio, sep= | )
print(Jugos", 24, $750, sep= | )
print(Galletas, 18, $600, sep= | )
print(Barritas, 30, $850, sep= | )
print(Valor total del inventario: , $, 54300)
```

---

## Ejercicio 3 — Tarjeta de transporte ⭐⭐ (15 pts)

Escribe un programa que simule los siguientes movimientos de una tarjeta de transporte:

1. Saldo inicial: $12.000
2. Recarga de la mañana: +$5.300
3. Viaje al liceo: -$850
4. Compra de colación: -$1.500
5. Recarga de la tarde: +$3.000
6. Viaje de regreso: -$850

**Regla obligatoria:** debes usar **una sola variable de saldo** que se va actualizando paso a paso. Puedes usar la forma corta (`variable += valor`, `variable -= valor`) o la forma larga (`variable = variable + valor`, `variable = variable - valor`), pero siempre debe ser **la misma variable**. No uses una variable distinta para cada movimiento.

**El programa debe imprimir con `print()`:**

> El bloque destinado a la salida esperada aparece vacío en la fotografía.

### Código visible en la celda

```python
# Ejercicio 3 — Tarjeta de transporte
# Escribe tu código aquí

print(📦 INVENTARIO DEL KIOSCO)
print(Producto, Stock, Precio, sep= | )
print(Jugos", 24, $750", sep= | )
print(Galletas, 18, $600, sep= | )
print(Barritas, 30, $850, sep= | )
print(Valor total del inventario:, $, 54300)
```

---

## Ejercicio 4 — Recargo por servicio ⭐⭐ (15 pts)

**El programa debe pedir con `input()`:**

- El precio base de una compra
- El porcentaje de recargo por servicio

**El programa debe imprimir con `print()`:**

```text
--- RESUMEN DEL RECARGO ---
Precio base: $ 18000.0
Recargo (10%): $ 1800.0
Precio final: $ 19800.0
```

### Código visible en la celda

```python
# Ejercicio 4 — Recargo por servicio
# Escribe tu código aquí

precio_base = float(input(Ingrese el precio base de la compra: ))
porcentaje = float(input(Ingrese el porcentaje de recargo por servicio: ))

recargo = precio_base * porcentaje / 100
precio_final = precio_base + recargo

print(--- RESUMEN DEL RECARGO ---)
print(Precio base: $, precio_base)
print(fRecargo ({porcentaje}%): $, recargo)
print(Precio final: $, precio_final)
```

### Texto adicional visible debajo de la celda

```text
precio_base = float(input("Ingrese el precio base: ")) porcentaje = float(input("Ingrese el porcentaje de recargo: "))

recargo = precio_base * porcentaje / 100 precio_final = precio_base + recargo

print("--- RESUMEN DEL RECARGO ---") print("Precio base: ", precio_base) print("Recargo(" + str(porcentaje) + "%", recargo) print("Precio fi...
```

> La última línea está cortada a la derecha en las fotografías.

---

## Ejercicio 5

> No aparece en ninguna de las fotografías proporcionadas.

---

## Ejercicio 6 — Depurar cálculo de promedio ponderado ⭐⭐ (15 pts)

El siguiente programa tiene **5 errores**. Encuéntralos y corrígelos sin cambiar los valores.

**El programa debe imprimir con `print()`:**

```text
📋 PROMEDIO PONDERADO DEL TALLER
Ejercicios (40%): 6.0
Desafío (25%): 5.4
Bitácora (20%): 6.8
Participación (15%): 6.4
Promedio final: 6.07
```

Verificación: 6.0×0.40 + 5.4×0.25 + 6.8×0.20 + 6.4×0.15 = 6.07

### Código visible en la celda

```python
# Ejercicio 6 — Depurar cálculo de promedio ponderado
# Este código tiene 5 errores. Corrígelos sin cambiar los valores.

nota ejercicios = 6.0
nota_desafio = 5.4
    nota_bitacora = 6.8
nota_participacion = 6.4

promedio_final = (nota_ejercicios * 0.40) + (nota_desafio + 0.25) + (notabitacora * 0.20) + (nota_participacion * 0.15)

print(📋 PROMEDIO PONDERADO DEL TALLER)
print(Ejercicios (40%):, nota_ejercicios)
print(Desafío (25%):, nota_desafio)
print(Bitácora (20%):, nota_bitacora)
print(Participación (15%)nota_participacion)
print(Promedio final:, promedio_final)
```

---

## Ejercicio 7 — Registro semanal de estudio ⭐⭐⭐ (20 pts)

**El programa debe pedir con `input()`:**

- La meta semanal de minutos de estudio
- Los minutos estudiados el lunes
- Los minutos estudiados el martes
- Los minutos estudiados el miércoles
- Los minutos estudiados el jueves
- Los minutos estudiados el viernes

**El programa debe imprimir con `print()`:**

```text
--- RESUMEN DE ESTUDIO ---
Meta semanal: 300 minutos
Total estudiado: 255 minutos
Minutos faltantes: 45
Porcentaje de avance: 85.0 %
```

### Código visible en la celda

```python
# Ejercicio 7 — Registro semanal de estudio
# Escribe tu código aquí
meta_semanal = int(input(Ingrese la meta semanal de minutos de estudio: ))
lunes = int(input(Minutos estudiados el lunes: ))
martes = int(input(Minutos estudiados el martes: ))
miercoles = int(input(Minutos estudiados el miércoles: ))
jueves = int(input(Minutos estudiados el jueves: ))
viernes = int(input(Minutos estudiados el viernes: ))

total_estudiado = lunes + martes + miercoles + jueves + viernes

minutos_faltantes = meta_semanal - total_estudiado

porcentaje = (total_estudiado / meta_semanal) * 100

print(\n--- RESUMEN DE ESTUDIO ---)
print(Meta semanal:, meta_semanal, minutos)
print(Total estudiado:, total_estudiado, minutos)
print(Minutos faltantes:, minutos_faltantes)
print(Porcentaje de avance:, porcentaje, %)
```

---

## Partes no recuperables con estas fotografías

- Encabezado general e instrucciones iniciales de la evaluación.
- Encabezado completo y puntaje del ejercicio 1.
- Enunciado y salida esperada completa del ejercicio 2.
- Salida esperada del ejercicio 3.
- Todo el ejercicio 5.
- Cualquier contenido posterior a la celda del ejercicio 7.
