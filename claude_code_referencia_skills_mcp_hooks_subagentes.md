# Referencia: Skills, MCP, Hooks y Subagentes en Claude Code

> Documento de referencia para auditar el uso correcto de los componentes de extensión de Claude Code en un proyecto. Cada sección incluye definición, criterios de decisión (cuándo usar / cuándo no), buenas prácticas y señales de mal uso revisables.

## 1. Modelo mental

Cada capa de extensión resuelve un problema distinto. No son intercambiables.

| Componente | Problema que resuelve | Naturaleza |
|---|---|---|
| CLAUDE.md | Contexto siempre presente (reglas "siempre haz X") | Determinista en carga, interpretado en aplicación |
| Skill | Conocimiento on-demand y workflows invocables | Interpretado (Claude decide cómo aplicar) |
| MCP | Conexión a servicios y datos externos | Herramientas + datos |
| Subagente | Aislamiento de contexto y especialización | Worker con loop propio |
| Hook | Automatización garantizada en eventos | Determinista (siempre dispara) |

Regla base de decisión:
- Si debe ser cierto en cada turno → CLAUDE.md.
- Si es un procedimiento o conocimiento que solo se necesita a veces → Skill.
- Si requiere datos o acciones de un sistema externo → MCP.
- Si genera mucho output intermedio que no se reutiliza, o necesita modelo/permisos distintos → Subagente.
- Si debe ocurrir siempre, igual, sin que el modelo "decida" → Hook.

Distinción crítica de garantía: una instrucción en un prompt o skill ("nunca edites `.env`") es una petición, no una garantía. Si una regla debe cumplirse siempre, va en un Hook (enforcement), no en un prompt.

---

## 2. Skills

### Definición
Archivo `SKILL.md` con frontmatter YAML (`name`, `description`) más instrucciones en markdown. Pueden ser de dos tipos:
- **Reference**: aportan conocimiento que Claude usa a lo largo de la sesión (ej. una guía de estilo de API).
- **Action**: ejecutan un workflow invocable con `/<nombre>` (ej. `/deploy`).

### Carga y costo de contexto
- En el arranque solo se cargan `name` + `description` de cada skill (≈100 tokens por skill).
- El cuerpo completo se carga solo cuando la skill se invoca o Claude la considera relevante.
- Progressive disclosure en tres niveles: frontmatter → cuerpo de `SKILL.md` → archivos vinculados (estos últimos no consumen contexto hasta que se leen). Los scripts pueden ejecutarse sin cargar su contenido; solo su salida consume tokens.

### Cuándo usar
- Material de referencia que se necesita a veces (esquemas, guías de estilo, documentación de API).
- Procedimientos repetibles (checklist de deploy, playbook de debugging).
- Cuando repites el mismo prompt largo o el mismo playbook por tercera vez.

### Cuándo NO usar
- Reglas "siempre haz X" → CLAUDE.md.
- Conexión a un servicio externo → MCP (la skill puede documentar cómo usarlo, pero no provee la conexión).
- Algo que debe cumplirse siempre y de forma garantizada → Hook.

### Buenas prácticas
- La `description` es el mecanismo principal de activación. Debe declarar **qué hace** y **cuándo usarse**. Máximo 1024 caracteres, sin etiquetas XML.
- `name`: solo minúsculas, números y guiones. Recomendado usar forma de gerundio en inglés (verbo + -ing) para describir la capacidad.
- Mantener `SKILL.md` focalizado; mover material extenso a archivos referenciados (sin penalización de contexto hasta usarse).
- Usar `disable-model-invocation: true` en skills con efectos secundarios: solo se invocan manualmente y su costo de contexto es cero hasta invocarlas.
- Usar `allowed-tools` para restringir herramientas cuando aplique.
- Probar la skill con todos los modelos con que se usará. Haiku suele necesitar más guía; Opus, menos detalle.
- Validar la activación con ~20 consultas de prueba (mezcla de *should-trigger* y *should-not-trigger*).
- Usar solo skills de fuentes confiables: una skill maliciosa puede dirigir a Claude a ejecutar código o exfiltrar datos fuera de su propósito declarado.

### Señales de mal uso (revisables)
- `description` vaga, genérica o que se solapa con otra skill → Claude carga la equivocada o ninguna.
- Cuerpo de `SKILL.md` excesivamente largo con material que debería estar en archivos de referencia.
- Skill con efectos secundarios sin `disable-model-invocation`.
- Contenido que en realidad es una regla siempre-on (debería estar en CLAUDE.md) o un guardrail (debería ser Hook).

---

## 3. MCP (Model Context Protocol)

### Definición
Protocolo que conecta Claude a servicios y herramientas externas. Un servidor MCP expone capacidades (tools, resources, prompts) que Claude descubre al inicio y llama cuando las necesita.

### Carga y costo de contexto
- En el arranque se cargan los nombres de las herramientas; los esquemas JSON completos quedan diferidos hasta que se usa una herramienta concreta.
- La búsqueda de herramientas (tool search) está activa por defecto, por lo que las herramientas inactivas consumen contexto mínimo.

### Cuándo usar
- Se necesitan datos o acciones externas: consultar una base de datos, postear en Slack, controlar un navegador, llamar a una API interna.
- Indicador típico: copias repetidamente datos desde una pestaña o sistema que Claude no puede ver.

### Cuándo NO usar
- Solo se necesita conocimiento estático → Skill.
- Los datos ya están disponibles localmente en el repositorio.

### Buenas prácticas
- Conectar solo los servidores que se usan; desconectar los inactivos.
- Usar `/mcp` para ver estado de conexión y costo de tokens por servidor.
- Combinar con una skill que documente cómo usar bien el MCP (esquema de datos, patrones de consulta, qué tablas usar). El MCP da la conexión; la skill da el conocimiento de uso.

### Precedencia (scope)
Cuando el mismo servidor existe en varios niveles, gana por nombre: **local > project > user**.

### Señales de mal uso (revisables)
- Servidores conectados que nunca se invocan (costo y ruido innecesarios).
- Uso de MCP para conocimiento estático que debería ser una skill.
- Ausencia de una skill que documente el modelo de datos o patrones de consulta del servidor.

---

## 4. Subagentes

### Definición
Worker con contexto aislado y su propio system prompt. Ejecuta su propio loop y devuelve solo un resumen al agente principal. El trabajo intermedio (lecturas, búsquedas, output verboso) permanece aislado y no contamina la conversación principal.

### Carga y costo de contexto
- Contexto fresco y aislado: no hereda el historial de la conversación ni las skills ya invocadas.
- Carga su propio system prompt, el contenido completo de las skills listadas en su campo `skills:`, CLAUDE.md y git status (los agentes integrados Explore y Plan omiten estos dos), y el contexto que le pase el agente líder.

### Cuándo usar
- Aislamiento de contexto: una tarea lee decenas de archivos pero solo importa el resultado.
- Trabajo en paralelo entre tareas independientes.
- La tarea requiere comportamiento distinto: otro modelo (costo o capacidad), acceso restringido de herramientas (seguridad), o un system prompt especializado.

### Cuándo NO usar
- Workflows que requieren pasos observables e incrementales → asignarlos al agente principal.
- Cuando los workers necesitan comunicarse entre sí, compartir hallazgos o desafiarse → agent teams (capa siguiente).

### Configuración relevante
`name`, `description` (define cuándo delegar), `tools` (restringe el acceso), `model` (`haiku` / `sonnet` / `opus` / `inherit`), `skills` (precargadas), `maxTurns`, `memory`.

### Buenas prácticas
- Una sola área de expertise por subagente.
- Acceso mínimo de herramientas.
- Haiku para tareas simples; Sonnet u Opus para análisis complejo.
- Correr trabajo independiente en paralelo.
- Incluir una Definition of Done corta en el prompt del subagente.

### Precedencia (scope)
Gana por nombre: **managed > CLI flag > project > user > plugin**.

### Señales de mal uso (revisables)
- Subagente con múltiples áreas de expertise mezcladas.
- Acceso de herramientas más amplio de lo necesario.
- Modelo sobredimensionado para la tarea (Opus para algo trivial) o insuficiente.
- `description` que no deja claro cuándo el agente principal debe delegar.
- Uso de subagente para pasos que el usuario necesita ver en vivo.

---

## 5. Hooks

### Definición
Mecanismo que dispara en eventos del ciclo de vida de Claude Code y ejecuta una acción: comando shell, petición HTTP, prompt LLM o subagente. A diferencia de skills, su disparo está garantizado en el evento; no depende de que el modelo "decida".

### Carga y costo de contexto
- Cero por defecto: el hook corre fuera de la conversación.
- Solo consume contexto si devuelve output, que se añade como mensaje que Claude lee.

### Eventos del ciclo de vida (12 en total)
Los más usados: `PreToolUse` (checkpoint de seguridad, puede aprobar o bloquear antes de ejecutar una herramienta), `PostToolUse` (verificaciones y formateo tras ejecutar), `UserPromptSubmit` (puede bloquear o modificar el prompt antes de que Claude lo vea), `SessionStart`, `Stop` / `SubagentStop`, `PreCompact`, `PermissionRequest`.

### Tipos de handler
- **Command**: script shell. Ideal para tareas deterministas (formatear, linting, logging).
- **Prompt**: evaluación LLM de un turno para decisiones sí/no demasiado complejas para expresar en shell.
- **Agent**: lanza un subagente con acceso a herramientas (Read, Grep, Glob) para verificación profunda que requiere entender varios archivos (más completo pero más lento).

### Exit codes (handler Command)
- `0`: éxito.
- `2`: bloquea la acción y devuelve el mensaje de error a Claude.
- Cualquier otro: advertencia no bloqueante.
- Alternativa: `PreToolUse` puede negar mediante una decisión JSON con `permissionDecision: "deny"`.

### Cuándo usar
- La acción debe ocurrir igual, siempre, y no necesita que Claude razone (formatear al guardar, rechazar `rm -rf`, notificar al terminar una sesión).
- Guardrails y enforcement de políticas.

### Cuándo NO usar
- Cuando Claude debe decidir cómo aplicar los pasos, o cuando el contenido es conocimiento y no un script → Skill.

### Buenas prácticas
- Los guardrails van en hooks, no en prompts. Un `PreToolUse` que bloquea es enforcement real; una instrucción en CLAUDE.md o skill es solo una petición.
- Command para lo determinista; Prompt o Agent solo cuando se requiere razonamiento que no se expresa en shell.
- Side-effects que no deben frenar la ejecución (logging, backups, notificaciones): marcar como asíncronos.
- En Windows, escribir el script de validación en PowerShell y declarar `shell: powershell` en la entrada del hook.

### Precedencia (scope)
Los hooks se combinan: **todos** los hooks registrados disparan en su evento coincidente, sin importar el origen.

### Señales de mal uso (revisables)
- Guardrails de seguridad escritos solo como instrucciones en prompts en lugar de en hooks.
- Handler tipo Prompt o Agent para una tarea que un Command determinista resolvería (lento e innecesario).
- Exit codes incorrectos: usar algo distinto de `2` cuando se pretende bloquear.
- Side-effects pesados sin marcar como asíncronos, frenando la sesión.

---

## 6. Tabla de decisión rápida

| Necesidad | Componente |
|---|---|
| Regla que debe valer en cada turno | CLAUDE.md |
| Conocimiento o procedimiento que se usa a veces | Skill |
| Workflow invocable bajo demanda (`/<nombre>`) | Skill (action) |
| Conectar a base de datos, API, Slack, navegador | MCP |
| Tarea que lee muchos archivos y solo importa el resultado | Subagente |
| Trabajo en paralelo o con modelo/permisos distintos | Subagente |
| Algo que debe ocurrir siempre, de forma garantizada | Hook |
| Bloquear comandos peligrosos o ediciones prohibidas | Hook (`PreToolUse`, exit 2) |
| Formatear/lint tras cada edición | Hook (`PostToolUse`) |

---

## 7. Precedencia y costo de contexto (resumen)

| Componente | Cuándo carga | Costo de contexto | Precedencia entre niveles |
|---|---|---|---|
| CLAUDE.md | Inicio de sesión | Cada request (contenido completo) | Aditivo (todos los niveles suman) |
| Skills | Descripciones al inicio; cuerpo al usar | Bajo (cero si `disable-model-invocation`) | Override por nombre: managed > user > project |
| MCP | Nombres al inicio; esquemas on-demand | Bajo hasta usar una herramienta | Override por nombre: local > project > user |
| Subagentes | Al ser lanzados | Aislado del main | Override por nombre: managed > CLI flag > project > user > plugin |
| Hooks | Al dispararse el evento | Cero salvo que devuelvan output | Merge (todos disparan) |

---

## 8. Patrones de combinación

| Patrón | Cómo funciona | Ejemplo |
|---|---|---|
| Skill + MCP | MCP provee la conexión; la skill enseña a usarla bien | MCP conecta a la base de datos; la skill documenta el esquema y los patrones de consulta |
| Skill + Subagente | Una skill lanza subagentes para trabajo paralelo | `/audit` dispara subagentes de seguridad, rendimiento y estilo en contexto aislado |
| CLAUDE.md + Skill | CLAUDE.md tiene la regla siempre-on; la skill el material de referencia bajo demanda | CLAUDE.md dice "sigue nuestras convenciones de API"; la skill contiene la guía completa |
| Hook + MCP | Un hook dispara acciones externas vía MCP | Hook post-edición notifica a Slack cuando Claude modifica archivos críticos |

> Nota: los **plugins** son la capa de empaquetado. Agrupan skills, hooks, subagentes y servidores MCP en una unidad instalable y reutilizable entre repositorios. Las skills de plugin quedan con namespace (ej. `/mi-plugin:review`) para evitar conflictos.

---

## 9. Checklist de auditoría

Para revisar la claridad y el uso correcto de estos elementos en un proyecto:

**Skills**
- [ ] Cada `description` declara qué hace y cuándo usarse, es específica y no se solapa con otras.
- [ ] El cuerpo de `SKILL.md` está focalizado; el material extenso está en archivos referenciados.
- [ ] Las skills con efectos secundarios tienen `disable-model-invocation: true`.
- [ ] No hay skills que deberían ser CLAUDE.md (regla siempre-on) o Hook (enforcement).
- [ ] Las skills provienen de fuentes confiables.

**MCP**
- [ ] No hay servidores conectados que no se usen.
- [ ] Cada MCP no trivial tiene una skill que documenta su uso (esquema, patrones).
- [ ] No se usa MCP para conocimiento estático que debería ser skill.

**Subagentes**
- [ ] Cada subagente cubre una sola área de expertise.
- [ ] El acceso de herramientas (`tools`) es el mínimo necesario.
- [ ] El `model` es proporcional a la complejidad de la tarea.
- [ ] La `description` deja claro cuándo delegar.
- [ ] No se delegan a subagentes pasos que deben ser observables en vivo.

**Hooks**
- [ ] Los guardrails de seguridad están implementados como hooks, no solo como instrucciones en prompts.
- [ ] Los handlers Command se usan para lo determinista; Prompt/Agent solo cuando se requiere razonamiento.
- [ ] Los exit codes son correctos (`2` para bloquear).
- [ ] Los side-effects que no deben frenar la sesión están marcados como asíncronos.

Documentación oficial vigente a junio de 2026.
