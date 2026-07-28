---
name: generar-dodona-ejercicios
description: Genera la estructura de ejercicios Dodona con TESTed desde una propuesta JSON aprobada. Usa esta skill cuando Diego apruebe una propuesta Dodona y pida crear, ejecutar, materializar o generar los archivos para subir ejercicios a Dodona.
---

# Skill: Generar ejercicios Dodona

## Propósito

Crear carpetas Dodona listas para revisión local desde `dodona/propuestas/<slug>.json`. Por defecto escribe en el repo externo `dodona-ejercicios-profesor/`, conectado a `https://github.com/DiegoVP2001/dodona-ejercicios-profesor.git`. También genera un Jupyter notebook con todos los ejercicios del set en `dodona/<set_slug>/<set_slug>-ejercicios.ipynb`. Esta skill ejecuta el workflow solo después de aprobación explícita de la propuesta.

## Requisitos previos

- Debe existir una propuesta aprobada en JSON, creada por `disenar-dodona-ejercicios`.
- La propuesta debe seguir `references/dodona-estructura.md` y el esquema de la skill de diseño.
- Si Diego no aprobó la propuesta, vuelve a `disenar-dodona-ejercicios`.

## Flujo

1. Lee la propuesta JSON aprobada.
2. Revisa que cada ejercicio tenga `slug`, `title`, `type`, `statement_md`, `tests` y `solution_py`.
3. Ejecuta el generador:

```powershell
& "C:\Program Files\GIMP 3\bin\python.exe" ".claude/skills/generar-dodona-ejercicios/scripts/generar_dodona.py" "dodona/propuestas/<slug>.json" --output-root "dodona-ejercicios-profesor"
```

Si hay otro Python disponible en PATH, puede usarse `python` con el mismo script.

4. Activa `validar-dodona-ejercicios` sobre la carpeta generada.
5. Si los ejercicios son `io`, ejecuta las soluciones oficiales contra los casos del JSON cuando sea posible y confirma que el `stdout` coincide.
6. Reporta archivos creados, ejercicios generados y cualquier advertencia.

## Salida esperada

```text
dodona-ejercicios-profesor/
  dirconfig.json
  <set_slug>/
    dirconfig.json
    <exercise_slug>/
      config.json
      description/
        description.es.md
        description.en.md
      evaluation/
        suite.yaml
      solution/
        solution.py

dodona/
  <set_slug>/
    <set_slug>-ejercicios.ipynb   ← notebook Jupyter generado automáticamente
```

El notebook tiene una sección por ejercicio (celda markdown con enunciado + celda de código vacía) y al final una sección "📋 Soluciones" con `<details>` colapsables por ejercicio. Úsalo para compartir el set como práctica offline o como respaldo de los ejercicios Dodona.

## Opciones del script

```
generar_dodona.py propuesta.json [--output-root DIR] [--jupyter-root DIR] [--no-jupyter] [--force]
```

- `--output-root`: carpeta destino para las carpetas Dodona (default: `dodona-ejercicios-profesor`)
- `--jupyter-root`: carpeta raíz donde se escribe el notebook (default: `dodona`)
- `--no-jupyter`: omite la generación del notebook
- `--force`: sobreescribe el set si ya existe

## Reglas

- No publiques ni hagas `git push` a Dodona sin instruccion explicita.
- Antes de generar, verifica que `dodona-ejercicios-profesor/` exista y esté limpio o que los cambios pendientes sean del workflow actual.
- Despues de generar y validar, si Diego autoriza publicar, crea commit en `dodona-ejercicios-profesor/` y usa `git -c http.sslBackend=openssl push`.
- El push ya fue probado en este computador: Diego autorizo GitHub y confirmo que el piloto se ve en Dodona.
- Aunque el push funcione, nunca lo ejecutes sin autorizacion explicita de Diego.
- No edites ejercicios generados a mano si el cambio viene de la propuesta; ajusta el JSON y regenera.
- Usa `access: private` por defecto.
- Usa `evaluation.handler: tested` y `evaluation.test_suite: suite.yaml`.
- Para `stdout` no vacío, termina con `\n`.
- Si un test de la propuesta tiene `"hidden": true`, el generador debe ponerlo en un tab con `hidden: true`.
- El generador debe preservar `dodona-ejercicios-profesor/dirconfig.json` si ya existe; no eliminar `time_limit`, `memory_limit` ni `contact`.
- La descripción Markdown generada (`description.es.md`) contiene solo el título y el `statement_md`. **No incluye** el sample inline, `**Contenidos:**`, `_Clase foco:_` ni `_Fuente pedagógica:_` — Dodona renderiza el sample nativamente.

## Recursos

- `scripts/generar_dodona.py`: genera carpetas Dodona + notebook Jupyter desde JSON.
- `references/dodona-estructura.md`: contrato técnico mínimo de Dodona/TESTed usado por este workflow.
