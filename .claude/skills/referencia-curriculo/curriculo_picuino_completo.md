# Síntesis estructurada del Tutorial de Python de Picuino — clases 1 a 33

**Propósito:** documento de trabajo docente que recupera la progresión, conceptos, sintaxis y actividades de las clases 1 a 33 del Tutorial de Python de Picuino.

**Nota de uso:** no es una reproducción literal completa del sitio. Es una síntesis estructurada y atribuida, pensada para planificación, adaptación curricular y diseño de clases.

**Fuente base:** Picuino, Tutorial de Python, Carlos Félix Pardo Martín. Contenidos bajo licencia CC BY-SA 4.0 y software bajo GPL v3, salvo indicación contraria.

## Mapa general de progresión

| Clase | Tema | Foco | Herramientas clave | Actividades recuperadas |
|---:|---|---|---|---|
| 1 | Introducción al lenguaje Python | Lenguajes de programación, usos de Python y primeros pasos en IDLE. | Operaciones directas en consola: 5 + 16., Archivo .py guardado y ejecutado desde IDLE. | Abrir IDLE.; Ejecutar operaciones simples en modo interactivo.; Crear una macro, guardarla y ejecutarla.; Responder entradas que el programa solicite. |
| 2 | Datos numéricos | Tipos numéricos y operatoria básica con enteros y flotantes. | +  -  *  //  %  **  /, round(numero, decimales), int(n), float(n), import math; math.gcd(a, b) | Sumar distancias.; Calcular el cuadrado de 55.; Calcular y redondear una media.; Obtener restos con módulo. |
| 3 | Las variables | Asignación de valores, nombres de variables y eliminación de números mágicos. | pi = 3.1415927, altura = 176, persona_altura = 175 | Calcular perímetro de un círculo.; Calcular sueldo según horas y tarifa.; Calcular volumen de un cubo.; Calcular cambio de una compra. |
| 4 | Palabras reservadas | Palabras reservadas, funciones integradas y sensibilidad a mayúsculas/minúsculas. | False, None, True, and, or, not, if, elif, else, for, while, def, return, import | Nombrar variables para edad, altura, peso y nombre sin usar palabras reservadas.; Investigar funciones integradas: abs(), sum(), max(), min(). |
| 5 | Los comentarios | Uso de comentarios con # y criterio para comentar código. | # Esto es un comentario, 5  # comentario al final de una línea | Reconocer comentarios ignorados por el intérprete.; Distinguir entre comentario útil y comentario redundante. |
| 6 | La función print() | Salida por pantalla y parámetros sep/end. | print('Hola, mundo'), print(1, 2, 3, sep=' + '), print('Hola,', end=' '); print('mundo') | Imprimir números separados por punto y coma.; Imprimir dos palabras en una misma línea usando dos print.; Calcular e imprimir media de tres notas.; Usar \n para salto de línea. |
| 7 | La función input() | Entrada por teclado y conversión de datos ingresados. | nombre = input('Escribe tu nombre: '), num = int(input('Escribe un número: ')), float(num) | Pedir dos números e imprimir la suma.; Pedir nombre y saludar de forma personalizada.; Pedir dos números y calcular máximo común divisor usando math.gcd(). |
| 8 | El tipo Booleano | Valores True/False, comparaciones y lógica booleana. | 1 == 1, 5 > 8, True and False, bool(0), bool(1) | Evaluar comparaciones numéricas y de cadenas.; Explorar tablas de verdad con and/or/not.; Probar bool() con cero, positivos y negativos. |
| 9 | Sentencia if else | Control de flujo condicional e indentación obligatoria. | if edad >= 18:,     print('Mayor de edad'), else:,     print('Menor de edad') | Número positivo o negativo.; Número par o impar.; Comparar dos números.; Comprobar una condición True/False. |
| 10 | Operadores and, or, not | Condiciones compuestas en estructuras if. | if (altura >= 150) and (altura <= 200):, if not (num % 2 == 0):, if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)): | Detectar meses de primavera.; Modificar condición de par a impar usando not.; Validar longitud de nombre entre 4 y 6 letras.; Controlar riego según sensores de lluvia y día. |
| 11 | Sentencias if anidadas | Condicionales dentro de condicionales y decisiones jerárquicas. | if numero % 3 == 0:,     if numero % 5 == 0:,         print(...) | Precio de cine según edad.; Acceso a atracciones según altura y edad.; Clasificación de nota.; Diagnóstico de reparación con preguntas sí/no. |
| 12 | Sentencia elif | Evaluación de múltiples condiciones sin anidamiento excesivo. | if nota < 5:, elif nota < 6:, elif nota < 7:, else: | Clasificar entero como positivo, negativo o cero.; Traducir mes numérico a estación.; Validar rango de nota.; Verificar si un número entre 1 y 10 es primo y explicar divisibilidad. |
| 13 | Sentencia for | Bucles definidos con variable iteradora sobre rango o lista. | for num in range(1, 10):, for nombre in ['Abel', 'Beatriz']:, suma = suma + i | Tabla del 6.; Suma desde 1 hasta n.; Factorial.; Edades de 15 a 20 con mayoría de edad. |
| 14 | La función range() | Generación de secuencias numéricas para bucles. | range(2, 20, 3), range(100, 0, -10), range(5, 11), range(6) | Imprimir pares de 2 a 20.; Imprimir impares de 1 a 19.; Cuenta atrás de 10 a 0.; Listados descendentes de 50 a 20 y de -50 a -20. |
| 15 | Sentencia continue | Saltar una iteración y continuar con el siguiente elemento del bucle. | if num % 3 == 0:,     continue, print(num) | Imprimir 1 a 20 excepto múltiplos de 5.; Imprimir 1 a 10 excepto 4 y 7.; Sumar 1 a 100 excepto múltiplos de 3.; Contar números quitando múltiplos de 3 y 7. |
| 16 | Sentencia break | Interrupción anticipada de bucles y uso de for/else. | if num == 5:,     break, for ...:,     ... | Cuenta atrás detenida en 5.; Contraseña con máximo 4 intentos.; Imprimir frase hasta letra 30.; Sumar hasta superar 1000. |
| 17 | Sentencias for anidadas | Bucles dentro de bucles para construir tablas y patrones. | for i in range(1, 11):,     for j in range(1, 11):,         print(i*j, end='\t') | Determinar si un número es producto de dos números de 1 a 10.; Dibujar triángulo de asteriscos.; Dibujar triángulo de números.; Dibujar triángulo invertido. |
| 18 | Sentencia while | Bucles condicionados cuando no se sabe de antemano la cantidad de repeticiones. | while suma < 1000:, while True:,     if nombre == 'fin':,         break | Imprimir 0 a 10.; Imprimir 10 a 0.; Sumar enteros hasta llegar a 1000.; Repetir hasta que la respuesta sea n. |
| 19 | Definición de funciones | Crear bloques reutilizables con def, parámetros y return. | def mensaje():, def saludo(nombre):, def suma(a, b):,     return a + b | Función par/impar.; Función mayor(a,b).; Conversión Celsius a Fahrenheit.; Función factorial. |
| 20 | Parámetros con valores por omisión | Argumentos opcionales y diseño de funciones reutilizables. | def saludo(nombre='María'):, def reemplaza_vocales(texto, vocal='e'): | Contar múltiplos desde 1 hasta tope.; Agregar tope por defecto igual a 100.; Contar vocales en una cadena.; Imprimir el menor de tres números. |
| 21 | Cadenas de texto | Manipulación básica de strings, escapes, Unicode y cadenas multilínea. | 'Hola, mundo', 'doesn\'t', print("""texto multilínea"""), 'Hola, ' + 'mundo' | Crear texto con caracteres especiales.; Dibujar recuadro doble multilínea.; Crear función que imprima tabla 2x2 con docstring.; Leer cadena e imprimir cantidad de caracteres. |
| 22 | Índices de cadenas de texto | Acceso, rebanadas e iteración de caracteres. | lang[0], lang[-1], lang[0:3], lang[:3] | Función deletrea sin índices.; Función deletrea con índices.; Impresión progresiva de una cadena desde la izquierda.; Impresión progresiva desde la derecha. |
| 23 | Métodos de cadenas de texto | Métodos asociados a strings y búsqueda de subcadenas. | 'PaLaBrA'.upper(), cadena.find('lugar'), 'Hola nombre'.replace('nombre','Miguel'), 'hola' in 'Hola, mundo'.lower() | Alternar mayúsculas y minúsculas letra por letra.; Mayúsculas en índices múltiplos de 3.; Detector de palabras tabú en descripción de Lionel Messi.; Función para reemplazar vocales por una vocal configurable. |
| 24 | Formateo de cadenas de texto | f-strings y formatos numéricos/textuales. | f'El creador de Python es {nombre} {apellido}', f'{num:03d}', f'{nombre:>20}', f'{pi:10.3f}' | Alinear nombre a derecha, izquierda y centro.; Formatear enteros en decimal, con signo, hexadecimal y binario.; Formatear flotantes con decimales, ceros y notación científica.; Explorar caracteres Unicode. |
| 25 | Listas | Estructuras ordenadas de datos y operaciones básicas. | lista_impares = [1, 3, 5, 7, 9], nombre_y_altura = [['Juan', 176], ['Nerea', 169]], [1,2,3] + [4,5,6], 3 in lista | Lista de cinco compañeros/as o amigos/as.; Lista de edades y lista anidada.; Lista multilínea con frases famosas.; Lista de los 10 primeros primos en dos partes. |
| 26 | Índices de listas | Acceso, rebanadas, modificación y eliminación de elementos en listas. | lista[0], lista[-1], lista[1:-1], lista[0] = 'A' | Imprimir primer, tercer y séptimo primo.; Sumar los 4 primeros primos con bucle por índices.; Modificar el segundo nombre de una lista.; Imprimir sublistas del abecedario. |
| 27 | Iteración de listas | Recorrer listas y generar listas nuevas. | for nombre in lista:, for i in range(len(lista)):, list(range(10)), list('Hola, mundo') | Imprimir nombres y letra inicial.; Leer frase y mostrarla al revés.; Generar impares hasta 99 y sumar 2500.; Eliminar duplicados construyendo lista nueva. |
| 28 | Métodos de listas | Métodos y funciones frecuentes para manipular listas. | lista.append(6), lista.pop(), lista.pop(0), lista.index(4) | Función promedio de una lista.; Función que retorna solo números pares.; Función resumen que retorne mínimo, máximo, cantidad y suma. |
| 29 | Búsqueda de datos | Búsqueda lineal implementada manualmente. | def busca_menor(lista):, menor = 0, for i in range(len(lista)):,     if lista[i] < lista[menor]: | Buscar elemento mayor.; Devolver posición del último par o None.; Devolver posición del primer impar o None.; Contar apariciones de un elemento. |
| 30 | Búsqueda binaria | Algoritmo eficiente de búsqueda sobre listas ordenadas. | inicio = 0, final = len(lista) - 1, medio = (inicio + final) // 2, if lista[medio] == buscado: | Programar función que retorne la posición donde insertar un nuevo número en una lista ordenada.; Probar inserciones con 7, 25, 48, 68 y 100. |
| 31 | Desplazamiento de datos | Movimiento de datos en memoria/listas: intercambio y desplazamientos. | temp = bajo; bajo = alto; alto = temp, for i in range(final, 0, -1): lista[i] = lista[i-1], for i in range(final): lista[i] = lista[i+1] | Intercambiar dos variables.; Intercambiar tres variables hasta que coincidan con sus nombres.; Función desplaza_izquierda(lista, nuevo_valor).; Función desplaza_derecha(lista, min). |
| 32 | Ordenación por selección | Ordenamiento seleccionando repetidamente el menor elemento. | def busca_menor(lista, final):, for final in range(len(lista)-1):, temp = lista[final], desplaza_derecha(lista, comienzo, menor) | Reescribir ordenación I de mayor a menor.; Reescribir ordenación II comenzando por la derecha.; Mover todos los ceros de una lista a la izquierda manteniendo orden del resto.; Ordenar cadenas por longitud. |
| 33 | Ordenación por inserción | Ordenamiento insertando cada elemento en una sublista ya ordenada. | def inserta_elemento(lista, index):, for i in range(index, 0, -1):, if lista[i-1] > lista[i]:, while primero <= ultimo: | Ordenar lista de tres elementos sin bucles, solo if.; Reescribir ordenación descendente.; Reescribir todo en una sola función.; Ordenar cadenas por longitud. |

## Fichas por clase

### 1. Introducción al lenguaje Python

**URL:** https://www.picuino.com/es/python-intro.html

**Foco:** Lenguajes de programación, usos de Python y primeros pasos en IDLE.

**Conceptos recuperados:**
- Qué es un lenguaje de programación y para qué se usa.
- Python como lenguaje accesible para web, datos, IA y robótica.
- Entorno IDLE: consola interactiva, órdenes inmediatas y resultados.
- Macros o archivos .py: escribir, guardar y ejecutar programas con Run/F5.
**Sintaxis / herramientas:**
- `Operaciones directas en consola: 5 + 16.`
- `Archivo .py guardado y ejecutado desde IDLE.`
**Actividades o ejercicios recuperados:**
- Abrir IDLE.
- Ejecutar operaciones simples en modo interactivo.
- Crear una macro, guardarla y ejecutarla.
- Responder entradas que el programa solicite.
**Uso pedagógico sugerido:** Sirve como clase de instalación, orientación y cultura de programación. Conviene transformar IDLE por Google Colab si el contexto escolar trabaja en navegador.

### 2. Datos numéricos

**URL:** https://www.picuino.com/es/python-datos-numeros.html

**Foco:** Tipos numéricos y operatoria básica con enteros y flotantes.

**Conceptos recuperados:**
- Tipos int y float; complex se menciona pero no se aborda.
- Uso del punto decimal en Python, no coma decimal.
- Operaciones con enteros: suma, resta, multiplicación, división entera, módulo y potencia.
- Operaciones con flotantes: división decimal, módulo, potencia y redondeo.
- Errores de representación de números flotantes.
- Conversión entre tipos con int() y float().
- Uso inicial de la librería math, con ejemplo de máximo común divisor.
**Sintaxis / herramientas:**
- `+  -  *  //  %  **  /`
- `round(numero, decimales)`
- `int(n), float(n)`
- `import math; math.gcd(a, b)`
**Actividades o ejercicios recuperados:**
- Sumar distancias.
- Calcular el cuadrado de 55.
- Calcular y redondear una media.
- Obtener restos con módulo.
- Buscar el siguiente número posterior a 80 divisible por 7.
**Uso pedagógico sugerido:** Es una buena base para problemas de cálculo contextualizados. En aula chilena conviene explicitar la diferencia entre coma decimal cultural y punto decimal en código.

### 3. Las variables

**URL:** https://www.picuino.com/es/python-variables.html

**Foco:** Asignación de valores, nombres de variables y eliminación de números mágicos.

**Conceptos recuperados:**
- Variable como contenedor con nombre descriptivo.
- Asignación mediante nombre = valor.
- El valor de una variable puede mantenerse o cambiar.
- Números mágicos y uso de variables para mejorar legibilidad.
- Reglas de nombres: significativos, cortos, sin caracteres especiales, snake_case, no palabras reservadas.
**Sintaxis / herramientas:**
- `pi = 3.1415927`
- `altura = 176`
- `persona_altura = 175`
**Actividades o ejercicios recuperados:**
- Calcular perímetro de un círculo.
- Calcular sueldo según horas y tarifa.
- Calcular volumen de un cubo.
- Calcular cambio de una compra.
- Aplicar descuento del 25%.
**Uso pedagógico sugerido:** Clave para enseñar legibilidad. Permite instalar desde el inicio una norma de estilo: nombres claros, snake_case y variables para datos relevantes.

### 4. Palabras reservadas

**URL:** https://www.picuino.com/es/python-palabras-reservadas.html

**Foco:** Palabras reservadas, funciones integradas y sensibilidad a mayúsculas/minúsculas.

**Conceptos recuperados:**
- Las palabras reservadas tienen significado propio y no pueden usarse como nombres.
- Python tiene palabras como False, None, True, and, break, class, def, elif, else, for, if, import, not, or, return, while, etc.
- Las funciones integradas no son palabras reservadas, pero tampoco conviene usarlas como nombres.
- Python distingue mayúsculas y minúsculas: False no es lo mismo que false.
- Evitar variables que solo cambian por mayúsculas, por legibilidad y mantención.
**Sintaxis / herramientas:**
- `False, None, True`
- `and, or, not`
- `if, elif, else, for, while`
- `def, return, import`
**Actividades o ejercicios recuperados:**
- Nombrar variables para edad, altura, peso y nombre sin usar palabras reservadas.
- Investigar funciones integradas: abs(), sum(), max(), min().
**Uso pedagógico sugerido:** Conviene usar esta clase como verificación de errores típicos: nombres inválidos, mayúsculas incorrectas y sobrescritura accidental de funciones.

### 5. Los comentarios

**URL:** https://www.picuino.com/es/python-comentarios.html

**Foco:** Uso de comentarios con # y criterio para comentar código.

**Conceptos recuperados:**
- Los comentarios explican el funcionamiento del programa.
- El intérprete ignora los comentarios.
- En Python comienzan con #.
- El código debe explicarse principalmente por nombres claros y buena organización.
- Los comentarios se recomiendan para explicaciones que no puedan expresarse de otra manera.
**Sintaxis / herramientas:**
- `# Esto es un comentario`
- `5  # comentario al final de una línea`
**Actividades o ejercicios recuperados:**
- Reconocer comentarios ignorados por el intérprete.
- Distinguir entre comentario útil y comentario redundante.
**Uso pedagógico sugerido:** Útil para instalar una regla de calidad: comentar la intención o una decisión, no traducir línea por línea lo que el código ya dice.

### 6. La función print()

**URL:** https://www.picuino.com/es/python-print.html

**Foco:** Salida por pantalla y parámetros sep/end.

**Conceptos recuperados:**
- print() imprime textos, números y objetos.
- Es útil para mostrar información y depurar programas.
- sep define el separador entre objetos impresos.
- end define el carácter final; por defecto es salto de línea.
- Se pueden concatenar varias órdenes en una línea con ;, aunque pedagógicamente conviene usarlo con cuidado.
**Sintaxis / herramientas:**
- `print('Hola, mundo')`
- `print(1, 2, 3, sep=' + ')`
- `print('Hola,', end=' '); print('mundo')`
**Actividades o ejercicios recuperados:**
- Imprimir números separados por punto y coma.
- Imprimir dos palabras en una misma línea usando dos print.
- Calcular e imprimir media de tres notas.
- Usar \n para salto de línea.
- Imprimir valores de variables y suma de dos variables.
**Uso pedagógico sugerido:** Muy apropiada para una clase inicial en Colab: resultados visibles inmediatos y conexión con depuración.

### 7. La función input()

**URL:** https://www.picuino.com/es/python-input.html

**Foco:** Entrada por teclado y conversión de datos ingresados.

**Conceptos recuperados:**
- input(prompt) muestra un mensaje y devuelve texto ingresado por el usuario.
- Puede detener la ejecución hasta presionar Enter.
- Todo valor ingresado por input() llega como cadena de texto.
- Para calcular, se debe convertir con int() o float().
**Sintaxis / herramientas:**
- `nombre = input('Escribe tu nombre: ')`
- `num = int(input('Escribe un número: '))`
- `float(num)`
**Actividades o ejercicios recuperados:**
- Pedir dos números e imprimir la suma.
- Pedir nombre y saludar de forma personalizada.
- Pedir dos números y calcular máximo común divisor usando math.gcd().
**Uso pedagógico sugerido:** Conectar de inmediato input + conversión + print. Es donde suelen aparecer errores por intentar sumar textos en vez de números.

### 8. El tipo Booleano

**URL:** https://www.picuino.com/es/python-booleanos.html

**Foco:** Valores True/False, comparaciones y lógica booleana.

**Conceptos recuperados:**
- Booleano representa verdadero o falso.
- True y False se escriben con inicial mayúscula.
- Las comparaciones devuelven valores booleanos.
- Operadores de comparación: ==, !=, >, <, >=, <=.
- Operadores lógicos: and, or, not.
- bool() convierte valores a su evaluación booleana.
**Sintaxis / herramientas:**
- `1 == 1`
- `5 > 8`
- `True and False`
- `bool(0), bool(1)`
**Actividades o ejercicios recuperados:**
- Evaluar comparaciones numéricas y de cadenas.
- Explorar tablas de verdad con and/or/not.
- Probar bool() con cero, positivos y negativos.
**Uso pedagógico sugerido:** Es prerequisito directo para condicionales. Conviene trabajarlo con predicciones antes de ejecutar.

### 9. Sentencia if else

**URL:** https://www.picuino.com/es/python-if-else.html

**Foco:** Control de flujo condicional e indentación obligatoria.

**Conceptos recuperados:**
- if else ejecuta un bloque si se cumple una condición y otro si no.
- Controla el orden de ejecución del programa.
- En Python la sangría define qué instrucciones pertenecen a cada bloque.
- La convención de sangría es 4 espacios.
- Sangrías inconsistentes producen errores.
**Sintaxis / herramientas:**
- `if edad >= 18:`
- `    print('Mayor de edad')`
- `else:`
- `    print('Menor de edad')`
**Actividades o ejercicios recuperados:**
- Número positivo o negativo.
- Número par o impar.
- Comparar dos números.
- Comprobar una condición True/False.
- Determinar nota aprobada o suspensa.
- Validar contraseña.
**Uso pedagógico sugerido:** Debe enseñarse junto a lectura de errores de indentación. En Colab conviene mostrar un error intencional y corregirlo.

### 10. Operadores and, or, not

**URL:** https://www.picuino.com/es/python-if-and-or-not.html

**Foco:** Condiciones compuestas en estructuras if.

**Conceptos recuperados:**
- and exige que se cumplan dos condiciones.
- or permite que se cumpla al menos una condición.
- not invierte el valor lógico de una condición.
- El uso de paréntesis mejora la legibilidad.
- Ejemplos aplicados: montaña rusa y año bisiesto.
**Sintaxis / herramientas:**
- `if (altura >= 150) and (altura <= 200):`
- `if not (num % 2 == 0):`
- `if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):`
**Actividades o ejercicios recuperados:**
- Detectar meses de primavera.
- Modificar condición de par a impar usando not.
- Validar longitud de nombre entre 4 y 6 letras.
- Controlar riego según sensores de lluvia y día.
- Imprimir mensaje si un número es positivo y no divisible por 3.
**Uso pedagógico sugerido:** Buen punto para trabajar pensamiento lógico con sensores o reglas de automatización.

### 11. Sentencias if anidadas

**URL:** https://www.picuino.com/es/python-if-anidados.html

**Foco:** Condicionales dentro de condicionales y decisiones jerárquicas.

**Conceptos recuperados:**
- Una estructura anidada está dentro de otra.
- Cada nivel adicional requiere nueva sangría.
- Los if anidados pueden ser útiles, pero demasiados niveles reducen legibilidad.
- Ejemplos: divisibilidad por 3 y 5; clasificación por edad.
**Sintaxis / herramientas:**
- `if numero % 3 == 0:`
- `    if numero % 5 == 0:`
- `        print(...)`
**Actividades o ejercicios recuperados:**
- Precio de cine según edad.
- Acceso a atracciones según altura y edad.
- Clasificación de nota.
- Diagnóstico de reparación con preguntas sí/no.
- Identificación de personajes de Astérix y Obélix.
- Login usuario/contraseña.
- Clasificación de triángulos.
- Año bisiesto con reglas de 4, 100 y 400.
**Uso pedagógico sugerido:** Permite discutir cuándo anidar y cuándo preferir elif o condiciones compuestas.

### 12. Sentencia elif

**URL:** https://www.picuino.com/es/python-if-elif.html

**Foco:** Evaluación de múltiples condiciones sin anidamiento excesivo.

**Conceptos recuperados:**
- elif equivale conceptualmente a else: if.
- Permite encadenar condiciones alternativas.
- Reduce sangrías sucesivas frente a if anidados.
- Ejemplo central: traducir nota numérica a categoría textual.
**Sintaxis / herramientas:**
- `if nota < 5:`
- `elif nota < 6:`
- `elif nota < 7:`
- `else:`
**Actividades o ejercicios recuperados:**
- Clasificar entero como positivo, negativo o cero.
- Traducir mes numérico a estación.
- Validar rango de nota.
- Verificar si un número entre 1 y 10 es primo y explicar divisibilidad.
**Uso pedagógico sugerido:** Aquí conviene contrastar tres soluciones equivalentes: if anidado, elif y operadores compuestos.

### 13. Sentencia for

**URL:** https://www.picuino.com/es/python-for.html

**Foco:** Bucles definidos con variable iteradora sobre rango o lista.

**Conceptos recuperados:**
- for permite repetir un bloque varias veces mientras una variable cambia.
- El bloque repetido se denomina bucle.
- La variable iteradora toma valores de un range o de una lista.
- range(1, 10) no incluye el 10.
**Sintaxis / herramientas:**
- `for num in range(1, 10):`
- `for nombre in ['Abel', 'Beatriz']:`
- `suma = suma + i`
**Actividades o ejercicios recuperados:**
- Tabla del 6.
- Suma desde 1 hasta n.
- Factorial.
- Edades de 15 a 20 con mayoría de edad.
- Divisibilidad por números entre 2 y 20.
- Ejercicio tipo FizzBuzz con choco/late/chocolate.
**Uso pedagógico sugerido:** Base para automatizar repetición. Conviene exigir traza manual de 3 iteraciones antes de correr el código.

### 14. La función range()

**URL:** https://www.picuino.com/es/python-for-range.html

**Foco:** Generación de secuencias numéricas para bucles.

**Conceptos recuperados:**
- range(start, stop, step) crea rangos para for.
- stop nunca se incluye.
- Con tres argumentos se define inicio, fin exclusivo y salto.
- Con dos argumentos, step vale 1.
- Con un argumento, start vale 0 y step vale 1.
- step puede ser negativo para cuentas descendentes.
**Sintaxis / herramientas:**
- `range(2, 20, 3)`
- `range(100, 0, -10)`
- `range(5, 11)`
- `range(6)`
**Actividades o ejercicios recuperados:**
- Imprimir pares de 2 a 20.
- Imprimir impares de 1 a 19.
- Cuenta atrás de 10 a 0.
- Listados descendentes de 50 a 20 y de -50 a -20.
- Suma de los primeros n impares y verificación de n^2.
**Uso pedagógico sugerido:** Debe enseñarse con recta numérica y comparación de inclusión/exclusión; el error típico es esperar que stop aparezca.

### 15. Sentencia continue

**URL:** https://www.picuino.com/es/python-for-continue.html

**Foco:** Saltar una iteración y continuar con el siguiente elemento del bucle.

**Conceptos recuperados:**
- continue vuelve al comienzo del bucle.
- Evita ejecutar el código que aparece después dentro de esa iteración.
- Ejemplo: imprimir 1 a 20 excepto múltiplos de 3.
**Sintaxis / herramientas:**
- `if num % 3 == 0:`
- `    continue`
- `print(num)`
**Actividades o ejercicios recuperados:**
- Imprimir 1 a 20 excepto múltiplos de 5.
- Imprimir 1 a 10 excepto 4 y 7.
- Sumar 1 a 100 excepto múltiplos de 3.
- Contar números quitando múltiplos de 3 y 7.
- Imprimir años no bisiestos entre 1600 y 2400.
- Cambiar espacios por guiones bajos.
- Cambiar vocales por la letra a.
**Uso pedagógico sugerido:** Útil para depuración de filtros. Conviene comparar con una solución usando if sin continue.

### 16. Sentencia break

**URL:** https://www.picuino.com/es/python-for-break.html

**Foco:** Interrupción anticipada de bucles y uso de for/else.

**Conceptos recuperados:**
- break termina el bucle inmediatamente.
- La ejecución continúa después del bucle.
- for/else se ejecuta si el bucle termina normalmente y no por break.
- Ejemplos: detener en 5 y buscar primer múltiplo de 5 y 7.
**Sintaxis / herramientas:**
- `if num == 5:`
- `    break`
- `for ...:`
- `    ...`
- `else:`
- `    print('No encontrado')`
**Actividades o ejercicios recuperados:**
- Cuenta atrás detenida en 5.
- Contraseña con máximo 4 intentos.
- Imprimir frase hasta letra 30.
- Sumar hasta superar 1000.
- Buscar divisores para decidir si un número es primo.
**Uso pedagógico sugerido:** Permite enseñar búsqueda y validación. El uso de for/else suele ser avanzado; requiere ejemplo visual.

### 17. Sentencias for anidadas

**URL:** https://www.picuino.com/es/python-for-anidados.html

**Foco:** Bucles dentro de bucles para construir tablas y patrones.

**Conceptos recuperados:**
- Una estructura for puede estar dentro de otra.
- Cada nivel exige nueva sangría.
- Ejemplo central: tabla de multiplicar de 1 a 10.
- Uso de tabulación \t para alinear salidas.
**Sintaxis / herramientas:**
- `for i in range(1, 11):`
- `    for j in range(1, 11):`
- `        print(i*j, end='\t')`
**Actividades o ejercicios recuperados:**
- Determinar si un número es producto de dos números de 1 a 10.
- Dibujar triángulo de asteriscos.
- Dibujar triángulo de números.
- Dibujar triángulo invertido.
- Dibujar patrón tipo ajedrez.
- Dibujar patrón según divisibilidad de coordenadas por 3.
**Uso pedagógico sugerido:** Muy adecuado para ejercicios visuales; permite detectar si el estudiante comprende filas, columnas y reinicio de línea.

### 18. Sentencia while

**URL:** https://www.picuino.com/es/python-while.html

**Foco:** Bucles condicionados cuando no se sabe de antemano la cantidad de repeticiones.

**Conceptos recuperados:**
- while ejecuta un bloque mientras se cumple una condición.
- Se usa cuando se conoce la condición de continuidad, no necesariamente el número de repeticiones.
- while True crea bucles potencialmente infinitos.
- break permite detener un while True cuando se cumple una condición interna.
**Sintaxis / herramientas:**
- `while suma < 1000:`
- `while True:`
- `    if nombre == 'fin':`
- `        break`
**Actividades o ejercicios recuperados:**
- Imprimir 0 a 10.
- Imprimir 10 a 0.
- Sumar enteros hasta llegar a 1000.
- Repetir hasta que la respuesta sea n.
- Imprimir sucesión de Fibonacci hasta 1000.
- Juego de adivinar número con random.randint().
**Uso pedagógico sugerido:** Debe enseñarse junto con riesgo de bucle infinito y actualización de variables de control.

### 19. Definición de funciones

**URL:** https://www.picuino.com/es/python-funciones.html

**Foco:** Crear bloques reutilizables con def, parámetros y return.

**Conceptos recuperados:**
- Una función agrupa código que realiza una tarea.
- Ayuda a dividir programas largos en bloques pequeños.
- La definición no ejecuta por sí sola: requiere llamada.
- Parámetros son variables declaradas en la función; argumentos son valores enviados al llamarla.
- return devuelve un dato y puede terminar la función.
**Sintaxis / herramientas:**
- `def mensaje():`
- `def saludo(nombre):`
- `def suma(a, b):`
- `    return a + b`
**Actividades o ejercicios recuperados:**
- Función par/impar.
- Función mayor(a,b).
- Conversión Celsius a Fahrenheit.
- Función factorial.
- Función fila de asteriscos y triángulo.
- Función tabla de multiplicar.
**Uso pedagógico sugerido:** Hito importante de abstracción. Conviene exigir que toda función tenga propósito claro, entrada y salida esperada.

### 20. Parámetros con valores por omisión

**URL:** https://www.picuino.com/es/python-funciones-argumentos.html

**Foco:** Argumentos opcionales y diseño de funciones reutilizables.

**Conceptos recuperados:**
- Los parámetros pueden tener valores por defecto.
- Si existe valor por defecto, el argumento puede omitirse.
- Los parámetros con valores por defecto deben colocarse a la derecha de los demás.
- Ejemplo: saludo(nombre='María').
**Sintaxis / herramientas:**
- `def saludo(nombre='María'):`
- `def reemplaza_vocales(texto, vocal='e'):`
**Actividades o ejercicios recuperados:**
- Contar múltiplos desde 1 hasta tope.
- Agregar tope por defecto igual a 100.
- Contar vocales en una cadena.
- Imprimir el menor de tres números.
- Retornar True si tres números están ordenados.
- Ordenar tres números usando función auxiliar.
**Uso pedagógico sugerido:** Buena oportunidad para hablar de API de una función: qué argumentos son obligatorios y cuáles son opcionales.

### 21. Cadenas de texto

**URL:** https://www.picuino.com/es/python-textos.html

**Foco:** Manipulación básica de strings, escapes, Unicode y cadenas multilínea.

**Conceptos recuperados:**
- Las cadenas pueden escribirse con comillas simples o dobles.
- El carácter escape permite incluir comillas y símbolos especiales.
- Secuencias comunes: \, \n, \r, \t, \b.
- Python puede manejar Unicode: tildes, ñ, alfabetos, símbolos y emojis.
- Cadenas multilínea con triple comilla.
- Docstrings dentro de funciones y consulta con help().
- Unión con + y repetición con *.
**Sintaxis / herramientas:**
- `'Hola, mundo'`
- `'doesn\'t'`
- `print("""texto multilínea""")`
- `'Hola, ' + 'mundo'`
- `'Ja ' * 5`
**Actividades o ejercicios recuperados:**
- Crear texto con caracteres especiales.
- Dibujar recuadro doble multilínea.
- Crear función que imprima tabla 2x2 con docstring.
- Leer cadena e imprimir cantidad de caracteres.
- Función que genere recuadro alrededor de cualquier texto.
**Uso pedagógico sugerido:** Conecta programación con expresión visual. Útil para motivar a estudiantes mediante salidas personalizadas.

### 22. Índices de cadenas de texto

**URL:** https://www.picuino.com/es/python-textos-indices.html

**Foco:** Acceso, rebanadas e iteración de caracteres.

**Conceptos recuperados:**
- Las cadenas están formadas por caracteres individuales.
- Los índices comienzan en 0.
- Los índices negativos comienzan desde el final.
- Índices fuera de rango producen error.
- Las rebanadas usan dos puntos para tomar rangos de caracteres.
- Omitir límites equivale a tomar desde el comienzo o hasta el final.
- Las rebanadas fuera de rango devuelven cadena vacía.
- Un for puede recorrer una cadena carácter por carácter.
**Sintaxis / herramientas:**
- `lang[0]`
- `lang[-1]`
- `lang[0:3]`
- `lang[:3]`
- `lang[3:]`
- `for c in 'Hola, mundo':`
**Actividades o ejercicios recuperados:**
- Función deletrea sin índices.
- Función deletrea con índices.
- Impresión progresiva de una cadena desde la izquierda.
- Impresión progresiva desde la derecha.
- Ventana móvil de cinco caracteres.
**Uso pedagógico sugerido:** Se debe insistir en índice cero y diferencia entre índice único y rebanada.

### 23. Métodos de cadenas de texto

**URL:** https://www.picuino.com/es/python-textos-metodos.html

**Foco:** Métodos asociados a strings y búsqueda de subcadenas.

**Conceptos recuperados:**
- Los métodos se llaman con punto sobre una cadena o variable.
- Métodos tratados: upper(), lower(), swapcase(), title(), find(), strip(), replace(), split().
- La sentencia in permite saber si un texto está dentro de otro.
- La búsqueda es sensible a mayúsculas/minúsculas; lower() ayuda a normalizar.
**Sintaxis / herramientas:**
- `'PaLaBrA'.upper()`
- `cadena.find('lugar')`
- `'Hola nombre'.replace('nombre','Miguel')`
- `'hola' in 'Hola, mundo'.lower()`
**Actividades o ejercicios recuperados:**
- Alternar mayúsculas y minúsculas letra por letra.
- Mayúsculas en índices múltiplos de 3.
- Detector de palabras tabú en descripción de Lionel Messi.
- Función para reemplazar vocales por una vocal configurable.
**Uso pedagógico sugerido:** Muy útil para proyectos de procesamiento simple de texto, validación de entradas y filtros.

### 24. Formateo de cadenas de texto

**URL:** https://www.picuino.com/es/python-textos-formateo.html

**Foco:** f-strings y formatos numéricos/textuales.

**Conceptos recuperados:**
- Un f-string empieza con f o F y usa campos entre llaves.
- Los campos contienen variables y pueden incluir formato.
- Para imprimir llaves se duplican: {{ o }}.
- Formatos abordados: alineación, relleno, enteros, signo, hexadecimal, binario, flotantes, notación científica y carácter Unicode.
**Sintaxis / herramientas:**
- `f'El creador de Python es {nombre} {apellido}'`
- `f'{num:03d}'`
- `f'{nombre:>20}'`
- `f'{pi:10.3f}'`
- `f'{78:c}'`
**Actividades o ejercicios recuperados:**
- Alinear nombre a derecha, izquierda y centro.
- Formatear enteros en decimal, con signo, hexadecimal y binario.
- Formatear flotantes con decimales, ceros y notación científica.
- Explorar caracteres Unicode.
- Mostrar los siguientes 20 caracteres desde uno ingresado con ord().
- Convertir color RGB a hexadecimal.
**Uso pedagógico sugerido:** Es una clase potente para salidas prolijas y reportes. Conviene simplificar para principiantes y priorizar casos reales: notas, porcentajes y colores.

### 25. Listas

**URL:** https://www.picuino.com/es/python-listas.html

**Foco:** Estructuras ordenadas de datos y operaciones básicas.

**Conceptos recuperados:**
- Una lista es un conjunto ordenado de datos.
- Se define con corchetes y elementos separados por comas.
- Puede contener datos de distintos tipos e incluso otras listas.
- Las listas complejas pueden escribirse en varias líneas.
- Se pueden concatenar con + y repetir con *.
- in y not in permiten verificar pertenencia.
**Sintaxis / herramientas:**
- `lista_impares = [1, 3, 5, 7, 9]`
- `nombre_y_altura = [['Juan', 176], ['Nerea', 169]]`
- `[1,2,3] + [4,5,6]`
- `3 in lista`
**Actividades o ejercicios recuperados:**
- Lista de cinco compañeros/as o amigos/as.
- Lista de edades y lista anidada.
- Lista multilínea con frases famosas.
- Lista de los 10 primeros primos en dos partes.
- Función para comprobar pertenencia de números a la lista de primos.
**Uso pedagógico sugerido:** Marca el paso desde variables sueltas a colecciones. Conviene usar listas con datos significativos para estudiantes.

### 26. Índices de listas

**URL:** https://www.picuino.com/es/python-listas-indices.html

**Foco:** Acceso, rebanadas, modificación y eliminación de elementos en listas.

**Conceptos recuperados:**
- Las listas usan índices y rebanadas como las cadenas.
- Los índices empiezan en cero y pueden ser negativos.
- Las rebanadas devuelven sublistas.
- A diferencia de strings, las listas son mutables.
- Se pueden reemplazar elementos individuales o tramos.
- del elimina elementos o rebanadas.
**Sintaxis / herramientas:**
- `lista[0]`
- `lista[-1]`
- `lista[1:-1]`
- `lista[0] = 'A'`
- `del lista[2]`
- `del lista[1:3]`
**Actividades o ejercicios recuperados:**
- Imprimir primer, tercer y séptimo primo.
- Sumar los 4 primeros primos con bucle por índices.
- Modificar el segundo nombre de una lista.
- Imprimir sublistas del abecedario.
- Borrar posiciones pares.
- Cambiar letras mayúsculas a minúsculas recorriendo con len().
**Uso pedagógico sugerido:** Debe trabajarse con dibujos de posiciones. La mutabilidad de listas es una diferencia conceptual clave frente a strings.

### 27. Iteración de listas

**URL:** https://www.picuino.com/es/python-listas-iteracion.html

**Foco:** Recorrer listas y generar listas nuevas.

**Conceptos recuperados:**
- Iterar una lista significa recorrer sus elementos uno a uno.
- for permite actuar sobre cada elemento.
- len() entrega número de elementos y permite iterar por índice.
- list() permite crear listas desde range() o desde una cadena.
- La comprensión de listas genera listas de forma abreviada.
**Sintaxis / herramientas:**
- `for nombre in lista:`
- `for i in range(len(lista)):`
- `list(range(10))`
- `list('Hola, mundo')`
- `[num for num in range(10)]`
**Actividades o ejercicios recuperados:**
- Imprimir nombres y letra inicial.
- Leer frase y mostrarla al revés.
- Generar impares hasta 99 y sumar 2500.
- Eliminar duplicados construyendo lista nueva.
- Cifrar frase separando caracteres de índices pares e impares.
- Descifrar el código anterior.
**Uso pedagógico sugerido:** Clase muy rica para pensamiento algorítmico. Conviene reforzar diferencia entre recorrer valores y recorrer posiciones.

### 28. Métodos de listas

**URL:** https://www.picuino.com/es/python-listas-metodos.html

**Foco:** Métodos y funciones frecuentes para manipular listas.

**Conceptos recuperados:**
- Métodos de lista se llaman con punto.
- append() añade al final.
- pop() retira elementos.
- index() devuelve posición.
- count() cuenta apariciones.
- join() une cadenas de una lista.
- Funciones abordadas: max(), min(), sum(), len(), sorted(), list().
**Sintaxis / herramientas:**
- `lista.append(6)`
- `lista.pop()`
- `lista.pop(0)`
- `lista.index(4)`
- `lista.count(3)`
- `', '.join(lista)`
- `sum(lista)`
- `sorted(lista)`
**Actividades o ejercicios recuperados:**
- Función promedio de una lista.
- Función que retorna solo números pares.
- Función resumen que retorne mínimo, máximo, cantidad y suma.
**Uso pedagógico sugerido:** Ideal para construir mini-proyectos de análisis de datos simples, por ejemplo listas de notas o tiempos deportivos.

### 29. Búsqueda de datos

**URL:** https://www.picuino.com/es/python-busqueda.html

**Foco:** Búsqueda lineal implementada manualmente.

**Conceptos recuperados:**
- Se estudian algoritmos de búsqueda sin usar funciones ya hechas para comprender su funcionamiento interno.
- La búsqueda lineal recorre todos los elementos hasta encontrar lo buscado.
- Ejemplo base: buscar la posición del menor elemento de una lista.
- Se usa una variable para guardar la mejor posición encontrada hasta el momento.
**Sintaxis / herramientas:**
- `def busca_menor(lista):`
- `menor = 0`
- `for i in range(len(lista)):`
- `    if lista[i] < lista[menor]:`
- `        menor = i`
**Actividades o ejercicios recuperados:**
- Buscar elemento mayor.
- Devolver posición del último par o None.
- Devolver posición del primer impar o None.
- Contar apariciones de un elemento.
- Contar apariciones de todas las notas de 0 a 10.
- Repetir búsqueda del menor, imprimirlo y eliminarlo para obtener salida ordenada.
**Uso pedagógico sugerido:** Clase de transición desde uso de listas hacia algoritmos. Conviene pedir trazas de variables menor/i.

### 30. Búsqueda binaria

**URL:** https://www.picuino.com/es/python-busqueda-binaria.html

**Foco:** Algoritmo eficiente de búsqueda sobre listas ordenadas.

**Conceptos recuperados:**
- La búsqueda binaria es más rápida que la lineal si la lista está ordenada.
- Busca en la mitad de la lista y descarta mitades sucesivamente.
- Devuelve posición si encuentra el elemento; si no, devuelve None.
- Usa índices inicio, final y medio.
- Ejemplo: encontrar un elemento en 3 comparaciones frente a muchas de búsqueda lineal.
**Sintaxis / herramientas:**
- `inicio = 0`
- `final = len(lista) - 1`
- `medio = (inicio + final) // 2`
- `if lista[medio] == buscado:`
- `elif lista[medio] < buscado:`
- `return None`
**Actividades o ejercicios recuperados:**
- Programar función que retorne la posición donde insertar un nuevo número en una lista ordenada.
- Probar inserciones con 7, 25, 48, 68 y 100.
**Uso pedagógico sugerido:** Excelente para comparar eficiencia algorítmica. Requiere que estudiantes entiendan primero ordenamiento y posiciones.

### 31. Desplazamiento de datos

**URL:** https://www.picuino.com/es/python-desplazamiento.html

**Foco:** Movimiento de datos en memoria/listas: intercambio y desplazamientos.

**Conceptos recuperados:**
- Desplazar datos significa mover datos de un lugar a otro.
- Aunque Python tiene métodos eficientes, se trabaja a bajo nivel para comprender algoritmos generales.
- Intercambio de variables usando temporal.
- Intercambio de posiciones de una lista.
- Desplazamiento a la derecha: comenzar desde la derecha para no pisar datos.
- Desplazamiento a la izquierda: mover en dirección contraria.
**Sintaxis / herramientas:**
- `temp = bajo; bajo = alto; alto = temp`
- `for i in range(final, 0, -1): lista[i] = lista[i-1]`
- `for i in range(final): lista[i] = lista[i+1]`
**Actividades o ejercicios recuperados:**
- Intercambiar dos variables.
- Intercambiar tres variables hasta que coincidan con sus nombres.
- Función desplaza_izquierda(lista, nuevo_valor).
- Función desplaza_derecha(lista, min).
- Función desplaza_izquierda(lista, min).
**Uso pedagógico sugerido:** Fundamental para entender ordenamientos. Conviene dibujar la lista antes/después y explicar riesgo de sobrescribir datos.

### 32. Ordenación por selección

**URL:** https://www.picuino.com/es/python-sort-seleccion.html

**Foco:** Ordenamiento seleccionando repetidamente el menor elemento.

**Conceptos recuperados:**
- Los algoritmos de ordenación organizan listas de menor a mayor.
- Selección busca el elemento más pequeño de la parte no ordenada.
- Luego intercambia ese menor con la primera posición no ordenada.
- Al repetir, crece una zona inicial ordenada.
- Versión I usa intercambio directo.
- Versión II usa desplazamiento a la derecha para conservar el orden relativo de elementos no movidos.
**Sintaxis / herramientas:**
- `def busca_menor(lista, final):`
- `for final in range(len(lista)-1):`
- `temp = lista[final]`
- `desplaza_derecha(lista, comienzo, menor)`
**Actividades o ejercicios recuperados:**
- Reescribir ordenación I de mayor a menor.
- Reescribir ordenación II comenzando por la derecha.
- Mover todos los ceros de una lista a la izquierda manteniendo orden del resto.
- Ordenar cadenas por longitud.
**Uso pedagógico sugerido:** Debe abordarse después de búsqueda y desplazamiento. Buena clase para comparar intercambio vs desplazamiento.

### 33. Ordenación por inserción

**URL:** https://www.picuino.com/es/python-sort-insercion.html

**Foco:** Ordenamiento insertando cada elemento en una sublista ya ordenada.

**Conceptos recuperados:**
- La inserción permite modificar la lista mientras se ordena.
- Es flexible para conjuntos pequeños, especialmente menores de 100 elementos.
- Se supone inicialmente ordenado el primer elemento.
- Cada nuevo elemento se mueve hacia la izquierda hasta encontrar su posición.
- Puede mejorarse usando búsqueda binaria para hallar posición de inserción.
**Sintaxis / herramientas:**
- `def inserta_elemento(lista, index):`
- `for i in range(index, 0, -1):`
- `if lista[i-1] > lista[i]:`
- `while primero <= ultimo:`
- `lista[primero] = temp`
**Actividades o ejercicios recuperados:**
- Ordenar lista de tres elementos sin bucles, solo if.
- Reescribir ordenación descendente.
- Reescribir todo en una sola función.
- Ordenar cadenas por longitud.
**Uso pedagógico sugerido:** Cierra bien una secuencia de algoritmos: búsqueda binaria + desplazamiento + ordenamiento. Recomienda comparar con selección.

## Fuentes consultadas

- Picuino — Tutorial de Python: https://www.picuino.com/es/python-index.html
- Clase 1: Introducción al lenguaje Python — https://www.picuino.com/es/python-intro.html
- Clase 2: Datos numéricos — https://www.picuino.com/es/python-datos-numeros.html
- Clase 3: Las variables — https://www.picuino.com/es/python-variables.html
- Clase 4: Palabras reservadas — https://www.picuino.com/es/python-palabras-reservadas.html
- Clase 5: Los comentarios — https://www.picuino.com/es/python-comentarios.html
- Clase 6: La función print() — https://www.picuino.com/es/python-print.html
- Clase 7: La función input() — https://www.picuino.com/es/python-input.html
- Clase 8: El tipo Booleano — https://www.picuino.com/es/python-booleanos.html
- Clase 9: Sentencia if else — https://www.picuino.com/es/python-if-else.html
- Clase 10: Operadores and, or, not — https://www.picuino.com/es/python-if-and-or-not.html
- Clase 11: Sentencias if anidadas — https://www.picuino.com/es/python-if-anidados.html
- Clase 12: Sentencia elif — https://www.picuino.com/es/python-if-elif.html
- Clase 13: Sentencia for — https://www.picuino.com/es/python-for.html
- Clase 14: La función range() — https://www.picuino.com/es/python-for-range.html
- Clase 15: Sentencia continue — https://www.picuino.com/es/python-for-continue.html
- Clase 16: Sentencia break — https://www.picuino.com/es/python-for-break.html
- Clase 17: Sentencias for anidadas — https://www.picuino.com/es/python-for-anidados.html
- Clase 18: Sentencia while — https://www.picuino.com/es/python-while.html
- Clase 19: Definición de funciones — https://www.picuino.com/es/python-funciones.html
- Clase 20: Parámetros con valores por omisión — https://www.picuino.com/es/python-funciones-argumentos.html
- Clase 21: Cadenas de texto — https://www.picuino.com/es/python-textos.html
- Clase 22: Índices de cadenas de texto — https://www.picuino.com/es/python-textos-indices.html
- Clase 23: Métodos de cadenas de texto — https://www.picuino.com/es/python-textos-metodos.html
- Clase 24: Formateo de cadenas de texto — https://www.picuino.com/es/python-textos-formateo.html
- Clase 25: Listas — https://www.picuino.com/es/python-listas.html
- Clase 26: Índices de listas — https://www.picuino.com/es/python-listas-indices.html
- Clase 27: Iteración de listas — https://www.picuino.com/es/python-listas-iteracion.html
- Clase 28: Métodos de listas — https://www.picuino.com/es/python-listas-metodos.html
- Clase 29: Búsqueda de datos — https://www.picuino.com/es/python-busqueda.html
- Clase 30: Búsqueda binaria — https://www.picuino.com/es/python-busqueda-binaria.html
- Clase 31: Desplazamiento de datos — https://www.picuino.com/es/python-desplazamiento.html
- Clase 32: Ordenación por selección — https://www.picuino.com/es/python-sort-seleccion.html
- Clase 33: Ordenación por inserción — https://www.picuino.com/es/python-sort-insercion.html