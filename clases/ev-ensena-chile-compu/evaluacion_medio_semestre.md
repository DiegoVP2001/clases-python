# Banco de Preguntas - Evaluación Final de Medio Semestre
## Pensamiento Computacional y Programación (4° Medio)

Este archivo contiene el banco de 20 preguntas estructuradas para la evaluación final de medio semestre, conforme a los requisitos metodológicos y al formato establecido.

---

pregunta 1

¿Cuál es el tipo de dato en Python más adecuado para almacenar si un estudiante asistió (`True`) o no asistió (`False`) a su clase de Pensamiento Computacional?
str
float
int
bool
Respuesta: bool
OA: OA2 - IND-CS-2.1
Dificultad: facil

pregunta 2

Queremos guardar el saldo disponible en pesos chilenos de una tarjeta Bip! (por ejemplo, 2500 o 800) en una variable llamada `saldo_bip`. ¿Qué tipo de dato es el más adecuado en Python para representar este saldo de forma precisa?
bool
int
float
str
Respuesta: int
OA: OA2 - IND-CS-2.1
Dificultad: facil

pregunta 3

Un estudiante quiere ingresar su promedio final de Tecnología por teclado para saber si es eximido de examen. ¿Cuál de las siguientes líneas de código Python captura correctamente este promedio decimal desde el teclado?
`promedio = input(float("Ingresa tu promedio: "))`
`promedio = float(input("Ingresa tu promedio: "))`
`promedio = float(print("Ingresa tu promedio: "))`
`promedio = int(input("Ingresa tu promedio: "))`
Respuesta: `promedio = float(input("Ingresa tu promedio: "))`
OA: OA2 - IND-CS-2.2
Dificultad: facil

pregunta 4

Para registrar a los alumnos participantes en un torneo de fútbol escolar, necesitamos solicitar su edad por teclado como número entero. ¿Qué opción realiza esta captura correctamente en Python?
`edad = int(input("Ingresa tu edad: "))`
`edad = float(input("Ingresa tu edad: "))`
`edad = input("Ingresa tu edad: ")`
`edad = int("Ingresa tu edad: ")`
Respuesta: `edad = int(input("Ingresa tu edad: "))`
OA: OA2 - IND-CS-2.2
Dificultad: facil

pregunta 5

En un videojuego, un jugador tiene 1500 puntos en la variable `puntos` y el valor `True` en la variable `tiene_pase`. Evaluamos la siguiente condición:
`puntos >= 1000 and tiene_pase`
¿Qué valor produce esta expresión al ser evaluada en Python?
True
False
1500
Error de sintaxis
Respuesta: True
OA: OAd - IND-CS-d.1
Dificultad: facil

pregunta 6

Analiza el siguiente bloque de código en Python:
```python
saldo_bip = 700
costo_pasaje = 730

if saldo_bip >= costo_pasaje:
    print("Viaje autorizado")
else:
    print("Saldo insuficiente")
```
¿Qué texto se mostrará en la pantalla al ejecutar este código?
Viaje autorizado
Saldo insuficiente
No se muestra nada
Error de sintaxis
Respuesta: Saldo insuficiente
OA: OA3 - IND-CS-3.1
Dificultad: facil

pregunta 7

Deseamos crear un programa que pida dos notas de tareas por teclado (que pueden ser decimales), calcule su promedio y lo muestre en pantalla con un mensaje descriptivo. ¿Cuál de los siguientes fragmentos de código realiza esta tarea de manera correcta y robusta?
```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
promedio = (nota1 + nota2) / 2
print("Tu promedio es: " + promedio)
```
```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
promedio = (nota1 + nota2) / 2
print("Tu promedio es:", promedio)
```
```python
nota1 = input("Nota 1: ")
nota2 = input("Nota 2: ")
promedio = (int(nota1) + int(nota2)) / 2
print("Tu promedio es:", promedio)
```
```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
promedio = nota1 + nota2 / 2
print("Tu promedio es:", promedio)
```
Respuesta:
```python
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
promedio = (nota1 + nota2) / 2
print("Tu promedio es:", promedio)
```
OA: OA2 - IND-CS-2.2
Dificultad: medio

pregunta 8

Queremos simular la boletería de un cine escolar. El programa solicita la cantidad de entradas que el usuario desea comprar (número entero) y calcula el costo total sabiendo que cada entrada cuesta 2500 pesos. ¿Cuál es el código correcto para capturar y mostrar esta información?
```python
cantidad = input("¿Cuántas entradas quieres? ")
total = cantidad * 2500
print("El total a pagar es:", total)
```
```python
cantidad = int(input("¿Cuántas entradas quieres? "))
total = cantidad * 2500
print("El total a pagar es:", total)
```
```python
cantidad = float(input("¿Cuántas entradas quieres? "))
total = cantidad + 2500
print("El total a pagar es: " + total)
```
```python
cantidad = int(input("¿Cuántas entradas quieres? "))
total = cantidad * "2500"
print("El total a pagar es:", total)
```
Respuesta:
```python
cantidad = int(input("¿Cuántas entradas quieres? "))
total = cantidad * 2500
print("El total a pagar es:", total)
```
OA: OA2 - IND-CS-2.2
Dificultad: medio

pregunta 9

Considera las variables `edad = 14` y `tiene_permiso = False`. Evaluamos la siguiente condición en un sistema de registro de un videojuego en línea:
`edad >= 18 or (edad >= 12 and tiene_permiso)`
¿Cuál es el resultado de evaluar esta expresión lógica en Python?
True
False
Error de sintaxis
None
Respuesta: False
OA: OAd - IND-CS-d.1
Dificultad: medio

pregunta 10

Para aprobar un curso escolar, las reglas indican que un alumno debe tener un promedio mayor o igual a 4.0 y una asistencia mayor o igual al 85%, O BIEN tener un promedio mayor o igual a 6.0 sin importar la asistencia. Si un alumno tiene `promedio = 5.2` y `asistencia = 80`, ¿cuál es el resultado de evaluar la siguiente condición?
`(promedio >= 4.0 and asistencia >= 85) or promedio >= 6.0`
True
False
80
Error de tipo (TypeError)
Respuesta: False
OA: OAd - IND-CS-d.1
Dificultad: medio

pregunta 11

Analiza el siguiente código Python:
```python
edad = 16

if edad >= 18:
    print("Entrada General")
else:
    print("Requiere Acompañante Adulto")
```
¿Cuál es el resultado que se muestra en consola al ejecutar este fragmento de código?
Entrada General
Requiere Acompañante Adulto
No se imprime nada
Ambos mensajes se imprimen
Respuesta: Requiere Acompañante Adulto
OA: OA3 - IND-CS-3.1
Dificultad: medio

pregunta 12

Se ejecuta el siguiente código en un punto de venta interactivo:
```python
es_estudiante = True
total = 5000

if es_estudiante:
    total = total - 1000
else:
    total = total - 200

print("Total final:", total)
```
¿Qué valor se imprimirá para `total` al final de la ejecución?
Total final: 5000
Total final: 4800
Total final: 4000
Total final: 3800
Respuesta: Total final: 4000
OA: OA3 - IND-CS-3.1
Dificultad: medio

pregunta 13

Analiza el flujo del siguiente código con condicionales anidados:
```python
paga_suscripcion = True
calidad_hd = False

if paga_suscripcion:
    if calidad_hd:
        print("Plan Premium")
    else:
        print("Plan Estándar")
else:
    print("Plan Básico con anuncios")
```
¿Qué mensaje se mostrará en pantalla al ejecutar este programa?
Plan Premium
Plan Estándar
Plan Básico con anuncios
Error: No se puede tener un if dentro de otro if
Respuesta: Plan Estándar
OA: OA1 - IND-CS-1.1
Dificultad: medio

pregunta 14

Un profesor usa el siguiente código con la estructura `elif` para asignar conceptos a las calificaciones de sus estudiantes:
```python
puntaje = 65

if puntaje >= 80:
    print("Excelente")
elif puntaje >= 60:
    print("Aprobado")
elif puntaje >= 40:
    print("Suficiente")
else:
    print("Insuficiente")
```
¿Qué concepto imprimirá el programa para un alumno que obtuvo 65 puntos?
Excelente
Aprobado
Suficiente
Aprobado y Suficiente
Respuesta: Aprobado
OA: OA1 - IND-CS-1.1
Dificultad: medio

pregunta 15

Un estudiante intenta programar un aviso para saber si tiene exactamente nota 4.0 en su tarea de Pensamiento Computacional, y escribe lo siguiente:
```python
nota = 4.0
if nota = 4.0:
    print("Aprobado justo")
```
Al ejecutar este código en Python, el programa genera un error. ¿Por qué ocurre este error?
Porque falta una sentencia `else`.
Porque el bloque de `print` no está indentado.
Porque para comparar igualdad se debe usar el operador `==` en lugar de `=`.
Porque el valor decimal `4.0` debe escribirse entre comillas dobles.
Respuesta: Porque para comparar igualdad se debe usar el operador `==` en lugar de `=`.
OA: OA3 - IND-CS-3.2
Dificultad: medio

pregunta 16

Revisa el siguiente código escrito por un estudiante para verificar el saldo de la tarjeta Bip!:
```python
saldo_bip = 800
if saldo_bip < 730:
print("Saldo insuficiente")
else:
print("Viaje permitido")
```
¿Cuál es el error en este fragmento de código?
Falta un paréntesis en la expresión `if saldo_bip < 730`.
El operador `<` no se puede utilizar para comparar una variable con un número entero.
Las sentencias dentro de los bloques `if` y `else` no tienen la indentación (sangría) obligatoria en Python.
Las condiciones de tipo `if` y `else` deben estar escritas completamente en una sola línea.
Respuesta: Las sentencias dentro de los bloques `if` y `else` no tienen la indentación (sangría) obligatoria en Python.
OA: OA3 - IND-CS-3.2
Dificultad: medio

pregunta 17

Considera la siguiente expresión lógica compleja utilizada para determinar si un estudiante que faltó a clases puede rendir una prueba recuperativa:
`not (promedio >= 4.0) and (asistencia < 85 and justificado)`
Si definimos las variables de la siguiente manera:
`promedio = 3.8`
`asistencia = 82`
`justificado = True`
¿Cuál es el resultado de evaluar esta expresión lógica completa en Python?
True
False
Error de sintaxis
Error de tipo (TypeError)
Respuesta: True
OA: OAd - IND-CS-d.1
Dificultad: dificil

pregunta 18

Analiza el siguiente fragmento de código que clasifica a un jugador de eSports según su puntaje acumulado:
```python
puntos_clasificatoria = 85

if puntos_clasificatoria >= 80:
    print("Oro")
if puntos_clasificatoria >= 60:
    print("Plata")
if puntos_clasificatoria >= 40:
    print("Bronce")
else:
    print("Sin categoría")
```
¿Qué salidas consecutivas se imprimirán en la consola cuando se ejecute este código?
Solo se imprime: Oro
Se imprimen: Oro y Plata
Se imprimen: Oro, Plata y Bronce
Se imprimen: Oro, Plata y Sin categoría
Respuesta: Se imprimen: Oro, Plata y Bronce
OA: OA3 - IND-CS-3.1
Dificultad: dificil

pregunta 19

Estudia detalladamente el flujo lógico de la siguiente estructura condicional anidada que ajusta el precio de una entrada al parque de diversiones según el día de la semana y la edad del visitante:
```python
dia = "sabado"
edad = 15
precio = 4000

if dia == "sabado" or dia == "domingo":
    if edad < 12:
        precio = precio * 0.5
    elif edad < 18:
        precio = precio * 0.8
    else:
        precio = precio
else:
    if edad < 18:
        precio = precio * 0.6
    else:
        precio = precio * 0.9

print("Precio final:", precio)
```
¿Cuál será la salida que mostrará la consola al ejecutar el programa con los valores dados?
Precio final: 2000.0
Precio final: 3200.0
Precio final: 2400.0
Precio final: 4000
Respuesta: Precio final: 3200.0
OA: OA1 - IND-CS-1.1
Dificultad: dificil

pregunta 20

Considera el siguiente fragmento de código Python que aplica descuentos complejos en una boletería escolar de teatro interactiva:
```python
tipo_entrada = "estudiante"
codigo_descuento = "DESCUENTO10"
total = 10000

if tipo_entrada == "estudiante":
    total = total - 3000
    if codigo_descuento == "DESCUENTO10":
        total = total * 0.9
    elif codigo_descuento == "PROMO15":
        total = total * 0.85
elif tipo_entrada == "general":
    if codigo_descuento == "DESCUENTO10":
        total = total * 0.9
else:
    total = total

print("Monto a pagar:", total)
```
¿Cuál será el valor impreso para el monto a pagar después de ejecutar este código?
Monto a pagar: 7000
Monto a pagar: 6300.0
Monto a pagar: 9000.0
Monto a pagar: 5950.0
Respuesta: Monto a pagar: 6300.0
OA: OA1 - IND-CS-1.1
Dificultad: dificil
