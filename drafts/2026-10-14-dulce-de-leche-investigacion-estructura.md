# Remando en dulce de leche — investigación y estructura provisional

Fecha de investigación: 2026-10-14. Documento de trabajo, fuera del contenido publicado.

Dirección elegida: **retrospectiva crítica + ensayo técnico**. No es todavía el post.

Actualización editorial: la propuesta de un ensayo único queda reemplazada por [un post histórico y una serie de tutoriales narrativos por herramienta](2026-10-14-dulce-de-leche-serie-editorial.md). Este documento conserva la investigación y el primer esquema como antecedente; la estructura vigente está en el documento de la serie.

Actualización de fuentes: [la historia documentada](2026-10-14-historia-documentada.md) amplía esta investigación con el escaneo de todas las sesiones Pi disponibles y la lectura dirigida de git, tickets y whisper. Recupera el nacimiento de whisper como skill en julio, un tracer dont→ah→WAI implementado en junio y el repo evallerina en septiembre. Para cronología y evaluación histórica, usar ese dossier antes de reutilizar las conclusiones del informe antiguo.

## Pregunta y tesis provisional

¿Qué cambia cuando construir herramientas para agentes resulta barato, pero demostrar que ayudan sigue siendo difícil?

El ecosistema externaliza distintas responsabilidades del agente: recordar decisiones, fundamentar afirmaciones, expresar requisitos, relacionarlos con tests, seleccionar verificaciones y comprobar composición. Algunas conexiones ya existen en código. La pregunta crítica es cuánto de esa estructura produce evidencia útil y cuánto agrega trabajo de mantenimiento, contexto y rituales.

Hipótesis editorial, no resultado medido: hacer explícita una responsabilidad ayuda cuando también hacemos explícito cómo refutar su cumplimiento. Instalar una herramienta, aprobar una especificación y obtener un resultado útil son acontecimientos distintos.

## Alcance y procedencia

Se consultaron los checkouts locales de ddl y sus herramientas, sus READMEs y páginas de estado, y puntos concretos de implementación. No se ejecutó una evaluación comparativa, ni se repitió el censo de uso, ni se verificaron instalaciones en tres plataformas. Los números de rendimiento y adopción siguen atribuidos a sus fuentes originales.

- Microdancing: rama actual `data/datos-uso-ia`, HEAD inicial `09c063e`.
- Rama `data/conference-analysis`: HEAD `52e59b1`; leída con `git show`, sin cambiar el checkout.
- Ddl: HEAD `7c49a37`; hay modificaciones locales previas, por lo que el SHA no identifica todo lo observado en el working tree.
- La evaluación `conference-analysis/analysis/data/ddl-family-evaluation.md` está en el directorio **no trackeado** del checkout actual; no aparece en el árbol de la rama de conferencias. Es material recuperado, no un documento que podamos atribuir a un commit de esa rama.
- Se consultaron también los repositorios públicos de [ddl](https://github.com/charly-vibes/dulce-de-leche), [specodelic](https://github.com/charly-vibes/specodelic) y [funkalization](https://github.com/charly-vibes/funkalization). Las páginas públicas y los checkouts locales pueden diferir; esta investigación describe principalmente el estado local.

## Inventario: los 12 tools del registro actual

El registro ejecutable en `../../dulce-de-leche/src/platform.rs` es la referencia de pertenencia. La [matriz generada](../../dulce-de-leche/docs/capability-matrix.md) y el README coinciden en 12 herramientas. El documento `docs/src/ecosystem.md` conserva categorías y recuentos anteriores.

| Tool / binario | Responsabilidad | Estado observado / límite para el post | Fuente local |
|---|---|---|---|
| wai / `wai` | Preservar investigación, decisiones, fases y handoffs; recuperar el porqué | Comandos implementados; README dice beta, catálogo ddl dice stable. Los tiempos de recuperación son una meta, no una medición demostrada aquí | [README](../../wai/README.md), [estado](../../wai/docs/src/status.md) |
| testaruda / `testaruda` | Seleccionar tests a partir de dependencias y cambios, explicar selección | Motor y cinco adaptadores documentados; proyecto beta, catálogo stable. Selección conservadora no equivale a garantizar que los tests sean buenos | [README](../../testaruda/README.md), [estado](../../testaruda/docs/src/status.md) |
| dont / `dont`, `dt` | Hacer explícitos claims, evidencia, dudas y vocabulario | Máquina de estados y gate implementados; registrar evidencia no garantiza su verdad | [README](../../dont/README.md), [estado](../../dont/docs/src/status.md) |
| espectacular / `ah` | Relacionar escenarios de specs con contratos y tests; producir señales de calidad | Correspondencia y ejecución implementadas; un test asociado y verde no demuestra por sí solo que falsifique bien el requisito | [estado](../../espectacular/docs/src/status.md), [check.rs](../../espectacular/src/check.rs) |
| pretender / `pretender` | Inspección estructural: complejidad, duplicación y superficie de mutación | Reportes y gates implementados; métricas estructurales no son una medida completa de calidad | [README](../../pretender/README.md), [estado](../../pretender/docs/src/status.md) |
| vampiro / `vampiro` | Analizar compatibilidad y obligaciones en límites de composición | Análisis de seams implementado. `prove` imprime que la verificación de leyes no está implementada, pese a la tabla de estado | [README](../../vampiro/README.md), [dispatch CLI](../../vampiro/crates/vampiro-cli/src/cli/mod.rs) |
| whisper / `turu`, `turututu`, `whisper` | Routing determinista de conocimiento por repo, branch, worktree y otros scopes | key/resolve/append/recall/distill/bundle implementados. La reescritura semántica de distill la hace el agente; el CLI guarda revisión y concurrencia | [README](../../whisper/README.md), [estado](../../whisper/docs/src/status.md) |
| specodelic / `specodelic`, `spk` | Specs Markdown: Intent, Constraints, Model y Properties; lint, compile y verify | Experimental, comandos documentados como implementados. Verificación acotada de claims explícitos y properties compiladas; no prueba de corrección de la aplicación | [README](../../specodelic/README.md), [relaciones](../../specodelic/docs/src/tool-relationships.md) |
| funkalization / `funkalization` | Workspace semántico de diseño: revisiones, autoridad, obligaciones y evidencia | Experimental. README dice scaffold; estado local ya describe tracer persistente G0–G4 y proyecciones. UI e integración completas siguen abiertas; README dice no publicado | [README](../../funkalization/README.md), [estado](../../funkalization/docs/src/status.md) |
| incitaciones / paquete npm | Distribuir skills y prompts reutilizables, compilación y validación del corpus | Experimental con pipelines de contenido implementados. Validar estructura/frescura de un skill no demuestra su eficacia conductual | [README](../../incitaciones/README.md), [estado](../../incitaciones/docs/src/status.md) |
| beads / `bd` | Issues y dependencias | Externo, install-only. En este workspace JSONL + git es la fuente de verdad indicada por el usuario; no generalizar la antigua arquitectura Dolt del informe | [registro ddl](../../dulce-de-leche/src/platform.rs), instrucciones del workspace |
| OpenSpec / `openspec` | Propuestas, deltas, tareas y archivo de cambios | Externo, install-only. Es workflow de cambios; specodelic añade estructura verificable al contenido y ah comprueba correspondencia | [relaciones](../../specodelic/docs/src/tool-relationships.md), [registro ddl](../../dulce-de-leche/src/platform.rs) |

Ddl mismo es el orquestador: instalación, configuración, migración, diagnóstico y actualización. El estado local describe un producto shipped; no confundir que el registro conozca una herramienta con que esa herramienta ya tenga un release instalable.

## Ecosistema ampliado

El [mapa](../../dulce-de-leche/docs/ecosystem-map.md) incluye herramientas que no están en el registro de instalación. Esa diferencia importa para contar la historia sin inflar el bundle.

| Componente | Papel y estado observado | Fuente |
|---|---|---|
| genesis / `genesis-vibes` | Biblioteca compartida de envelopes, config, doctor, bloques gestionados, plumbing git y hooks. Infraestructura, no un tool de usuario instalado por ddl | [README](../../genesis/README.md) |
| wild / `wild`, crate `wild-vibes` | Compatibilidad de componentes como contratos; extract/check implementados. Experimentos pequeños y simulaciones, con límites reconocidos | [README](../../wild/README.md) |
| bajan / `bajan` | Pipeline de knowledge graph: ingestión, extracción de claims y consulta, SQLite y procedencia. Release temprano, ruta LLM todavía joven | [README](../../bajan/README.md) |
| gently / `gently` | Port de Graph::Easy: layout determinista y diagramas textuales. Wave inicial implementada con oracle diferencial; el mapa ddl todavía dice no publicado | [README](../../gently/README.md) |
| fotos / `fotos-mcp` y app | Capturas, anotación y visión para feedback con agentes; proyecto Tauri con MCP. Integraba el alcance antiguo del informe, no el registro actual | [README](../../fotos/README.md) |
| fabbro / `fabbro` | TUI de anotaciones de review, FEM y extracción JSON para feedback humano→agente. También pertenece al alcance histórico, no al registro actual | [README](../../fabbro/README.md) |
| livin | Propuesta para revisar cobertura de valores de frontera; sin implementación de aplicación según README | [README](../../livin/README.md) |
| crua | Propuesta para verificar costos de hardware/runtime; sin implementación de aplicación según README | [README](../../crua/README.md) |
| homebrew-charly / scoop-charly | Canales de distribución manual; desde el cambio descrito como DDL-ei3, ddl decide instalación por binarios/cargo/npm, no por brew/scoop | [estado ddl](../../dulce-de-leche/docs/src/status.md) |

## Conexiones que ya existen

Estas conexiones describen código/documentación observados, no un pipeline único validado de punta a punta.

1. **ah → testaruda**: `espectacular/src/check.rs:107` invoca `testaruda select --agent --files`; si no hay store, binario o JSON válido, conserva la selección sin podar. La lógica posterior utiliza la selección para refinar contratos.
2. **ah → specodelic**: `espectacular/src/cmd_misc.rs:233` pasa `spk` a `sync::run_sync` para derivar contratos de Properties lint-clean. Es un puente concreto entre contenido de spec y verificación de comportamiento.
3. **OpenSpec ↔ specodelic**: doble formato, lint de drift y `spk archive-companion`; el archivo stock de OpenSpec puede destruir la capa specodelic. El companion preserva deltas y falla si falta la capa requerida.
4. **ah ← dont**: `ah signals` recoge señales de rechazo/drift; `dont check` está documentado como gate de CI de vampiro. Separar señales observadas de garantía epistemológica.
5. **wai → plugins**: `wai/src/plugin.rs` define detección, passthrough y comandos de contexto para tools como dont, testaruda y pretender. No asumir que todos los comandos configurados sean vigentes o que toda integración haya sido evaluada.
6. **incitaciones → turu**: el skill whisper apunta al pack mantenido por turu. La habilidad guía el trabajo semántico; el binario resuelve rutas, idempotencia y revisiones deterministas.
7. **tools → genesis / ddl → tools**: compartir biblioteca de infraestructura es distinto de consumir estado de workflow. Ddl usa protocolo de subprocess para mantener identidades y ciclos de release separados.

## Material previo recuperado

En `data/datos-uso-ia`:

- [Resoluciones de septiembre](post-principal-resoluciones.md): crónica cronológica, primera persona, escena → dato → pregunta; herramientas nacidas de fricciones; post grande con guías separadas. No repetir la filosofía de los posts publicados.
- [Boceto de junio](serie-aprendizaje-6-meses-boceto.md): abundancia, infraestructura, límites visuales, autonomía y soledad del juicio. Sus números y el supuesto cierre definitivo tras la pausa quedaron revisados en septiembre.
- `data/` y visualización Gantt: candidatos para contexto histórico, con corte temporal y definiciones explícitas. No equivalen a métricas de eficacia por herramienta.

En `data/conference-analysis` (leer con `git show data/conference-analysis:<path>`):

- `conference-analysis/analysis/data/diff_report.md`: diferencia entre discursos de transformación y construcción; método y límites del corpus.
- `conference-analysis/analysis/data/leverage_list.md`: lectura orientada al operador solo, context churn y falta de evals.
- `conference-analysis/memory-systems-report.md`: memoria/persistencia y gobierno del conocimiento.
- `conference-analysis/workshop/skill_management_practices.md`: build/share/govern, routing, disclosure progresivo y evals de skills.
- `conference-analysis/aix-for-genesis-report.md`: receipts, budgets de contexto, evals y feedback→scenario.

En el directorio no trackeado de la rama actual:

- [Evaluación ddl](../conference-analysis/analysis/data/ddl-family-evaluation.md): hipótesis críticas útiles, pero snapshot antiguo. Conserva referencias a fotos/fabbro y un censo basado en PATH, state dirs y timestamps; no es una medición longitudinal de valor.

## Qué debe actualizarse antes de convertir el análisis antiguo en afirmaciones del post

| Afirmación anterior | Evidencia local actual | Uso editorial |
|---|---|---|
| Ddl no verifica checksums | `dulce-de-leche/src/installer.rs:502` exige checksum por defecto; mismatch nunca se saltea; ausencia requiere autorización explícita para legacy-unverified | Contar evolución. No reciclar el hallazgo como vulnerabilidad vigente |
| Ningún tool consume estado de otro | ah invoca testaruda; sync usa spk; protocolo dual-format y señales dont existen | Mostrar conexiones concretas y evaluar sus bordes. No proclamar integración completa |
| Solo dos tools tienen uso diario | Censo histórico por state dirs y últimas escrituras, no repetido aquí | Presentarlo como observación situada y con proxy imperfecto; configs ausentes no prueban ausencia de uso |
| Cero métricas/evals propios | Hay metas explícitas, gates, pruebas y dogfood documentados; no se auditó un corpus de evals de toda la familia | Distinguir meta, test técnico, dogfood y outcome medido. No sustituir un absoluto por otro |
| La familia tiene diez herramientas | Registro actual de doce, con miembros distintos y vecinos fuera del bundle | Fijar fecha y alcance |
| Todos los comandos marcados stable están completos | Vampiro `prove` contradice status; funkalization status avanzó respecto del README; wai/testaruda difieren del catálogo | La documentación también es evidencia que puede fallar |

## Estructura propuesta del ensayo

Título de trabajo: **Remando en dulce de leche**.

Subtítulo posible: **Lo que mis herramientas para agentes pueden comprobar — y lo que todavía tengo que demostrar.**

Audiencia asumida: personas que ya usan agentes de programación y necesitan entender el costo y las garantías de formalizar el entorno. El texto debe funcionar sin conocer estos nombres previamente.

### 1. Una respuesta para cada fricción

Abrir con un episodio real, todavía por elegir: retomar un proyecto y reconstruir su porqué; o un gate que marca éxito sin ofrecer la evidencia esperada. No inventar diálogo ni experiencia.

Presentar la pregunta: ¿cuándo una herramienta reduce incertidumbre y cuándo solo la vuelve administrable? Recuperar la historia como contexto breve, sin rehacer el post autobiográfico completo.

### 2. El mapa de responsabilidades

Agrupar por preguntas, no dar doce mini-READMEs:

- ¿Qué sabemos y por qué? wai, turu, dont, bd.
- ¿Qué prometimos construir? OpenSpec, specodelic, funkalization.
- ¿Cómo intentamos refutarlo? ah, pretender, testaruda, vampiro; wild como vecino.
- ¿Cómo sostenemos el entorno? incitaciones, genesis, ddl y canales de distribución.

Introducir cada nombre cuando responde una pregunta concreta. El inventario completo puede ser un cuadro lateral o un anexo.

### 3. Seguir una obligación de punta a punta

Elegir un caso pequeño, con un requisito y un fallo deliberado. Recorrer OpenSpec → specodelic → ah y, cuando aplica, testaruda. Mostrar el artefacto que cruza cada borde y su criterio de aceptación.

El recorrido está respaldado por conexiones de implementación, pero **el ejemplo reproducible todavía debe ejecutarse**. Separar gates paralelos (pretender/vampiro/dont) de una cadena secuencial que no existe para todos los tools.

### 4. El verde tiene distintos significados

Centro técnico y crítico del ensayo:

- lint-clean: estructura admisible;
- correspondence: un escenario y un contrato se relacionan;
- test passed: una ejecución tuvo éxito;
- bounded verification: ciertas propiedades del modelo no encontraron contraejemplo dentro del alcance;
- user outcome: alguien resolvió su problema con menor costo o mejores resultados.

La cadena no permite inferir automáticamente el último nivel. Usar el caso `vampiro prove` como ejemplo concreto de por qué exit code, estado documentado y capacidad real deben leerse juntos.

### 5. Volver sobre la crítica anterior

Comparar el informe antiguo con el estado actual: checksum incorporado, puentes de integración existentes, miembros nuevos y documentación que todavía deriva. Mostrar qué objeción recibió respuesta y cuál sigue sin medición.

Mantener la pregunta de fondo: ¿el conjunto devuelve más atención de la que consume? No deducir ansiedad, utilidad o ausencia de adopción únicamente del número de repos o de tests.

### 6. Qué evidencia aceptaría como mejora

Proponer criterios de evaluación, identificados como futuros, no resultados:

- recuperación: tiempo y precisión al reconstruir una decisión, con y sin wai/turu;
- selección: tests omitidos y fallos perdidos frente a la suite completa;
- correspondencia: defectos deliberados detectados y falsos positivos;
- contexto: bytes/tokens inyectados y utilidad al retomar;
- mantenimiento: tiempo de upgrades, resolución de drift y reparaciones de CI;
- skills: tareas representativas con grader independiente de la implementación.

Cerrar con una consecuencia concreta para la práctica: toda nueva herramienta debe declarar qué sabe comprobar, qué deja sin comprobar y cuál sería una observación capaz de desmentir su promesa.

## Decisiones editoriales todavía abiertas

El hook requiere un episodio confirmado por el autor. La pieza puede apuntar a 2.000–3.000 palabras y reservar el tour de instalación y la guía reproducible para posts separados. El idioma del primer borrador puede seguir el español de las resoluciones previas; no se preparó todavía una traducción.

Evitar convertir cifras de charlas en resultados del ecosistema, citar metas SMART como resultados alcanzados o sugerir que una verificación del modelo prueba la aplicación. El perfil privado de estilo no debe copiarse al post ni publicarse.
