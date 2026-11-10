# Prompt de sesión — Clase N°43 v2: «La neurona aprende sola» (reformulación)

**Fecha de la clase:** martes 2026-11-10 (**hoy** — ejecutar esto primero)
**Estado:** Spec v2 no escrita. La v1 (`Clase 43 - Neurona - *.ipynb`, ajuste manual de pesos) queda **archivada sin dictar**; no tocarla. Todo archivo nuevo lleva el sufijo `v2` (`Clase 43 - Neurona v2 - Spec.md`, `... - Clase.ipynb`, etc.).
**Flujo:** liviano (Spec → gate → Colab + Solucionario + Guía Docente Voz + slides + Ticket al Form → gate → push de la carpeta). Lee antes: `clases/clases-znoviembre/Plan Noviembre - Checklist y traspaso entre sesiones.md` (sección «Calendario v6»), «Reglas vigentes desde 2026-11-07» de `disenar-clase/SKILL.md` y la sección «Bloque IA» del `CLAUDE.md`.

## Qué cambia respecto a la v1 y al plan del traspaso

1. **Misma base de datos que la 42b (el wifi del liceo), ya cargada.** Nada de dataset nuevo de colmenas (el B1 del traspaso queda **descartado**). Usar `clases/clase-42b-tabla-a-listas/datos_wifi_verificados.json`, trío de columnas `dispositivos_conectados`, `estudiantes_viendo_video`, `horas_desde_reinicio`; etiqueta «¿se cayó el wifi?» (1 = sí). Filas 1–16 = *train*, 17–20 = *test* (`[0, 1, 1, 0]`).
2. **Las listas `entradas_train`, `etiquetas_train`, `entradas_test`, `etiquetas_test` vienen ya escritas en la primera sección del Colab; los estudiantes solo las ejecutan** (hoy no tipean datos: el foco es el modelo). Recordar en una línea que eso lo hicieron a mano en la 42b.
3. **Foco de la clase:** (a) explicar qué es una **neurona** (recibe las 3 columnas, **pondera** cada una —le da más o menos importancia—, suma y decide 0 o 1; los pesos los **ajusta sola la computadora** al entrenar) y (b) **crearla con el mismo proceso del árbol**: crear → `fit` → `predict` → `accuracy_score`. Solo cambia la línea que crea el modelo.
4. **Analizar y comparar** el resultado con el árbol de la 42b sobre **los mismos datos**: verificado con scikit-learn 1.9.1 → árbol `accuracy = 1.0` (4/4), neurona `accuracy = 0.75` (3/4; falla la fila 18). Plantear la pregunta «¿cuál usarían y por qué?» y recordar que con 4 filas cada fila vale 25 %.
5. **«Los `import` raros van SIEMPRE en la primera celda, ejecutada primero».** Insistirlo en el Colab (celda inicial titulada «🔧 Ejecuta esta celda primero» con `DecisionTreeClassifier`, `MLPClassifier`, `accuracy_score`) y en la Guía del colega. Esta es la regla **de aquí en adelante para todos los cuadernos y pruebas** (la Prueba 1 ya lo hace) para que no se atasquen escribiendo `from sklearn... import ...`.

## Llamada del modelo (idéntica a la de la Prueba 1 — no cambiarla)

```python
modelo = MLPClassifier(hidden_layer_sizes=(), max_iter=2000, random_state=0)
modelo.fit(entradas_train, etiquetas_train)
predicciones = modelo.predict(entradas_test)
exactitud = accuracy_score(etiquetas_test, predicciones)
print("Accuracy de la neurona:", exactitud)
```

`hidden_layer_sizes=()` = **una sola neurona** (sin capas ocultas); mencionarlo en un `<details>` y no profundizar. **Decisión de Diego (2026-11-10) sobre «abrir la caja» (`coefs_`, `intercepts_`): SÍ se muestran los pesos (opción b).** Con esta llamada (solver `adam` por defecto, sin escalar) los pesos **cambian según la semilla** y no siempre se leen bien (`random_state=0`: `[-0.035, 0.376, 0.098]`; `random_state=1`: `[-0.001, 0.767, -0.099]`; en ambos «dispositivos» casi no pesa, aunque en la tabla sea una columna clara). Por eso la clase debe:
1. Mostrar `modelo.coefs_` e `intercepts_` y explicar que son **las importancias («pesos») que la computadora ajustó sola**.
2. **Reiterar la importancia de `random_state`:** es el número que fija el punto de partida aleatorio del entrenamiento; con otra semilla los pesos (y a veces el `accuracy`) **salen distintos**. Mostrarlo en vivo cambiando `random_state` de 0 a 1 y volviendo a imprimir. Insistir en que en las pruebas **siempre se deja `random_state=0`** para que todos obtengan lo mismo.
3. Advertir, en una línea y **sin profundizar**, que los números también pueden variar por **otras razones técnicas** (por ejemplo, cómo termina de procesar el entrenamiento) y que **no las veremos en este curso**.
4. No leer los pesos como «verdad absoluta» ni usarlos para concluir qué columna es «la importante» (hoy «dispositivos» sale casi en cero); quedarse en la idea de que **existen y los ajusta la computadora**.

Con `solver="lbfgs"` los pesos son estables y positivos, pero la llamada ya no coincide con la de la prueba: **no usar `lbfgs` sin que Diego lo apruebe.**

## Alineación con la Prueba 1 (leer `clase-45-prueba-1-tecnica/Clase 45 - Prueba 1 Técnica - Prueba.ipynb` y su Temario)

La prueba pide: crear/entrenar/evaluar árbol **y** neurona (B), comparar con números propios (C1), y explicar por qué un test de 4 filas da poca seguridad (C3). Que la guiada de la 43 v2 haga exactamente ese recorrido con el wifi. Sugerencia de ejercicio guiado único: entrenar la neurona con los datos listos y **escribir 2 líneas** comparando su `accuracy` con el del árbol de la 42b.

## Molde y entregables

- Molde de clase de IA (reglas 1–11 del SKILL): la computadora aprende sola, historia continua del wifi, «el problema tenía 6 columnas, pero el encargado pide estas 3», «filas», concepto final «Revisar» (leer resultado + precisión) y detalles de hiperparámetros en `<details>`. Un solo ejercicio obligatorio (la guiada); los extras sin tiempo asignado.
- **Recordatorio puente** (ayer → hoy es distinto → próxima clase) tras el Haz Ahora; la próxima clase es el **lunes 16 (mini-LLM)**.
- **Slides animadas** en `sitio-hub/clase-43-v2/` (una por concepto del ICN, Haz Ahora, «Para pensar», resumen). **Ticket al Form** (Colab solo con el link; preguntas en el PPT local y el Solucionario + JSON de respuestas). **Guía Docente Voz** (el colega solo habla cuando Diego la activa).
- Actitud: Diego la elige entre 3–4 opciones que le propongas.
- Cierre: commit/push **solo de `clases/clase-43-neurona/`** con `git add` + `git commit` con pathspec propio; el `Ticket de Salida.pptx` NO se pushea antes de dictar la clase.
