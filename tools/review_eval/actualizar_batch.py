"""
Actualiza puntajes.json con los resultados de un batch de revision.
Uso: python tools/review_eval/actualizar_batch.py
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.parent
PUNTAJES_PATH = BASE_DIR / "clases" / "reforzamiento-evaluacion" / "revision" / "puntajes.json"

# ── Batch 1 ──────────────────────────────────────────────────────────────────
BATCH_1 = {
    "alonso YT": {
        "ej1": (7,  "Faltan 3 prints individuales (-2), promedio sin etiqueta (-1)."),
        "ej2": (10, "Titulo, encabezado columnas, sep, total: todo correcto."),
        "ej3": (15, "Usa una sola variable saldo con += y -= en cada paso. Caso ideal."),
        "ej4": (15, "input float ok, descuento y precio final correctos, datos en output."),
        "ej5": (12, "Calculos correctos. Olvidó prefijo f en f-strings: prints muestran texto literal en vez de valores (-3)."),
        "ej6": (15, "Los 5 errores corregidos."),
        "ej7": (20, "6 inputs, total, promedio, saldo y header --- RESUMEN SEMANAL --- presentes."),
    },
    "Benjamín Diaz": {
        "ej1": (2,  "print(primera_nota=5.5) -> TypeError. Promedio hardcodeado. Intento visible pero nada funciona."),
        "ej2": (0,  "Sintaxis completamente rota."),
        "ej3": (0,  "Usa $20000 con signo pesos: no es Python valido."),
        "ej4": (0,  "Vacio."),
        "ej5": (0,  "Vacio."),
        "ej6": (0,  "Ningún error corregido."),
        "ej7": (0,  "Vacio."),
    },
    "Cristóbal Muñoz": {
        "ej1": (10, "3 variables snake_case, promedio calculado, 4 prints con etiqueta."),
        "ej2": (9,  "sep ok, encabezado columnas ok, total ok. Falta titulo principal del reporte (-1)."),
        "ej3": (9,  "Multiples variables en vez de una sola (4/10 calc). Prints con etiqueta (5/5)."),
        "ej4": (15, "input float ok, calculos correctos, datos en output."),
        "ej5": (14, "Ganancia neta y por persona calculadas inline. Todos los datos en output. Falta separador --- (-1)."),
        "ej6": (15, "Los 5 errores corregidos."),
        "ej7": (10, "6 inputs ok. Bugs: gasto_viernes sumado dos veces, divisor 4 en vez de 5, saldo_inicial undefined (NameError), falta header (-1)."),
    },
    "Damián Silva": {
        "ej1": (3,  "3 variables definidas, promedio no calculado. Imprime nota_uno etiquetado como promedio."),
        "ej2": (9,  "sep ok, encabezado columnas ok, valores hardcodeados pero correctos. Falta titulo (-1)."),
        "ej3": (2,  "Flujo correcto pero valores hardcodeados, prints sin etiqueta."),
        "ej4": (1,  "Un print(input(...)) sin calculos."),
        "ej5": (0,  "Vacio."),
        "ej6": (0,  "Ningún error corregido."),
        "ej7": (0,  "Vacio."),
    },
    "Diego Cifuentes": {
        "ej1": (2,  "Variables definidas. promedio = sin valor: error de sintaxis."),
        "ej2": (2,  "Variables y total calculados, seccion de prints vacia."),
        "ej3": (2,  "Multiples variables hardcodeadas, calculos inline, sin etiquetas."),
        "ej4": (0,  "Vacio."),
        "ej5": (0,  "Vacio."),
        "ej6": (15, "Los 5 errores corregidos."),
        "ej7": (0,  "Vacio."),
    },
    "Diego Donoso": {
        "ej1": (3,  "PascalCase (-2). Promedio = suma sin dividir. Print hardcodeado con valor incorrecto."),
        "ej2": (2,  "Variables y total calculados. Prints vacios."),
        "ej3": (0,  "Solo saldo_inical = 20000, nada mas."),
        "ej4": (1,  "Valores hardcodeados, un input sin usar, sin calculo real."),
        "ej5": (0,  "Vacio."),
        "ej6": (6,  "Errores 1 y 2 corregidos (nota_modulo sin espacio, indentacion ok). Errores 3, 4, 5 sin corregir (2 x 3 = 6 pts)."),
        "ej7": (0,  "Vacio."),
    },
}


def actualizar(batch: dict) -> None:
    data = json.loads(PUNTAJES_PATH.read_text(encoding="utf-8"))
    updated = []

    for nombre, ejercicios in batch.items():
        if nombre not in data["estudiantes"]:
            print(f"  ADVERTENCIA: '{nombre}' no encontrado en puntajes.json")
            continue

        est = data["estudiantes"][nombre]
        total = 0
        for ej, (obtenido, comentario) in ejercicios.items():
            est["puntajes"][ej]["obtenido"] = obtenido
            est["puntajes"][ej]["comentario"] = comentario
            total += obtenido
        est["total"] = total
        est["revisado"] = True
        updated.append(f"  {nombre}: {total} pts")

    PUNTAJES_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("Batch actualizado:")
    for line in updated:
        print(line)


# ── Batch 2 ──────────────────────────────────────────────────────────────────
BATCH_2 = {
    "Diego Vargas": {
        "ej1": (2,  "Prints de strings hardcodeados, IndentationError en línea 3, sin variables definidas ni cálculo."),
        "ej2": (2,  "Total calculado pero prints solo dicen 'empanadas', 'bebidas', 'sopaipillas'. Sin título, encabezado ni total impreso."),
        "ej3": (0,  "print(var) =valor es sintaxis rota. Sin variables ni operaciones válidas."),
        "ej4": (0,  "input(precio_producto)=59990 es sintaxis inválida. Nada ejecuta."),
        "ej5": (0,  "Vacío."),
        "ej6": (0,  "Conserva todos los errores originales y agrega código adicional roto (x en vez de *)."),
        "ej7": (0,  "Vacío (solo el comentario del enunciado)."),
    },
    "Eduardo Eleazarth Pacco Ríos": {
        "ej1": (10, "nota1, nota2, nota3 definidas, promedio calculado, 4 prints con etiqueta. Perfecto."),
        "ej2": (10, "Título presente (distinto pero válido), encabezado columnas, sep, total: todo correcto."),
        "ej3": (15, "Variable única saldo con +=/-= para cada operación. 6 prints con etiqueta. Caso ideal."),
        "ej4": (10, "input() para precio ok, pero pide el monto del descuento directamente en vez del porcentaje. Sin cálculo %. 3 valores en output."),
        "ej5": (14, "3 inputs, ganancia_neta y por_persona calculadas correctamente. Todos los datos en output. Falta título '--- REPARTO DEL PUESTO ---' (-1)."),
        "ej6": (12, "Errores 1-4 corregidos. Error 5 (coma faltante en print Participación) sin corregir."),
        "ej7": (20, "6 inputs, total, promedio, saldo y header '------RESUMEN SEMANA-------' presentes. Perfecto."),
    },
    "Estudiante Profesor Diego 1": {
        "ej1": (7,  "Variables definidas, promedio calculado. Solo print(promedio) sin etiqueta. Faltan 3 prints individuales (-2), promedio sin etiqueta (-1)."),
        "ej2": (9,  "Encabezado columnas ok, sep ok, total ok. Falta título principal del reporte (-1)."),
        "ej3": (7,  "Múltiples variables hardcodeadas como estados (tras_sueldo=105000, etc.), no como montos. Fórmula de saldo_final incorrecta (suma estados). Falta paso servicios_básicos. Prints con etiquetas en 5 de 6 estados."),
        "ej4": (4,  "Valores hardcodeados, 2 inputs() no almacenados, precio_final calculado correctamente, pero solo 1 de 3 valores impreso."),
        "ej5": (2,  "Valores hardcodeados, 4 inputs() no almacenados, sin cálculo de ganancia_neta. Solo 1 de 5 valores impreso (ganancia_por_persona hardcodeada)."),
        "ej6": (12, "Errores 1-4 corregidos. Error 5 (coma faltante en print Participación) sin corregir."),
        "ej7": (1,  "Solo 2 llamadas a int(input()) sin almacenar. Sin variables, cálculos ni output."),
    },
    "Felipe Aravena": {
        "ej1": (10, "nota1, nota2, nota3 definidas, promedio calculado con round(), 4 prints con etiqueta. Perfecto."),
        "ej2": (10, "Título exacto con emoji, encabezado columnas, sep, 3 filas con variables, total. Perfecto."),
        "ej3": (15, "Variable única saldo_inicial con +=/-= en cada paso. 6 prints con etiqueta. Caso ideal."),
        "ej4": (12, "input() para precio ok. Descuento hardcodeado al 20% sin pedir porcentaje por input (-3). Cálculo correcto, 3 valores en output, título presente."),
        "ej5": (15, "3 inputs, ganancia_neta y por_persona calculadas, título y 5 datos en output. Perfecto."),
        "ej6": (12, "Errores 1-4 corregidos. Error 5 (coma faltante en print Participación) sin corregir."),
        "ej7": (20, "6 inputs, total, promedio, saldo y header '---RESUMEN SEMANAL---' presentes. Perfecto."),
    },
    "francisca parra": {
        "ej1": (2,  "Nota_1, Nota_2, Nota_3 en PascalCase (-3). promedio_notas = input(suma) es uso incorrecto de input(). Sin prints."),
        "ej2": (2,  "Variables y total calculados pero sin ningún print() escrito."),
        "ej3": (1,  "Usa ':' en vez de '=' (anotaciones de tipo, no asignaciones). Sin prints ni operaciones."),
        "ej4": (0,  "Vacío."),
        "ej5": (0,  "Vacío."),
        "ej6": (9,  "Errores 1, 2, 3 corregidos. Error 4 (nota_final destruida con print() en la fórmula) y error 5 (coma faltante) sin corregir."),
        "ej7": (0,  "Vacío."),
    },
    "francisco vega": {
        "ej1": (7,  "nota_1, nota_2, nota_3 definidas, promedio calculado. Solo print(promedio) sin etiqueta. Faltan 3 prints individuales (-2), promedio sin etiqueta (-1)."),
        "ej2": (10, "Título presente ('% REPORTE..'), encabezado columnas, sep, 3 filas con variables, total. Perfecto."),
        "ej3": (15, "Variable única saldo_inicial con +=/-=. 6 prints con etiqueta (typo 'supermemrcado' en texto). Caso ideal."),
        "ej4": (15, "2 inputs (precio + porcentaje), cálculo descuento = precio*(pct/100) correcto, precio_final ok, 3 valores en output, título. Perfecto."),
        "ej5": (15, "3 inputs, ganancia_neta y por_persona calculadas, título y 5 datos en output. Perfecto."),
        "ej6": (12, "Errores 1, 2, 4, 5 corregidos. Error 3 (notaparticipacion sin underscore) sin corregir aunque el código funciona."),
        "ej7": (11, "6 inputs ok, promedio correcto (sum/5). gasto_total calculado como presupuesto-gastos en vez de solo la suma de gastos. NameError en saldo (presupuesto_inicial1 typo). Header presente."),
    },
}


# ── Batch 3 ──────────────────────────────────────────────────────────────────
BATCH_3 = {
    "Héctor _": {
        "ej1": (10, "nota1, nota2, nota3 definidas, promedio calculado correctamente, 4 prints con etiqueta. Perfecto."),
        "ej2": (10, "Título, encabezado columnas, sep, 3 filas con variables, total. Perfecto."),
        "ej3": (15, "Variable única Saldo_inicial con +=/-= en cada paso. 6 prints con etiqueta. Caso ideal."),
        "ej4": (15, "2 inputs (precio + porcentaje), cálculo precio*pct/100 correcto, 3 valores en output. Perfecto."),
        "ej5": (14, "3 inputs, ganancia_neta y por_persona calculadas correctamente. 5 datos en output. Sin título '--- REPARTO DEL PUESTO ---' (-1)."),
        "ej6": (12, "Errores 1-4 corregidos. Error 5 (coma faltante en print Participación) sin corregir."),
        "ej7": (19, "6 inputs, total, promedio, saldo correctos. Sin header de resumen (-1)."),
    },
    "Lucas gaspar Valenzuela donoso": {
        "ej1": (1,  "':' en vez de '=' (anotaciones de tipo, no asignaciones). Promedio sin /3. Prints con variables mezcladas. Unterminated string."),
        "ej2": (2,  "Variables y total calculados. Print section: una sola línea con nombres de productos sin encabezado ni filas estructuradas."),
        "ej3": (0,  "Vacío."),
        "ej4": (0,  "Vacío."),
        "ej5": (0,  "Vacío."),
        "ej6": (0,  "Conserva todos los errores originales sin modificar."),
        "ej7": (0,  "Vacío."),
    },
    "Luckas Letelier": {
        "ej1": (5,  "3 variables definidas. Promedio divide por 4 en vez de 3 (-2). Prints imprimen literales no variables (-1). Print promedio roto: imprime solo el texto, no el valor (-2)."),
        "ej2": (7,  "Título (con typo), encabezado, filas con variables propias. Total hardcodeado e incorrecto (63000 vs 75000) (-2). Sin sep parameter (-1)."),
        "ej3": (9,  "Múltiples variables separadas (4/10 calc). Valores calculados correctamente. 6 prints con etiqueta (5/5)."),
        "ej4": (15, "2 inputs (precio + porcentaje), cálculo correcto, 3 valores en output con título. Label dinámico del % en el print. Perfecto."),
        "ej5": (15, "3 inputs, ganancia y por_persona calculadas, título y 5 datos en output. Perfecto."),
        "ej6": (9,  "Errores 1, 2, 3 corregidos. Error 4 (+ en vez de *) y error 5 (coma faltante) sin corregir."),
        "ej7": (20, "6 inputs, gasto_total, promedio, saldo calculados correctamente, header 'resumen semanal' presente. Perfecto."),
    },
    "Maura Isabel Muñoz Gutierrez": {
        "ej1": (8,  "3 variables definidas, 4 prints con etiqueta. Promedio sin paréntesis: nota_1+nota_2+nota_3/3 solo divide nota_3 por 3 (-2)."),
        "ej2": (6,  "Variables definidas, total calculado, sep y 3 filas presentes. Sin título (-2). Print de total muestra unidades en vez de total_recaudado (-2)."),
        "ej3": (1,  "Variables iniciales definidas pero código incompleto: referencias undefined, tras_bono sin valor. Sin prints."),
        "ej4": (3,  "2 inputs presentes. Fórmula completamente incorrecta (descuento = precio + pct). precio_final también errado. 3 prints con valores incorrectos."),
        "ej5": (2,  "3 inputs presentes. Sin cálculo de ganancia_neta ni por_persona. Prints muestran strings literales, no valores."),
        "ej6": (15, "Los 5 errores corregidos. Única en el curso que corrigió el error 5 (coma en print Participación)."),
        "ej7": (5,  "6 inputs presentes, total_gastado calculado. Promedio divide por 6 en vez de 5. Sin prints, sin saldo, sin header."),
    },
    "polar tv": {
        "ej1": (2,  "3 variables definidas. notafinal = suma sin /3 (promedio incorrecto). Solo 1 print con valor incorrecto."),
        "ej2": (8,  "Título, header con sep, total usando variable. Filas con strings hardcodeados en vez de variables (-2)."),
        "ej3": (7,  "Múltiples variables (4/10 calc). Fórmula saldo_final usa deposito_sueldo dos veces en vez de deposito_bono. 6 prints con etiqueta."),
        "ej4": (2,  "2 inputs (precio_inicial y descuento). Fórmula usa precio_original (undefined → NameError). Solo 1 print."),
        "ej5": (3,  "Título presente. 2 inputs reales. ganancia_neta pedida por input en vez de calculada. integrantes hardcodeado. 2 prints."),
        "ej6": (15, "Los 5 errores corregidos, incluyendo error 5 (coma en print Participación)."),
        "ej7": (3,  "Header presente. Pide 'total de gastos' y 'promedio' directamente por input en vez de 5 gastos diarios. Solo saldo calculado. 2 prints."),
    },
    "Sebastian Ulloa": {
        "ej1": (8,  "3 variables via float(input()), promedio calculado correctamente. Solo 1 print con etiqueta (-2 por faltar 3 prints individuales)."),
        "ej2": (4,  "Título y header presentes. Todo hardcodeado como strings, sin variables ni sep parameter. Total 63000 incorrecto (debería ser 75000)."),
        "ej3": (7,  "6 variables hardcodeadas con valores correctos, 6 prints con etiqueta. Sin ninguna operación +=/-=."),
        "ej4": (4,  "2 inputs, descuento_calculado = precio*porcentaje/100 correcto. Código incompleto: sin precio_final ni prints."),
        "ej5": (0,  "Vacío."),
        "ej6": (0,  "Conserva todos los errores originales sin modificar."),
        "ej7": (0,  "Vacío."),
    },
}


# ── Batch 4 ──────────────────────────────────────────────────────────────────
BATCH_4 = {
    "Vicho 11": {
        "ej1": (7,  "nota_1, nota_2, nota_3 definidas, promedio calculado correctamente. Solo print(promedio) sin etiqueta. Faltan 3 prints individuales (-2), promedio sin etiqueta (-1)."),
        "ej2": (3,  "Variables y total calculados. Prints muestran solo números en orden inverso: sin título, sin encabezado, sin sep, sin etiquetas."),
        "ej3": (2,  "Múltiples variables PascalCase hardcodeadas. Solo 1 print (saldo_final). Fórmula omite saldo_inicial y servicios_básicos. Resultado incorrecto."),
        "ej4": (2,  "Todo hardcodeado: precio_original y descuento como literales, sin inputs. precio_final calculado. 1 print sin etiqueta."),
        "ej5": (2,  "Valores hardcodeados. ganancias_netas = 24000/4 (24000 hardcodeado, no computado). Solo 1 print. Sin inputs."),
        "ej6": (15, "Los 5 errores corregidos, incluyendo error 5 (coma en print Participación)."),
        "ej7": (1,  "input(var = value) y print(var = value) son sintaxis inválida. Nada ejecuta. Intento visible de estructura correcta con 6 inputs y 4 prints."),
    },
}


if __name__ == "__main__":
    actualizar(BATCH_4)
