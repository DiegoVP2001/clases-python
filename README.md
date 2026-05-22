# Clases Python 4to Medio — Sistema Claude Code

Sistema para diseñar y producir clases de Python de forma iterativa con Claude Code.

## Estado actual (iteración 1 de 3)

Esta versión incluye:

- ✅ `CLAUDE.md` — Orquestador maestro con defaults del curso
- ✅ `.claude/skills/disenar-clase/` — Skill para el flujo de 5 pasos con aprobación incremental
- ⏳ Skills generadoras (`generar-colab-clase`, `generar-colab-ejercicios`, `generar-ppt-clase`) — iteración 2
- ⏳ Skills de referencia (`referencia-curriculo`, `referencia-bloom`, etc.) — iteración 3

Con la iteración 1 ya puedes **diseñar la especificación de una clase** (objetivo, propósito, estructura de 5 pasos) y guardarla. Aún no puedes generar los archivos finales.

## Instalación local

1. Tener Claude Code instalado (https://docs.claude.com/en/docs/claude-code/quickstart).
2. Tener Python 3.10+ con `pip` disponible (para las skills generadoras de iteraciones 2-3).
3. Copiar esta carpeta completa a tu máquina, por ejemplo a `~/proyectos/clases-python-4tomedio/`.
4. Desde esa carpeta, ejecutar `claude` en tu terminal.

Claude Code detectará automáticamente el `CLAUDE.md` (lo lee al iniciar) y las skills en `.claude/skills/` (las activa por descripción cuando aplican).

## Primer uso

Una vez en Claude Code dentro del proyecto, prueba:

```
Vamos a diseñar la clase 3 de Picuino.
```

Claude debería:
1. Consultar el currículo (en iteración 1 aún no tiene la referencia, así que le tendrás que pasar tú el documento `picuino_python_clases_1_33_sintesis.md` o copiar la info relevante)
2. Confirmar contexto y preguntar solo lo esencial
3. Proponer objetivo y propósito → esperar tu aprobación
4. Proponer estructura de 5 pasos → esperar tu aprobación
5. Guardar `clases/clase-03-variables/00-spec.md` y `historial.md`

## Estructura del proyecto

```
clases-python-4tomedio/
├── CLAUDE.md                    # Orquestador (se carga siempre)
├── README.md                    # Este archivo
├── .claude/
│   └── skills/
│       └── disenar-clase/
│           └── SKILL.md         # Skill del flujo pedagógico
├── clases/                      # Cada clase en su carpeta (se crean a medida)
│   └── clase-NN-tema/
│       ├── 00-spec.md
│       ├── 01-clase.ipynb       # (próxima iteración)
│       ├── 02-ejercicios.ipynb  # (próxima iteración)
│       ├── 03-presentacion.pptx # (próxima iteración)
│       └── historial.md
└── recursos-marca/              # (próxima iteración) referencias visuales
```

## Próximos pasos

**Iteración 2** (siguiente turno con Claude): construir las 3 skills generadoras de artefactos.

**Iteración 3**: convertir tus 4 documentos pedagógicos existentes en skills de referencia consultables.

**Iteración 4** (opcional): hacer juntos la clase 1 completa como caso de prueba del sistema.

## Filosofía de mejora continua

Cuando uses el sistema y detectes algo que debería mejorarse:

- Si es un cambio puntual de **una clase**, dilo en chat y Claude lo aplica.
- Si es un patrón que debería aplicarse **a todas las clases futuras**, pídele a Claude que actualice el `CLAUDE.md` o el `SKILL.md` correspondiente.

Ejemplo: "Los tickets de salida me están saliendo muy largos para 10 minutos. Actualiza el SKILL.md para que apunten a 5-7 minutos como máximo".
