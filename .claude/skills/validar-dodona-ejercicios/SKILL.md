---
name: validar-dodona-ejercicios
description: Valida ejercicios Dodona generados antes de publicarlos o subirlos al repositorio. Usa esta skill cuando Codex deba revisar estructura Dodona, config.json, dirconfig.json, suites TESTed, soluciones oficiales, o confirmar que el repo dodona-ejercicios-profesor/ esta listo para commit, push o prueba en plataforma.
---

# Skill: Validar ejercicios Dodona

## Proposito

Revisar que los ejercicios generados para Dodona tengan estructura y metadatos minimos correctos antes de publicar o subir a un repositorio remoto.

## Cuando usar

- Despues de `generar-dodona-ejercicios`.
- Antes de hacer commit/push de `dodona-ejercicios-profesor/`.
- Cuando Diego pida revisar si los ejercicios estan listos para Dodona.

## Flujo

1. Ejecuta el validador sobre la carpeta raiz Dodona o sobre un set:

```powershell
& "C:\Program Files\GIMP 3\bin\python.exe" ".claude/skills/validar-dodona-ejercicios/scripts/validar_dodona.py" "dodona-ejercicios-profesor"
```

2. Si hay errores, corrige la propuesta JSON o el generador segun corresponda y regenera.
3. Ejecuta las soluciones oficiales contra los casos del JSON cuando la propuesta este disponible, especialmente en ejercicios `io` con `stdin`/`stdout`.
4. Si solo hay advertencias, informa el riesgo y deja a Diego decidir si ajustar.
5. No hagas `git push` ni configures webhook sin instruccion explicita.
6. Si Diego autoriza push, ejecuta `git -c http.sslBackend=openssl push` desde `dodona-ejercicios-profesor/` y confirma luego `main...origin/main`.

## Que valida

- `config.json` parseable y con `evaluation.handler: tested`.
- `evaluation.test_suite` apunta a un archivo existente.
- Existe `description/description.es.md` o `description/description.en.md`.
- Existe `solution/solution.py`.
- `suite.yaml` contiene al menos un `tab` y casos de prueba.
- Los casos ocultos deben vivir en un tab con `hidden: true` cuando la propuesta JSON incluya tests con `"hidden": true`.
- `stdout` no vacio termina con salto de linea escapado.
- Los slugs de carpetas usan kebab-case ASCII.

## Estado operativo conocido

- El piloto `piloto-ayudantia-input-booleanos-if` fue validado localmente, pusheado y visto por Diego en Dodona.
- En esta maquina, el push por HTTPS funciona con `git -c http.sslBackend=openssl push` desde `dodona-ejercicios-profesor/`.

## Recursos

- `scripts/validar_dodona.py`: validador local sin dependencias externas obligatorias.
- `references/checklist.md`: lista de revision manual antes de publicar.
