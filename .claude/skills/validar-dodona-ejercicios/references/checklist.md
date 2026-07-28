# Checklist manual antes de publicar en Dodona

- El set vive bajo `dodona-ejercicios-profesor/<set_slug>/`.
- Cada ejercicio tiene `config.json`, `description/`, `evaluation/` y `solution/`.
- `config.json` usa `evaluation.handler: tested`.
- `evaluation.test_suite` coincide con el archivo YAML real.
- La descripcion visible no incluye la solucion.
- La solucion oficial pasa conceptualmente todos los casos.
- Hay al menos un caso visible y uno oculto cuando el ejercicio lo justifica.
- Los ejercicios no usan contenidos no vistos en las clases foco.
- Los outputs esperados son razonables para estudiantes y no dependen de prompts largos.
- No se hace `git push` sin instruccion explicita de Diego.
