# Remando en dulce de leche — historia documentada

Investigación: 2026-10-14. Material de trabajo para el post histórico y los tutoriales. Este dossier reconstruye acontecimientos; todavía no es el artículo.

## Qué podemos contar ahora

La historia no empieza con un bundle de doce herramientas. Empieza con proyectos, formas de devolver feedback y prácticas que se intentan conservar. En mayo aparece un pedido explícito de evaluar las herramientas **como sistema**. En julio se trabaja sobre su consistencia y surge genesis; tres días después, ddl. Whisper comienza como una skill y solo después se convierte en un CLI. En septiembre llegan nuevos formatos de especificación y un repo de evaluación. En octubre, los propios registros de uso alimentan cambios de integración y setup.

Ese recorrido está respaldado por solicitudes del autor, commits, tickets y notas de sesión. La relación entre estos materiales permite contar decisiones y consecuencias sin asumir que cada herramienta nació de la anterior, que cada ticket cerrado prueba eficacia o que toda la actividad registrada fue uso productivo.

## Cobertura y límites de la reconstrucción

Se enumeraron las sesiones con `terapia list`. Se parsearon todos los JSONL disponibles, incluyendo mensajes de usuario, respuestas, thinking, argumentos de herramientas, resultados y compactions textuales. Los cuerpos binarios de imágenes/audio no se interpretaron. Después se hizo una lectura dirigida de conversaciones y artefactos relevantes para el ecosistema. **Escaneo integral e indexación no significan lectura editorial línea por línea de cada conversación ajena al tema.**

| Fuente | Cobertura observada |
|---|---|
| Pi / terapia | 1.916 archivos y 1.916 ids de sesión; 426.216 líneas JSONL parseadas; cero líneas malformadas |
| Texto Pi indexado | 418.365 registros con texto; 12.066 mensajes textuales de usuario |
| Git | 55 checkouts descubiertos, 47 directorios git comunes; todas las refs locales; 6.670 filas de commits y 4.662 SHAs únicos |
| Beads | 6.337 filas de tickets, 4.466 ids distintos, incluyendo cerrados; los worktrees repiten snapshots |
| Comentarios Beads | 215 comentarios de los 88 ids que reportaban comentarios al consultar los trackers |
| Whisper | 191 archivos Markdown globales y locales; el directorio global resuelve al archivo del journal |
| WAI | 3.588 archivos Markdown de investigación, decisiones, planes y handoffs en los checkouts consultados |

El [registro de cobertura](history/2026-10-14-coverage.json) conserva los recuentos y sus definiciones. El [inventario de repositorios](history/2026-10-14-repository-inventory.tsv) permite revisar qué checkout aportó cada historia. Los [localizadores Pi](history/2026-10-14-pi-source-locators.md) identifican sesión, archivo, línea, mensaje y timestamp de los episodios citados abajo.

El índice integral está en `/tmp/charly-history/sources.sqlite`. No se copian transcripts privados ni exportaciones completas de tickets al repositorio. Las referencias de este dossier son paráfrasis y localizadores seleccionados.

No se consultaron remotos faltantes ni sesiones borradas. Los archivos estaban activos durante la lectura: esto es un snapshot observado por archivo, no un archivo congelado atómicamente. Los worktrees y el checkout anidado de un servidor MCP de terceros se cuentan como fuentes, **no como nuevos proyectos del autor**.

### Cómo leer las fechas

- La fecha del primer commit alcanzable muestra que un artefacto ya estaba registrado; no determina cuándo nació la idea ni cuándo se creó el repo en GitHub.
- Los commits conservan fechas de autor y committer en el índice. La tabla de hitos usa fechas de autor, salvo aclaración.
- Pi y Beads usan UTC. Para el relato se usa Buenos Aires (UTC−03:00). La conversación de whisper del 28 de julio UTC ocurrió todavía el 27 de julio local.
- Una nota whisper es una reconstrucción de sesión, a menudo escrita por un agente. Se contrasta con commits y tickets cuando hay discrepancias.
- La actividad dentro del repo de una herramienta puede ser **desarrollo de esa herramienta**. No se cuenta automáticamente como adopción en otros proyectos.

## I. Antes de la familia — enero a marzo

Los primeros commits alcanzables sitúan jams el **6 de enero**, fabbro el **9**, incitaciones y nayra el **12**, microdancing el **19**, WAI el **31**. Son fechas de registro local: los borradores anteriores a veces daban fechas de creación de repos un día después. No hay que reemplazar una por otra sin nombrar la diferencia.

Jams permite explorar aplicaciones pequeñas. Fabbro propone un feedback de review explícito, mediante anotaciones. Incitaciones conserva prácticas reutilizables; nayra aborda visualización de timelines. Microdancing convierte la experiencia en materia de escritura. WAI registra el porqué de las decisiones.

En febrero aparecen rizomas y fotos, la propuesta de bichos y los canales Homebrew/Scoop. Khipu entra en el registro a principios de marzo. Estas búsquedas conviven: interfaces, feedback visual, organización de agentes, distribución y lectura de traces.

**Evidencia git:** jams `1ef64cafe`; fabbro `b7311ab7b`; incitaciones `57462a03e`; nayra `3c598ae56`; microdancing `164107c60`; WAI `5681e32c1`; fotos `8fae5050e`; bichos `bbb6e3f28`; khipu `6ca1d51e4`.

**Límite:** el archivo Pi disponible empieza el **14 de abril**, no en enero. Los motivos originales de estas primeras herramientas deben reconstruirse desde specs, historial y explicaciones del autor; no existe acá una conversación Pi de su nacimiento. En particular, la propuesta de bichos puede anteceder a su primer commit conservado.

## II. Una herramienta sola ya no alcanza — abril y mayo

La primera sesión disponible de fabbro pide investigar una extensión para Pi ([P01](history/2026-10-14-pi-source-locators.md#p01)). Cuatro días después, el autor pide revisar conversaciones de Claude Code, Codex, Gemini y Amp para mejorar el uso de WAI ([P02](history/2026-10-14-pi-source-locators.md#p02)). Las herramientas ya se están evaluando a partir de fricción registrada, no solo de su diseño inicial.

Dont tiene su primer commit conservado el **20 de abril**, y pretender el **6 de mayo**. Para pretender, la solicitud de setup remite a un documento de diseño que ya existía ([P03](history/2026-10-14-pi-source-locators.md#p03)). Esto matiza la historia de una cadena de bugs que produce tools: a veces el repo implementa un diseño desarrollado antes y fuera de él.

Sobre dont, hay una explicación directa del autor el **10 de junio**: surgió después del artículo de Anthropic sobre vibe physics para buscar una forma de forzar duda y validez de claims ([P06](history/2026-10-14-pi-source-locators.md#p06)). Es una atribución retrospectiva explícita, no una conversación de concepción del 20 de abril. La fecha de creación del repo mencionada en los borradores anteriores sigue siendo una evidencia distinta.

### 12 de mayo: el pedido de un sistema fiable

A las 16:01 locales, el autor pide evaluar la combinación **dont, WAI y pretender** y pensar qué falta para crear un sistema fiable de desarrollo con IA ([P04](history/2026-10-14-pi-source-locators.md#p04)). En el intercambio posterior distingue feedback por herramienta, spec-to-assertion, drift y observabilidad para distintos harnesses.

A las 16:15 asigna el trabajo de spec-to-assertion a **espectacular** ([P05](history/2026-10-14-pi-source-locators.md#p05)). Los tickets `dont-nwck`, `pretender-5rk` y `wai-f0dv` registran feedback loops; `espectacular-e5w` se crea ese mismo día como tracer vertical dont → espectacular → WAI.

Acá tenemos una escena central para el post: no hace falta inventar el momento en que la familia empieza a pensarse como conjunto. Está en la conversación, y deja tickets con preguntas, entregables y revisiones.

**Discrepancia útil:** el primer commit alcanzable de espectacular está fechado el 14 de mayo, pero las solicitudes y tickets existen el 12. Un `git log --reverse` solo no habría contado bien el comienzo.

Los proyectos de aplicaciones —paranoid, atril, tRAGar, superficies y miblioteca— muestran el entorno en el que ocurren estas preguntas. Sus commits sitúan Android/WebView, visores de specs, RAG en browser, exploración visual y catalogación de libros. La intensidad o el costo por proyecto requiere una lectura separada del tracker; la cantidad de commits no mide esfuerzo ni comprensión.

## III. Junio: menor actividad y una integración concreta

El archivo Pi registra **17 sesiones iniciadas en junio**, frente a 259 en mayo. Esto describe los headers de este archivo, en UTC, y todos sus proyectos; no es una cuenta de horas, gasto ni toda la actividad del autor. Apoya una caída de actividad registrada, pero no prueba un abandono definitivo.

El **10 de junio** hay un pequeño circuito implementado:

| Repo | Registro | Cambio |
|---|---|---|
| dont | `08a8631a45` | Emisión de rejection events mediante `DONT_EMIT_EVENTS=1` |
| espectacular | `bc4d045af` | `ah signals` para leer drift signals de dont |
| WAI | `61f0963187` | `wai doctor` invoca `ah signals` con `WAI_DONT_SIGNALS=1` y muestra warnings |

`espectacular-e5w` se cierra ese día con una explicación del recorrido completo. El diff de WAI confirma el subprocess y la transformación de signals en checks.

La lectura precisa es **un tracer opt-in**, no una integración universal ni evidencia de adopción sostenida. Pero sí corrige la idea de que ningún tool consumía resultados de otro hasta octubre. Un circuito limitado ya existía en junio.

## IV. Julio: de tools parecidos a una infraestructura común

### Testaruda y los diseños que ya venían elaborados

El **7 de julio**, una solicitud en charly pide leer un SRS y configurar el repo que se llamará **testaruda**, no TIA ([P07](history/2026-10-14-pi-source-locators.md#p07)). El primer scaffold es `75414cb03`. Los tickets posteriores nombran fingerprinting, protocolo de adapters, shadow mode y contratos de exit codes.

Vampiro entra en git el **24 de julio** con un roadmap de especificación y tickets approval-gated. Livin y crua tienen setup conservado el **27**. Estos materiales permiten narrar una expansión de preguntas técnicas: selección de pruebas, composición, fronteras de valores y costos de ejecución. No permiten decir que todos esos productos quedaron implementados entonces.

### 27 de julio: consistencia, biblioteca y nombre

A las 19:06 locales, el autor pide evaluar la consistencia e integración de WAI, pretender, dont, espectacular, testaruda, crua y livin; agrega vampiro en el mismo intercambio ([P08](history/2026-10-14-pi-source-locators.md#p08)).

Después de discutir convenciones y propuestas por repo, pregunta si conviene una **biblioteca compartida** como base de las herramientas ([P09](history/2026-10-14-pi-source-locators.md#p09)). A las 19:57 elige el nombre **genesis** ([P10](history/2026-10-14-pi-source-locators.md#p10)).

El ticket `dont-2j6o`, creado el 15 de julio, ya proponía extraer el JSON envelope de dont. `genesis-4pa` generaliza esa extracción a infraestructura compartida. La nota whisper de genesis del 28 de julio enumera donantes, módulos, tests y propuestas de adopción. El conjunto nace de código y convenciones anteriores, no de una biblioteca que primero existió y luego creó la familia.

**Evidencia git:** `27ec9fe9e` registra la propuesta foundation; `ded8efd4d` el redactor de feedback; `d3c4eec7e` el serializer de context bundles. Los próximos snapshots narran config, guide y fixture y la adopción por los repos consumidores.

### La otra conversación del 27: preservar conocimiento operativo

En incitaciones, el autor cuestiona cómo se mezclan `.LOCAL_PLANS`, worktrees, cierre y journal. Propone guardar conocimiento global con niveles de repo/proyecto ([P11](history/2026-10-14-pi-source-locators.md#p11)) y luego llama **whisper** a lo que se venía proponiendo como lore ([P12](history/2026-10-14-pi-source-locators.md#p12)).

El commit `3542ea2a6f` de incitaciones registra el sistema `~/.whisper/` y las skills de sesión el 27 de julio local. **Whisper precede por más de un mes al repo del CLI.** Esta diferencia cambia la historia: primero se formalizó la práctica en instrucciones; después aparecieron errores mecánicos que justificaron un binario.

### 30 de julio: ddl

A las 12:48 locales, el autor pregunta si hace falta un bundle para simplificar setup e integración ([P13](history/2026-10-14-pi-source-locators.md#p13)). A las 12:54 elige **dulce-de-leche**, el comando **ddl**, y explicita el problema: centralizar configs bajo `.ddl/` para evitar poblar el root, descargar herramientas y migrar ([P14](history/2026-10-14-pi-source-locators.md#p14)).

El setup y los módulos de instalación y migración se registran ese día (`f5c5510a1`, `ec0aa613c`, `7040ace6f`). Los tickets `DDL-2te`, `DDL-r2t` y `DDL-w5k` especifican CLI, bootstrap y layout. Las notas whisper guardan la secuencia de propuesta, scaffold y siguientes pasos.

Esta escena explica ddl con la voz del autor y un problema concreto. No hace falta asumir una demanda externa que no aparece en la conversación.

## V. Agosto: reparar lo que la primera versión no resolvió

Los snapshots de ddl del **5 de agosto** registran arreglos de migración, idempotencia, symlinks, locking del manifest, descubrimiento de `.ddl/`, doctor y envelopes JSON, seguidos por integración de tests y release v0.3.0.

Son notas de reparación, no una validación independiente de eficacia. Para el relato importan porque desplazan el foco: instalar un bundle también introduce estado, reglas de compatibilidad y fallos que hay que mantener.

**Fuente whisper:** `~/.whisper/repos/cv/charly-vibes/dulce-de-leche/branches/main/notes.md`, apartados `2026-08-05 13:08` y `13:41`. La nota nombra tickets y archivos afectados; el historial local permite seguirlos. Las cifras de tests son las declaradas por la nota, no reruns de esta investigación.

## VI. Septiembre: las instrucciones se vuelven mecanismos

### De whisper a turu

El **1 de septiembre**, el autor reporta que whisper genera directorios de repo duplicados con distintos nombres ([P15](history/2026-10-14-pi-source-locators.md#p15)). Incitaciones registra canonical keys y consolidate en `96e39d2c4d`.

El **5 de septiembre** pide un CLI sobre genesis para hacer deterministas las operaciones de la skill, con configuración y separación por scope ([P16](history/2026-10-14-pi-source-locators.md#p16)). Los primeros commits son `f494c513c` (scaffold), `f0903231e` (comando turu, doctor y sync) y `0948e2a2f` (pack de skills).

El 15 de septiembre aparecen recall con presupuesto, distill en dos fases y consolidate (`4f27af0fa`, `6a54744c5`, `e217adf47`). La nota de consolidate cuenta un falso positivo en la detección de claves legacy y la corrección que exige una coincidencia más precisa antes de mover datos.

**Discrepancia de fuentes:** algunas notas rotulan el trabajo como 16 de septiembre, mientras commits y cierre de `whisper-ae0` lo sitúan el 15. Para fechar el cambio se prioriza el registro de git/Beads; la nota aporta el contexto del falso positivo.

La experiencia ofrece un tutorial natural: una regla aproximada puede servir para advertir, pero necesita otra precisión cuando decide mover conocimiento.

### Distribución y cambio de miembros del bundle

Ddl registra su instalación **binary-first con cargo fallback** el 15 de septiembre (`bd72a3651`). Incitaciones entra como paquete npm y turu como tool de la familia. El 28 de septiembre el registro elimina **fotos-mcp y fabbro** e incorpora **bd y OpenSpec** (`d5cd82c05`).

Por eso las tablas antiguas y actuales no describen exactamente el mismo conjunto. Fotos y fabbro siguen siendo parte de la historia, aunque hoy no sean miembros del bundle.

### Specodelic y bajan: ideas anteriores, nuevos repos

El **28 de septiembre**, el autor pide convertir un bundle `spec-format` en un CLI llamado **specodelic** sobre genesis ([P17](history/2026-10-14-pi-source-locators.md#p17)). La sesión del 23 de septiembre que reorganiza un bundle anterior también muestra que la investigación precedía al repo.

Ese mismo día pide crear **bajan** desde un informe de prácticas de knowledge graphs ([P18](history/2026-10-14-pi-source-locators.md#p18)). No son dos herramientas que necesariamente respondan al último bug local: llegan con material de diseño explícito.

**Git:** specodelic `661ca8234` (scaffold/rename), `3eeb5688f` (model-check), `dbb335120` (verify con ejecución de properties); bajan `e0f400766` (bootstrap). **Beads:** `bajan-6hz` se cierra el 29 de septiembre tras la vertical ingest→extract→SQLite→query.

### El capítulo de evaluación que faltaba en el primer inventario

**Evallerina** tiene scaffold conservado el 28 de septiembre (`00d56ecbd`). Su [README](../../evallerina/README.md) describe una batería de evaluación de consumo: si los agentes leen y actúan sobre envelopes, hints, bloques y discovery. El historial posterior incluye un agregador de fallos (`0499c62`), un harness de ablación AIX presente/ausente (`dcce78f`) y manejo de errores de transporte (`b677814`).

Esto impide repetir como diagnóstico vigente que el ecosistema nunca se evalúa a sí mismo. Existe infraestructura concreta de evaluación. Esta investigación no ejecutó modelos ni estimó tasas de éxito; disponer de un harness no demuestra todavía la utilidad global de la suite.

**Coffee y TV** también agregan una capa de observación: coffee separa el tracker de uso de microdancing; TV reúne y amplía el análisis de conferencias. Sus primeros commits pueden ser **historia heredada** por extracción de contenido. No se debe fechar la creación del repo usando automáticamente el primer commit heredado. [Coffee README](../../coffee/README.md), [TV README](../../tv/README.md).

## VII. Octubre: los consumidores devuelven problemas al ecosistema

### Archivar una spec puede romper su formato

`specodelic-fzo`, creado y cerrado el **1 de octubre**, recoge un pedido originado desde la migración de espectacular: OpenSpec archive descartaba frontmatter y tablas de la capa specodelic. Una receta local era un workaround; `spk archive-companion` convierte esa reparación en un mecanismo del tool (`0866ba7f5`).

Ah incorpora sync de Properties a contratos el mismo día (`88436bf68`). La integración puede contarse por el problema concreto que la empujó: preservar una spec al cambiar de fase y mantener su relación con las pruebas.

### Wild, consumidores de specs y un oracle externo

El **5 de octubre** se prepara **wild** desde un bundle ([P19](history/2026-10-14-pi-source-locators.md#p19)). Su implementación de contratos y composición tiene su propio roadmap; no hay que colapsarla con las garantías de vampiro porque comparten vocabulario.

El **6** aparecen los scaffolds conservados de **wanna** y **tambor**. Sus READMEs los sitúan como consumidores de specs/contratos para sistemas de interacción y UI. Ofrecen sitios donde estudiar si las herramientas efectivamente se combinan, además de testearlas sobre sí mismas.

El **8**, el autor pide portar **Graph::Easy a Rust**, empezando por specs sin implementación ([P20](history/2026-10-14-pi-source-locators.md#p20)). Gently adopta un oracle diferencial frente a la implementación Perl: tickets como `gently-2po.10` y `gently-0of` documentan el primer fixture y reparaciones del gate. Acá el comportamiento de referencia viene de fuera del tool que estamos construyendo.

### 9 de octubre: mirar las sesiones también necesita una herramienta

Desde los reports de pain y el trabajo previo de coffee se pide un tool pequeño en canticos. El nombre **terapia** queda elegido en la conversación ([P21](history/2026-10-14-pi-source-locators.md#p21)). Hoy esa CLI permite enumerar sesiones, inspeccionar tools y clasificar errores.

El script existe en `canticos/bin/terapia` y tiene tests; al consultar el historial de canticos no encontramos un commit con terapia en el asunto. La conversación y el working tree son fuentes distintas del git log. No asignar un SHA de implementación sin comprobar el diff correspondiente.

Ese mismo día `espectacular-0k8` propone usar selección de testaruda debajo de `ah check --run-tests`. La descripción cita una auditoría de sesiones —362 calls y 673 minutos— para justificar el cambio. **Esas cifras pertenecen a la auditoría del ticket; no fueron recalculadas acá.** El commit `a79d868af` implementa el refinamiento.

Esto ofrece un hilo crítico mejor que contar state dirs: una herramienta puede existir y aun así los agentes seguir ejecutando todo porque la interfaz no ofrece otra ruta. La reparación cambia la ruta disponible.

### 13 y 14 de octubre: el setup sigue siendo trabajo

Una nota de ddl del **13 de octubre** registra una auditoría de sesiones y una inspección de repos: el setup del fleet seguía realizándose manualmente en muchos casos. El ticket `DDL-fw7` especifica tres faltantes: bloque de ddl, reconciliación de installs con el manifest y pins.

El **14**, `975f835` implementa esas tres operaciones; `9122ce8` registra el merge de la rama. La revisión temporal es importante: el reporte del 13 no describe un fallo sin reparación para siempre. El siguiente día ya hay código que responde a parte de él. Esta investigación no repitió el sweep del fleet ni verificó su rollout completo.

El **13** también se configuran **sunset** y **funkalization** desde bundles de diseño. Para funkalization, la conversación fija la pertenencia al ecosistema ([P22](history/2026-10-14-pi-source-locators.md#p22)) y exige specs bajo OpenSpec sin duplicación ([P23](history/2026-10-14-pi-source-locators.md#p23)). Todavía debe distinguirse contrato, tracer persistente y UI completa.

## Repos periféricos que también pertenecen al recorrido

El inventario incluye proyectos que no están en el registro ddl y no necesitan convertirse artificialmente en CLIs:

- **Michael:** tema para desarrollo en pantallas en escala de grises; benchmark y gramática visual.
- **Fck:** kit de skills que explora la frustración como señal de falta de precisión en la interacción.
- **Coffee / TV:** medición de uso y corpus de investigación, con historia extraída de otros repos.
- **Evallerina:** evaluación del consumo de AIX por agentes.
- **Wanna / tambor / sunset:** consumidores y corpus que ejercitan especificación, UI y conocimiento documental.

Estos proyectos amplían la historia hacia lectura, diseño visual, evaluación y costo. Su papel debe justificarse con una experiencia o dependencia concreta en el relato. El [inventario completo](history/2026-10-14-repository-inventory.tsv) también conserva paseos, ruta, los sitios, canales de distribución y worktrees; la ausencia de un episodio fuerte no se rellena con una historia inventada.

## Escenas documentadas que pueden sostener el artículo

| Escena | Qué sabemos por las fuentes | Pregunta que abre |
|---|---|---|
| 12 de mayo: evaluar dont/WAI/pretender | Solicitud, respuesta, elección de espectacular y tickets | ¿Qué falta después de ordenar intención, claims y estructura? |
| 27 de julio: proponer una biblioteca | El autor pregunta por compartir infraestructura y elige genesis | ¿Cuándo varias herramientas parecidas necesitan un suelo común? |
| 27 de julio: abandonar LOCAL_PLANS | Se discuten scopes, journal y worktrees antes de nombrar whisper | ¿Dónde guardar lo aprendido para encontrarlo al volver? |
| 30 de julio: pedir un bundle | El problema de configs, descarga y migración aparece explícitamente | ¿Quién mantiene el entorno que necesita el agente? |
| Septiembre: claves duplicadas | Reporte del usuario, skill corregida y posterior CLI | ¿Qué parte de una habilidad conviene sacar del modelo? |
| Octubre: archive pierde información | Ticket desde un consumidor y companion implementado | ¿Qué se rompe entre dos herramientas que funcionan por separado? |
| Octubre: ah ejecuta demasiado | Auditoría citada en ticket y selección integrada | ¿Por qué el agente no utiliza una capacidad que ya existe? |
| Octubre: ddl no termina el setup | Audit/doctor, ticket y reparación fechada al día siguiente | ¿La promesa del orquestador aparece realmente en el camino cotidiano? |

La escena describe el intercambio y sus artefactos. El mate, el cansancio, una emoción o un diálogo reconstruido requieren testimonio del autor; estos registros no autorizan a inventarlos.

## Correcciones que el relato necesita conservar

1. **Whisper no nace en septiembre:** la skill está registrada el 27 de julio; septiembre es el CLI.
2. **La integración no empieza en octubre:** hay un tracer dont→ah→WAI en junio; octubre agrega otros puentes.
3. **No todos los repos nacen de una fricción inmediata:** varios llegan con diseños y bundles previos.
4. **Primer commit no es fecha de creación:** espectacular y los repos con historia extraída muestran por qué.
5. **El bundle cambia de miembros:** fotos/fabbro pertenecen al pasado de ddl aunque no al registro actual.
6. **Evaluación propia sí tiene un capítulo:** genesis y evallerina agregan infraestructura; falta distinguirla de resultados demostrados.
7. **Una nota de audit puede envejecer en un día:** DDL-fw7 ejemplifica reporte → ticket → implementación.
8. **Una pausa no es un final:** la caída registrada en junio convive con actividad técnica y el reinicio de julio.

## Qué sigue abierto para escribir la historia

Ya hay material suficiente para un relato cronológico con escenas reales. Permanecen abiertos los motivos originales de enero–marzo que no están en Pi, las fechas de creación GitHub cuando difieren del primer artefacto y los resultados sostenidos de uso fuera del desarrollo de los propios tools.

Antes de incluir cifras económicas, reconciliar tracker y versiones históricas en coffee: no mezclar estimaciones equivalentes, dinero efectivamente pagado ni cortes temporales distintos. Antes de un tutorial, ejecutar su ejemplo positivo/negativo con la versión elegida.

La tesis editorial puede emerger de estas escenas: el trabajo no fue únicamente producir más tools, sino mover decisiones desde instrucciones y conversaciones hacia mecanismos observables. La historia también muestra el costo de esos mecanismos, las promesas que todavía exceden la evidencia y las veces que el propio entorno hubo que volver a reparar.
