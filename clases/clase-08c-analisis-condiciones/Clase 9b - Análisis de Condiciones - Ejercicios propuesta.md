# Ejercicios adicionales — Clase 9b: Análisis de Condiciones

## Introducción

Estos ejercicios te permiten seguir practicando lo de hoy: leer una situación en lenguaje natural, identificar qué operador la representa mejor y escribir el programa correcto. Cada ejercicio cubre un error distinto — no todos los bugs son del mismo tipo. Intenta cada uno antes de mirar la solución.

---

## Ejercicio 1 — Clasificación Diamond en Brawl Stars

**Nivel:** Práctica base

**Enunciado:**
En Brawl Stars, los jugadores con 600 trofeos o más quedan clasificados automáticamente para el torneo Diamond del fin de semana. Cualquier jugador puede verificar si clasifica ingresando su conteo de trofeos. Un compañero que tenía exactamente 600 trofeos consultó y el sistema le dijo que no clasificaba.

Antes de escribir el programa, analiza:
1. Según las reglas del torneo, ¿un jugador con exactamente 600 trofeos debería clasificar? ¿Por qué?
2. La frase es "600 trofeos o más". ¿El límite exacto está incluido o excluido? ¿Qué operador lo representa mejor?
3. ¿Con qué tres valores de trofeos probarías tu programa para confirmar que el caso límite funciona?

Escribe el programa: le pide al jugador su conteo de trofeos e imprime si clasifica para el torneo Diamond.

**Resultado esperado:**
```
¿Cuántos trofeos tienes? 600
¿Clasificas para el torneo Diamond? True
```

**Solución:**
```python
trofeos_jugador = int(input("¿Cuántos trofeos tienes? "))
print("¿Clasificas para el torneo Diamond?", trofeos_jugador >= 600)
```

---

## Ejercicio 2 — Aforo de la micro escolar

**Nivel:** Práctica base

**Enunciado:**
El inspector de la micro escolar usa una app que muestra aviso verde si el bus lleva 45 pasajeros o menos (dentro del aforo permitido). Una mañana en que subieron exactamente 45 alumnos, el sistema marcó rojo, como si el aforo estuviera excedido.

Antes de escribir el programa, analiza:
1. ¿45 pasajeros en una micro con aforo de 45 debería estar dentro del límite? ¿Por qué?
2. La frase es "45 pasajeros o menos". ¿El límite exacto está incluido o excluido? ¿Qué operador lo representa mejor?
3. ¿Con qué tres valores probarías para confirmar que el caso límite funciona?

Escribe el programa: le pide al inspector el número de pasajeros e imprime si el bus está dentro del aforo.

**Resultado esperado:**
```
¿Cuántos pasajeros van en la micro? 45
¿Está dentro del aforo? True
```

**Solución:**
```python
pasajeros_micro = int(input("¿Cuántos pasajeros van en la micro? "))
print("¿Está dentro del aforo?", pasajeros_micro <= 45)
```

---

## Ejercicio 3 — Cobro en estacionamiento de mall

**Nivel:** Práctica base

**Enunciado:**
El sistema de estacionamiento de un mall cobra si el vehículo estuvo más de 60 minutos. Un usuario que estuvo exactamente 60 minutos se encontró con que el sistema le cobró, aunque las reglas dicen que los primeros 60 minutos son gratis.

Antes de escribir el programa, analiza:
1. ¿Debería cobrarse a alguien que estuvo exactamente 60 minutos? ¿Por qué?
2. La frase es "más de 60 minutos". ¿El límite exacto está incluido en el cobro o excluido? ¿Qué operador lo representa mejor?
3. ¿Con qué tres valores de minutos probarías para confirmar que el caso límite funciona?

Escribe el programa: le pide al usuario los minutos que estuvo estacionado e imprime si debe pagar.

**Resultado esperado:**
```
¿Cuántos minutos estuviste estacionado? 60
¿Debes pagar? False
```

**Solución:**
```python
minutos_estacionado = int(input("¿Cuántos minutos estuviste estacionado? "))
print("¿Debes pagar?", minutos_estacionado > 60)
```

---

## Ejercicio 4 — Tarifa preferencial del bus

**Nivel:** Práctica base

**Enunciado:**
El sistema de pago del bus otorga tarifa preferencial a pasajeros menores de 18 años. Un estudiante que acababa de cumplir 18 años se encontró con que el sistema le otorgó la tarifa preferencial, aunque ya tenía 18.

Antes de escribir el programa, analiza:
1. ¿Debería recibir tarifa preferencial alguien con exactamente 18 años? ¿Por qué?
2. La frase es "menores de 18 años". ¿El límite exacto está incluido en la preferencial o excluido? ¿Qué operador lo representa mejor?
3. ¿Con qué tres valores de edad probarías para confirmar que el caso límite funciona?

Escribe el programa: le pide al pasajero su edad e imprime si tiene tarifa preferencial.

**Resultado esperado:**
```
¿Cuántos años tienes? 18
¿Tienes tarifa preferencial? False
```

**Solución:**
```python
edad_pasajero = int(input("¿Cuántos años tienes? "))
print("¿Tienes tarifa preferencial?", edad_pasajero < 18)
```

---

## Ejercicio 5 — Enfrentamiento en torneo de esports ⭐

**Nivel:** Desafío opcional

**Enunciado:**
En un torneo de esports, avanza al siguiente round quien tenga el puntaje más alto del match. Si hay empate, ninguno avanza y se repite la partida. Cualquier participante puede consultar si avanzó ingresando su puntaje y el del rival. En un enfrentamiento donde ambos jugadores terminaron con 1850 puntos, el sistema avanzó a los dos — pero las reglas dicen que empate significa repetición.

Antes de escribir el programa, analiza:
1. ¿Debería avanzar alguien cuando hay empate exacto? ¿Por qué?
2. La frase es "puntaje más alto que el rival". ¿"Más alto" incluye el empate o lo excluye? ¿Qué operador lo representa mejor?
3. ¿Con qué tres pares de puntajes distintos probarías el caso límite?

Escribe el programa: le pide al usuario su puntaje y el del rival, e imprime si avanza al siguiente round.

**Pistas:**
Esta vez el programa necesita dos `input()`, uno para cada puntaje. La comparación es entre los dos valores ingresados, no contra un número fijo.

**Resultado esperado:**
```
¿Cuál es tu puntaje? 1850
¿Cuál es el puntaje del rival? 1850
¿Avanzas al siguiente round? False
```

**Solución:**
```python
puntaje_jugador = int(input("¿Cuál es tu puntaje? "))
puntaje_rival = int(input("¿Cuál es el puntaje del rival? "))
print("¿Avanzas al siguiente round?", puntaje_jugador > puntaje_rival)
```
