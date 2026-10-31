"""Step-by-step slides of the pipeline (Clase 41) as 1920x1080 SVG strings, plus speaker notes.

diapositivas() -> list of (title, svg, notes). construir.py renders them to PNG and builds the .pptx.
"""
from diagramas import (AZUL, AZUL_BG, INK, MORADO, MORADO_BG, NARANJA, NARANJA_BG, SLATE, TEAL, TEAL_BG,
                       bloque_entrenamiento, bloque_prueba, box, flecha, lines, text, tabla, tira, wrap_svg)

SUB = "Caso: riego automatizado de una viña de Isla de Maipo, como Santa Ema (datos ficticios)"


def titulo(t, sub=None):
    b = [text(60, 82, t, 54, "bold")]
    if sub:
        b.append(text(60, 128, sub, 30, fill=SLATE))
    return b


def panel(x, y, w, h, encabezado, filas, color, bg, size=32, step=48):
    return [box(x, y, w, h, bg, color), text(x + 30, y + 54, encabezado, 34, "bold", fill=color),
            lines(x + 30, y + 84 + size, filas, size, step)]


def paso(i, nombre, grupo, izquierda, visual, notas):
    b = titulo(f"Paso {i + 1} · {nombre}", grupo) + tira(activo=i)
    b += panel(60, 470, 870, 565, "Qué hacemos", izquierda, "#334155", "#ffffff", 36, 58)
    b += visual
    svg = wrap_svg("".join(b), f"Paso {i + 1}: {nombre}", " ".join(izquierda))
    return (f"Paso {i + 1} · {nombre}", svg, notas)


def barra(x, y, w, texto_, fill, stroke, size=28, h=54, color=INK):
    return [box(x, y, w, h, fill, stroke, radius=12), text(x + w // 2, y + h // 2 + int(size * 0.35), texto_, size, "bold", "middle", color)]


def diapositivas():
    out = []
    # 1 · Portada
    b = [box(0, 0, 40, 1080, AZUL, AZUL, radius=0), text(120, 400, "El recorrido de los datos", 92, "bold"),
         text(120, 490, "Cómo aprende un modelo y cómo comprobamos si es capaz de predecir", 42, fill=SLATE),
         text(120, 580, SUB, 32, fill=SLATE), text(120, 960, "Clase 41 · 3ro medio · Inteligencia artificial", 30, fill=SLATE)]
    out.append(("Portada", wrap_svg("".join(b), "El recorrido de los datos", SUB),
                "Abrimos con la pregunta: ¿cómo sabe una IA si lo que aprendió sirve? Hoy lo vemos paso a paso con un solo caso. "
                "Antes de partir, activa a la voz si quieres que plantee la pregunta."))
    # 2 · El caso
    b = titulo("Nuestro caso: ¿hay que regar mañana?", SUB)
    b += panel(60, 190, 870, 620, "Lo que sabemos hoy", ["Humedad del suelo", "Temperatura", "Días sin lluvia", "",
                                                         "Son las VARIABLES:", "lo que el modelo recibe."], AZUL, AZUL_BG, 36, 56)
    b += panel(990, 190, 870, 620, "Lo que queremos saber", ["¿Hay que regar mañana?", "", "Sí  /  No", "",
                                                             "Es la ETIQUETA:", "lo que queremos que prediga."], NARANJA, NARANJA_BG, 36, 56)
    b += barra(60, 850, 1800, "Un sistema automatizado de riego podría usar la respuesta para abrir o no las válvulas",
               "#ffffff", SLATE, 28, 80)
    out.append(("El caso", wrap_svg("".join(b), "Nuestro caso", "Variables y etiqueta del caso del riego."),
                "Presenta el caso con datos ficticios. Pregunta al curso qué datos creen que ayudarían a decidir si regar. "
                "Aclara que son datos inventados, inspirados en una viña de Isla de Maipo como Santa Ema."))
    # 3 · Recorrido completo
    b = titulo("El recorrido completo: 7 pasos", SUB) + tira()
    b += panel(60, 470, 1800, 565, "Cuatro bloques", ["PREPARAR: definimos el problema, reunimos los datos y los separamos en dos sets.",
                                                        "ENTRENAR: aquí la computadora aprende.",
                                                        "EVALUAR: aquí vemos si es capaz de predecir.",
                                                        "USAR: lo aplicamos en casos nuevos y revisamos.", "",
                                                        "Hoy lo vemos paso a paso. En las próximas clases lo programamos."],
               "#334155", "#ffffff", 34, 62)
    out.append(("Recorrido completo", wrap_svg("".join(b), "El recorrido completo", "Los siete pasos en cuatro bloques."),
                "Muestra el mapa completo antes de entrar al detalle. Marca los cuatro bloques con el puntero."))
    # 4–10 · Un paso por diapositiva
    v1 = [box(1010, 520, 810, 200, "#ffffff", NARANJA), text(1415, 635, "¿Hay que regar mañana?", 52, "bold", "middle")]
    v1 += barra(1010, 760, 390, "Sí", NARANJA_BG, NARANJA, 40, 100) + barra(1430, 760, 390, "No", NARANJA_BG, NARANJA, 40, 100)
    out.append(paso(0, "Definir el problema", "PREPARAR",
                    ["Decidimos qué queremos responder.", "Tiene que ser una pregunta de sí o no", "con la que el modelo pueda ayudarnos."],
                    v1, "Pregunta al curso: ¿qué pregunta de sí o no nos serviría en una viña? Recoge dos o tres ideas y quédate con la del riego."))

    anchos2 = [195, 195, 215, 205]
    cab = ["Humedad", "Temperatura", "Días sin lluvia", "¿Se regó?"]
    v2 = barra(1010, 505, 597, "VARIABLES: lo que el modelo recibe", AZUL_BG, AZUL, 24, 46) \
        + barra(1618, 505, 197, "ETIQUETA", NARANJA_BG, NARANJA, 24, 46)
    v2 += tabla(1010, 565, anchos2, cab, [["32 %", "27 °C", "5", "Sí"], ["58 %", "19 °C", "1", "No"], ["25 %", "31 °C", "7", "Sí"]],
                alto=52, size=25)
    v2 += [text(1010, 905, "Cada fila es un día de riego anterior.", 28, fill=SLATE)]
    out.append(paso(1, "Reunir datos: variables y etiqueta", "PREPARAR",
                    ["Juntamos registros de días anteriores.", "Variables: lo que el modelo recibe.", "Etiqueta: lo que queremos que prediga."],
                    v2, "Insiste en la diferencia: variables = lo que sabemos hoy; etiqueta = la respuesta que queremos predecir. "
                        "La etiqueta ya viene en los registros pasados porque esos días ya se decidió y se sabe qué pasó."))

    v3 = barra(1010, 505, 810, "SET DE DATOS · 60 filas", "#e2e8f0", SLATE, 28, 56)
    v3 += [flecha(1335, 563, 1335, 620, TEAL), flecha(1745, 563, 1745, 620, MORADO)]
    v3 += [box(1010, 625, 650, 200, "#f0fdfa", TEAL), text(1335, 705, "SET DE ENTRENAMIENTO", 30, "bold", "middle", "#115e59"),
           text(1335, 755, "48 filas · la mayoría", 28, anchor="middle"),
           box(1670, 625, 150, 200, "#f5f3ff", MORADO), text(1745, 705, "SET DE", 26, "bold", "middle", "#4c1d95"),
           text(1745, 738, "PRUEBA", 26, "bold", "middle", "#4c1d95"), text(1745, 785, "12 filas", 26, anchor="middle")]
    v3 += [text(1010, 905, "El set de prueba se guarda aparte antes de entrenar.", 28, "bold", fill="#4c1d95")]
    out.append(paso(2, "Separar en dos sets de datos", "PREPARAR",
                    ["Separamos las filas en dos sets:", "• Set de entrenamiento: la mayoría.", "• Set de prueba: una parte que se", "   guarda aparte, sin tocarla."],
                    v3, "Este es el paso que más se olvida. Usa la analogía del estudio y la prueba: estudiamos con unos ejercicios y nos "
                        "evalúan con otros que no vimos. Aquí conviene detenerse y preguntar por qué creen que se guarda aparte."))

    ent = bloque_entrenamiento(x=1010, y=500, w=810, h=335)
    ent += [flecha(1415, 840, 1415, 885, TEAL), box(1215, 890, 400, 130, "#fffbeb", "#b45309"),
            text(1415, 945, "MODELO", 34, "bold", "middle"), text(1415, 988, "aprendió patrones", 26, anchor="middle", fill=SLATE)]
    out.append(paso(3, "Entrenar el modelo", "ENTRENAR",
                    ["AQUÍ LA COMPUTADORA APRENDE.", "Mira el set de entrenamiento:", "variables y etiqueta, y busca patrones.",
                     "Ajusta el modelo para acertar cada", "vez más con esas filas."],
                    ent, "Enfatiza: entrenar es aprender de ejemplos que traen su respuesta (la etiqueta). Todavía no sabemos si aprendió bien."))

    pru = bloque_prueba(x=1010, y=500, w=810, h=335)
    pru += [flecha(1415, 840, 1415, 885, MORADO), box(1165, 890, 500, 130, "#fffbeb", "#b45309"),
            text(1415, 945, "El modelo predice:", 30, "bold", "middle"), text(1415, 990, "fila 1: «Sí»  ·  fila 2: «No»", 28, anchor="middle", fill=SLATE)]
    out.append(paso(4, "Predecir sobre el set de prueba", "EVALUAR",
                    ["AQUÍ VEMOS SI ES CAPAZ DE PREDECIR.", "El modelo ya está entrenado.", "Le damos solo las variables del",
                     "set de prueba, sin la etiqueta,", "y nos responde.", "Es como un examen: no vio estas filas."],
                    pru, "La etiqueta de la prueba existe, pero la escondemos al modelo: la usamos después para corregir. "
                         "Voz: «Colega, verifica comprensión del pipeline.» puede ir al terminar este paso o el siguiente."))

    filas = [("1", "Sí", "Sí", "Acertó"), ("2", "No", "No", "Acertó"), ("3", "Sí", "No", "Falló"), ("4", "No", "No", "Acertó")]
    v6 = []
    for j, (cab_, w) in enumerate([("Fila", 120), ("Predijo", 220), ("Realidad", 220), ("Resultado", 250)]):
        x = 1010 + sum(a for a in [120, 220, 220, 250][:j])
        v6 += barra(x, 505, w - 8, cab_, MORADO_BG, MORADO, 26, 52)
        for r, fila in enumerate(filas):
            malo = fila[3] == "Falló"
            v6 += barra(x, 570 + r * 66, w - 8, fila[j], NARANJA_BG if (malo and j == 3) else "#ffffff",
                        NARANJA if (malo and j == 3) else MORADO, 28, 56)
    v6 += [text(1010, 905, "Ejemplo: acertó 3 de 4.", 34, "bold"), text(1010, 950, "En nuestro set de prueba serían 12 filas.", 28, fill=SLATE)]
    out.append(paso(5, "Evaluar: ¿cuántas veces acertó?", "EVALUAR",
                    ["Comparamos lo que predijo con lo que", "realmente pasó en el set de prueba.", "Contamos cuántas veces acertó.",
                     "Eso nos dice cómo le irá con casos nuevos."],
                    v6, "Todavía no hablamos de 'accuracy': la idea es solo contar aciertos. El nombre llega el lunes 9."))

    v7 = tabla(1010, 520, [195, 195, 215, 205], ["Humedad", "Temperatura", "Días sin lluvia", "Predicción"],
               [["30 %", "29 °C", "6", "Regar"]], alto=56, size=25)
    v7 += barra(1010, 680, 810, "Datos de mañana → el modelo responde «Regar»", NARANJA_BG, NARANJA, 28, 70)
    v7 += [text(1010, 840, "Y después revisamos:", 32, "bold"), text(1010, 890, "¿sigue acertando con los días nuevos?", 30, fill=SLATE)]
    out.append(paso(6, "Usar en casos nuevos y revisar", "USAR",
                    ["Ya sabemos qué tan bien funciona.", "Lo usamos con los datos de mañana", "y revisamos si sigue acertando.",
                     "Si deja de acertar, volvemos a entrenarlo."],
                    v7, "Cierra el ciclo: un modelo no se entrega y se olvida; se revisa. Eso conecta con el discernimiento más adelante."))

    # 11 · Contraste entrenamiento / prueba
    b = titulo("Entrenar no es predecir", "Dos sets distintos, dos trabajos distintos")
    b += panel(60, 190, 870, 640, "SET DE ENTRENAMIENTO", ["Aquí la computadora", "APRENDE.", "", "Ve las variables", "y la etiqueta (la respuesta)."],
               TEAL, "#f0fdfa", 44, 72)
    b += panel(990, 190, 870, 640, "SET DE PRUEBA", ["Aquí vemos si es capaz", "de PREDECIR.", "", "No ve la etiqueta", "cuando responde."],
               MORADO, "#f5f3ff", 44, 72)
    b += barra(60, 870, 1800, "Si mezclamos los dos, no sabemos si aprendió o si solo se acuerda de las filas", NARANJA_BG, NARANJA, 30, 100)
    out.append(("Entrenar no es predecir", wrap_svg("".join(b), "Entrenar no es predecir", "Set de entrenamiento y set de prueba."),
                "Esta es la diapositiva clave. Haz que dos estudiantes la expliquen con sus palabras. Frase para quedarse: "
                "el set de entrenamiento es donde aprende; el set de prueba es donde vemos si predice."))
    # 12 · Error típico
    b = titulo("Error típico: evaluar con lo mismo que se entrenó")
    b += panel(60, 160, 870, 700, "Lo que pasó", ["Entrenamos con 60 filas", "y evaluamos con esas mismas 60.", "", "Resultado: acertó 60 de 60.", "",
                                                  "¿Es un modelo perfecto?"], NARANJA, NARANJA_BG, 40, 64)
    b += panel(990, 160, 870, 700, "Por qué no lo sabemos", ["Ya vio esas filas.", "Es como un examen con las preguntas", "que ya estudiamos de memoria.", "",
                                                             "No mide cómo le irá con casos nuevos."], SLATE, "#ffffff", 38, 62)
    b += barra(60, 900, 1800, "Solución: guardar un set de prueba aparte ANTES de entrenar", TEAL_BG, TEAL, 32, 100)
    out.append(("Error típico", wrap_svg("".join(b), "Error típico", "Evaluar con los mismos datos del entrenamiento."),
                "Prepara la actividad P4 (caza el error). Pregunta: ¿qué está mal acá? Deja que lo descubran antes de decirlo."))
    # 13 · Resumen
    b = titulo("Resumen del recorrido") + tira()
    b += panel(60, 470, 1800, 565, "Para llevarnos", ["Variables: lo que el modelo recibe. Etiqueta: lo que queremos que prediga.",
                                                      "Set de entrenamiento: aquí la computadora aprende.",
                                                      "Set de prueba: aquí vemos si es capaz de predecir.",
                                                      "Evaluamos con el set de prueba, nunca con el de entrenamiento."],
               "#334155", "#ffffff", 34, 76)
    out.append(("Resumen", wrap_svg("".join(b), "Resumen", "Ideas clave del recorrido."),
                "Cierra con el resumen. Voz: «Colega, verifica comprensión del pipeline.» (por qué guardamos datos aparte; "
                "qué diferencia hay entre entrenar y predecir)."))
    # 14 · A practicar
    b = [box(0, 0, 40, 1080, TEAL, TEAL, radius=0), text(120, 440, "Ahora practicamos", 84, "bold"),
         text(120, 560, "Vamos a la actividad P1 de la página", 52, fill=SLATE),
         text(120, 640, "(cambiamos a la página 2: entregamos el código en la sala)", 32, fill=SLATE)]
    out.append(("A practicar", wrap_svg("".join(b), "Ahora practicamos", "Ir a la actividad P1 de la página."),
                "Entrega el código de la página 2 y pasa a las actividades. En la página las actividades usan otro ejemplo: "
                "el sistema de climatización de las bodegas donde fermenta la uva."))
    return out
