# Historial — Clase 28

## 2026-08-26 — Especificación aprobada
- Objetivo: Extraer caracteres y segmentos específicos de una cadena de texto mediante índices y rebanadas, con precisión (actitud: Precisión).
- Alcance recortado respecto a Picuino N°21+N°22 en sesión de diseño previa (ver `Prompt.md`): solo índice y rebanada, sin creación/unión/repetición de cadenas ni recorrido con `for` (movido a Clase N°29 nueva).
- Estructura de 5 pasos propuesta y aprobada en una iteración, con un ajuste: Diego pidió fusionar los conceptos del ICN — índice positivo + índice negativo en un solo concepto, y rebanada + rebanada fuera de rango en otro — quedando 3 conceptos en vez de 5.
- Escenario compartido Haz Ahora/ICN/Guiada: código de sala de un torneo de videojuego móvil. Independiente con Ejercicios 0a/0b (índice puntual y rebanada), 1 (código de seguimiento de pedido), 2 (tag de clan gamer), 3 contextualizado (RUT — cuerpo y dígito verificador) y 4 desafío (código de acceso simétrico, sin usar `[::-1]` para no adelantar sintaxis).
