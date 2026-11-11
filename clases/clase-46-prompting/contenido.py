"""Textos compartidos de la Clase 46 (Prompting). Fuente de verdad para generar_clase.py, construir_slides.py y construir_laboratorio.py.

Escenario (Spec v3): una estudiante prepara la prueba de Biología del jueves y le pide ayuda a ChatGPT.
Tres prompts débiles (ninguno toca cámaras, reconocimiento facial ni asistencia, que es el caso de la Prueba 2).
Las respuestas de ejemplo son PREPARADAS a mano (no las generó ChatGPT): sirven de Haz Ahora, de laboratorio y de plan B.
"""

PARTES = ["Rol", "Contexto", "Formato", "Restricción"]

DEBIL_1 = "Explícame la fotosíntesis"
DEBIL_2 = "¿Es mejor estudiar de noche o de día? Dame una recomendación."
DEBIL_3 = "Hazme preguntas para la prueba de historia"
DEBIL_4 = "Escribe un correo para cambiar una prueba"

DEFINICION = "Un prompt es el texto que le escribes a una IA para pedirle algo."
GUIAS = {
    "Rol": "¿Quién queremos que sea la IA?",
    "Contexto": "¿Cuál es la situación, para qué lo necesitamos y para quién es?",
    "Formato": "¿Cómo queremos la respuesta? (lista, tabla, extensión, tono)",
    "Restricción": "¿Qué queremos que respete o que evite?",
}

# Prompts mejorados (modelo): cada uno con las 4 partes y el pedido original
MEJORADOS = {
    1: {
        "pedido": "Explícame la fotosíntesis.",
        "Rol": "Eres un profesor de Biología de 3ro medio.",
        "Contexto": "Tengo prueba el jueves sobre fotosíntesis y me confundo con las etapas.",
        "Formato": "Hazlo en una lista de 5 pasos, una oración por paso, con un ejemplo cotidiano al final y tono cercano.",
        "Restricción": "No uses términos universitarios sin definirlos y no pases de 150 palabras.",
    },
    2: {
        "pedido": "¿Es mejor estudiar de noche o de día? Dame una recomendación.",
        "Rol": "Actúa como orientadora de estudio para estudiantes de 3ro medio.",
        "Contexto": "Tengo prueba de Matemática el jueves; me levanto a las 6:30 y después de las 22:00 me da mucho sueño.",
        "Formato": "Responde con una tabla de ventajas y desventajas de cada opción y cierra con una recomendación en una sola frase.",
        "Restricción": "No des una respuesta absoluta: di de qué depende, y evita consejos médicos.",
    },
    3: {
        "pedido": "Hazme preguntas de práctica.",
        "Rol": "Eres un profesor de Historia de 3ro medio.",
        "Contexto": "Tengo prueba el jueves sobre la Revolución Industrial.",
        "Formato": "Que sean 8: 5 de alternativas y 3 de desarrollo breve, de dificultad media, con las respuestas correctas al final y una frase de explicación cada una.",
        "Restricción": "No repitas preguntas ni uses contenidos de otros temas.",
    },
    4: {
        "pedido": "Escribe un correo para cambiar una prueba.",
        "Rol": "Actúa como asistente de redacción para estudiantes de enseñanza media.",
        "Contexto": "Somos un curso de 3ro medio; tenemos tres pruebas el mismo jueves y queremos pedirle al profesor jefe que mueva una a otro día.",
        "Formato": "Que sea breve (máximo 120 palabras), con asunto, saludo y despedida, y un tono respetuoso y claro.",
        "Restricción": "No inventes excusas ni uses un tono exigente; propón dos fechas alternativas.",
    },
}


def armar(n: int) -> str:
    m = MEJORADOS[n]
    return " ".join([m["Rol"], m["Contexto"], m["pedido"], m["Formato"], m["Restricción"]])


# Haz Ahora: respuesta de ejemplo PREPARADA al débil 1 (3 párrafos; genérica, larga y de nivel universitario)
RESPUESTA_HAZ_AHORA = [
    "La fotosíntesis es un proceso anabólico mediante el cual los organismos autótrofos fototrofos transforman la energía lumínica en energía química, "
    "almacenándola en moléculas orgánicas a partir de dióxido de carbono y agua.",
    "Se desarrolla en dos fases: la fase dependiente de la luz, localizada en las membranas tilacoidales de los cloroplastos, donde se producen ATP y NADPH, "
    "y el ciclo de Calvin-Benson, en el estroma, donde la enzima RuBisCO fija el carbono.",
    "La eficiencia del proceso depende de factores como la intensidad lumínica, la concentración de CO₂ y la temperatura, "
    "y constituye la base de las cadenas tróficas y de la producción de oxígeno atmosférico.",
]

# Respuestas de ejemplo preparadas (plan B y laboratorio): lista de oraciones por respuesta
EJEMPLOS = {
    1: {
        "debil": RESPUESTA_HAZ_AHORA,
        "mejorada": [
            "¡Vamos con la fotosíntesis en 5 pasos!",
            "1. Las hojas de la planta captan la luz del sol.",
            "2. Las raíces absorben agua y las hojas toman dióxido de carbono del aire.",
            "3. Con la luz, la planta transforma el agua y el dióxido de carbono en glucosa, que es su alimento.",
            "4. Como resultado, libera oxígeno al aire.",
            "5. La planta guarda la glucosa para crecer.",
            "Ejemplo cotidiano: es como cocinar usando el sol como cocina.",
        ],
    },
    2: {
        "debil": [
            "Estudiar de día es siempre mejor.",
            "Durante el día tu mente está más despejada y aprovechas más el tiempo.",
            "La noche no es recomendable porque interrumpe el sueño.",
            "Recomendación: estudia de día y duerme temprano.",
        ],
        "mejorada": [
            "Depende de tu rutina: como te levantas a las 6:30 y después de las 22:00 te da mucho sueño, conviene combinar ambas opciones.",
            "De día (en la tarde, al llegar a casa): ventajas: estás más despierto y puedes repasar con calma; desventajas: hay más distracciones.",
            "De noche (antes de las 22:00): ventajas: hay silencio; desventajas: llegas cansado y duermes menos.",
            "Recomendación: estudia 45 minutos en la tarde y repasa 15 minutos antes de las 22:00, y ajusta según cómo te sientas.",
        ],
    },
    3: {
        "debil": [
            "Preguntas de historia: 1. ¿En qué año comenzó la Primera Guerra Mundial?",
            "2. ¿Quién fue Napoleón Bonaparte?",
            "3. ¿Qué fue la Revolución Francesa?",
            "4. ¿Qué caracteriza a la Edad Media?",
        ],
        "mejorada": [
            "Alternativas: 1. ¿Qué invento impulsó la producción textil en Inglaterra? 2. ¿Qué energía movía las primeras fábricas? "
            "3. ¿Qué cambio vivieron las ciudades? 4. ¿Qué clase social creció con las fábricas? 5. ¿Qué medio de transporte acortó las distancias?",
            "Desarrollo breve: 6. Explica por qué el trabajo en fábricas cambió la vida de las familias. "
            "7. Compara el trabajo artesanal con el trabajo en fábrica. 8. Menciona una consecuencia ambiental de la industrialización.",
            "Respuestas al final, con una frase de explicación cada una.",
        ],
    },
    4: {
        "debil": [
            "Estimado destinatario:",
            "Le escribo para solicitar el cambio de una prueba. Agradezco su atención.",
            "Saludos cordiales.",
        ],
        "mejorada": [
            "Asunto: Solicitud de cambio de fecha de una prueba",
            "Estimado profesor jefe:",
            "Somos el 3ro medio. Este jueves tenemos tres pruebas el mismo día y nos preocupa no alcanzar a prepararlas bien. "
            "¿Sería posible mover una de ellas a la semana siguiente, por ejemplo al lunes o al martes? Quedamos atentos a lo que usted considere mejor.",
            "Muchas gracias por su disposición. Saludos cordiales, 3ro medio.",
        ],
    },
}

# Laboratorio A1: frases a clasificar (frase, parte)
FRASES_A1 = [
    ("Eres un profesor de Biología de 3ro medio.", "Rol"),
    ("Tengo prueba el jueves y me confundo con las etapas.", "Contexto"),
    ("Respóndeme en una lista de 5 pasos.", "Formato"),
    ("No uses términos universitarios sin definirlos.", "Restricción"),
    ("Actúa como orientadora de estudio.", "Rol"),
    ("Soy estudiante de 3ro medio y estudio después de clases.", "Contexto"),
    ("Usa una tabla con ventajas y desventajas.", "Formato"),
    ("No me des consejos médicos.", "Restricción"),
]

# Laboratorio A2: prompts parciales y qué partes faltan
ITEMS_A2 = [
    ("Eres profesor de Biología. Explícame la fotosíntesis.", ["Contexto", "Formato", "Restricción"]),
    ("Tengo prueba el jueves de Historia. Hazme preguntas.", ["Rol", "Formato", "Restricción"]),
    ("Eres orientador de estudio. Quiero estudiar de noche porque de día trabajo. ¿Me conviene? Responde en una tabla.", ["Restricción"]),
    ("Eres una profesora de Lenguaje. Estoy preparando una disertación. Respóndeme en una lista corta y sin tecnicismos.", []),
]

# Laboratorio A3: elegir la cita que prueba la consecuencia
ITEMS_A3 = [
    {
        "prompt": DEBIL_1, "falta": "Contexto y Formato", "consecuencia": "la respuesta es demasiado técnica para un estudiante de 3ro medio",
        "oraciones": RESPUESTA_HAZ_AHORA[:2] + ["Espero que esta información te sirva.", "Puedes preguntarme lo que quieras."],
        "correcta": 0,
        "porque": "Esa frase usa «autótrofos fototrofos» y «anabólico» sin explicarlos: es lo que prueba el nivel universitario. Las otras dos son relleno y no muestran la consecuencia.",
    },
    {
        "prompt": DEBIL_2, "falta": "Contexto y Restricción", "consecuencia": "la respuesta toma una postura sin matices",
        "oraciones": ["Estudiar de día es siempre mejor.", "Recuerda tomar agua mientras estudias.", "Descansa un poco entre materias.",
                      "Puedes pedirme más ayuda."],
        "correcta": 0,
        "porque": "«siempre mejor» es una postura absoluta, sin considerar la rutina de quien pregunta: eso es lo que prueba la consecuencia.",
    },
]

OBJETIVO = "Escribir prompts de IA de forma correcta con flexibilidad."
URL_FORM = "https://forms.gle/sjRpbgmQzrpkEBsH9"
TEMA_FORM = "Prompting"
URL_HUB = "https://clases-ia-mario-bertero.vercel.app"
URL_SLIDES = f"{URL_HUB}/clase-46/"
URL_LAB = f"{URL_HUB}/clase-46/laboratorio/"
