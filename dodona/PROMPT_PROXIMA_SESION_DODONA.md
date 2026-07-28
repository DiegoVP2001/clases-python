# Prompt para proxima sesion Dodona

Estoy en el workspace:

```text
C:\Users\diego\OneDrive\Escritorio\claude_codex\clases\claude_python\clases-python-4tomedio
```

Quiero continuar el workflow Dodona ya habilitado.

Contexto operativo confirmado:

- Repo externo Dodona local: `dodona-ejercicios-profesor/`
- GitHub: `https://github.com/DiegoVP2001/dodona-ejercicios-profesor.git`
- Dodona webhook/repo: `https://dodona.be/en/repositories/586/hook/`
- Branch del repo externo: `main`
- El push HTTPS ya funciona desde este computador con:

```powershell
git -c http.sslBackend=openssl push
```

- Piloto ya probado end-to-end:
  - Set: `piloto-ayudantia-input-booleanos-if`
  - Commit: `624595d Add piloto ayudantia input booleanos if`
  - Diego confirmo que el set se ve en Dodona.
- El repo externo quedo sincronizado despues del push: `main...origin/main`.

Reglas importantes:

- No hacer push sin autorizacion explicita de Diego.
- Las propuestas aprobadas viven en `dodona/propuestas/<set_slug>.json`.
- Los ejercicios generados viven en `dodona-ejercicios-profesor/<set_slug>/`.
- Usar TESTed por defecto.
- En tests ocultos, usar `"hidden": true` en el JSON; el generador los separa en `Casos ocultos` con `hidden: true` en `suite.yaml`.
- Validar estructura con:

```powershell
& "C:\Program Files\GIMP 3\bin\python.exe" ".claude\skills\validar-dodona-ejercicios\scripts\validar_dodona.py" "dodona-ejercicios-profesor\<set_slug>"
```

- Cuando sea posible, ejecutar las soluciones oficiales contra todos los casos del JSON para verificar `stdout`, porque TESTed no esta instalado localmente (`No module named tested`).
- Si se cambia un ejercicio, editar primero el JSON en `dodona/propuestas/` y regenerar; no editar a mano las carpetas generadas salvo para corregir el generador.

Proximo trabajo sugerido:

1. Revisar si el piloto necesita ajustes desde Dodona.
2. Si Diego quiere otro set, partir por propuesta en chat con 2-4 ejercicios.
3. Esperar aprobacion antes de generar archivos.
4. Guardar JSON aprobado.
5. Generar en `dodona-ejercicios-profesor/`.
6. Validar estructura y soluciones.
7. Commit local en el repo externo.
8. Solo si Diego autoriza, hacer push.
9. Confirmar `git status --short --branch` como `main...origin/main`.
10. Pedir a Diego revisar Dodona en `https://dodona.be/en/repositories/586/hook/`.

