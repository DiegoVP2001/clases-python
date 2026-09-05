# Historial — Clase 32

## 2026-08-27 — Especificación aprobada
- Objetivo: Aplicar métodos de cadenas y operadores de texto para transformar datos desordenados en un formato limpio y estándar, con orden.
- Actitud: Orden. Contexto: Los Mellis Al Paso (negocio ancla único de toda la clase, primer caso de la skill `referencia-empresas-isla-de-maipo`).
- Sesión iniciada el 2026-08-26 (cortada por tokens): se acordaron actitud, contexto y recorte de contenido. Retomada el 2026-08-27: se cerró el objetivo/propósito (Diego pidió simplificar el objetivo a "cadenas y operadores de texto", sacando la lista de sintaxis Python) y se aprobó la estructura completa de 5 pasos en una sola iteración, sin ajustes.
- Piloto en curso: formato de propósito con compañía real (ver `disenar-clase/SKILL.md`). Pendiente confirmar con Diego al cerrar la clase si se generaliza.
- Contenido recortado de la ficha Picuino N°23: sin `swapcase()`, sin `in`/`find()` (movidos a Clase 33, renumerada desde Clase 32 el 2026-09-03), sin f-strings (sacadas del currículo cercano).

## 2026-08-27 — Colab de clase aprobado
- Archivos: `Clase.ipynb`, `Solucionario.ipynb`, `Ticket de Salida Respuestas.json`, `Ticket de Salida.pptx`.
- Generado con la skill `generar-colab-clase`. Ambos notebooks se ejecutaron sin errores (`nbconvert --execute`) y las 6 soluciones de Independiente (0a, 0b, 1-4) se verificaron a mano contra sus `verificar_ejercicio_N()`.
- Dos bugs de `crear_colab.py` detectados y corregidos en el camino (afectan a cualquier clase futura, no solo esta):
  1. El regex del título de concepto del ICN cortaba mal si el título traía un `*` literal (ej. "Operadores `+` y `*` en strings") — el Concepto 1 completo se perdía. Corregido para cortar solo en un `**` real de cierre.
  2. El spec tenía `**Celda de verificación:**` después de `- Solución:` en los 6 ejercicios — el parser corta el bloque en `- Solución:`, así que las 6 celdas de verificación se perdían. Se reordenó el spec al orden canónico (verificación antes de solución).
- Aprobado por Diego sin pedir cambios adicionales.
