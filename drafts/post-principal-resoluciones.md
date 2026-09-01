# Post principal — resoluciones de la estructura (actualizado 2026-09-01)

> Documento de trabajo con decisiones y datos actualizados.
> Fecha: 2026-09-01

## Formato

- **Post grande** narrativo/ensayístico que funciona como columna vertebral
- **Posts-guías** separados después, detallando puntos específicos como guías prácticas

## Voz

- **Primera persona del singular** ("yo"), consistente con el resto del blog
- No dramático ni lamentoso — tono de crónica de exploración: "entramos a ver qué había, esto encontramos, esto aprendimos"
- Sabíamos que esto iba a pasar — nos metimos de cabeza a programar con IA a encontrarle las limitaciones

## Estilo narrativo

- **Periodístico**, imitando estructura de David Foster Wallace
- El tema emerge gradualmente con escenas concretas y digresiones que construyen tesis
- El lector descubre el patrón al mismo tiempo que el narrador

## Arco

- **Cronológico (Opción A)** — la historia tiene una curva dramática natural que los datos ya cuentan
- No es un arco trágico sino de expedición: a medida que nos íbamos sumergiendo surgían nuevas dudas

## Mecanismo narrativo

- **Escena → dato → pregunta** (Opción C)
- Datos del tracker como esqueleto ("qué pasó"), escenas como carne ("cómo se sintió")
- La tensión entre lo que *sentías* que pasaba y lo que *muestran* los datos es el motor narrativo

## Estructura en 3 partes

### Parte 1 — La exploración (enero–febrero, $0)

Entrás probando cosas sueltas. Fabbro, jams, nayra. Todo gratis, todo experimental. Rápido descubrís que la falta de organización te come — creás WAI. Explorás agentes con bichos. Descubrís que la infraestructura funciona bien (fotos). El patrón ya está ahí: cada herramienta nace de una fricción anterior, pero todavía no lo ves como patrón.

*Repos involucrados:* jams, fabbro, incitaciones, nayra, microdancing, wai, rizomas, bichos, fotos, homebrew-charly, scoop-charly

**Timeline:**
| Fecha | Repo | Propósito |
|---|---|---|
| Ene 7 | jams | Web experiments — mini-apps vanilla JS con spec y notas de sesión (el primero de todos) |
| Ene 9 | fabbro | Local-first code review TUI — anotar archivos con Fabbro Editing Markup para feedback loops con IA |
| Ene 12 | incitaciones | Prompts y skills reutilizables para LLM CLIs (pi, Claude Code, Amp, Gemini) |
| Ene 12 | nayra | Timeline Explorer — visualización de timelines sin framework, 60 FPS con 10k+ puntos |
| Ene 19 | microdancing | El blog |
| Ene 24 | charly-vibes | Home Page |
| Ene 31 | wai | CLI workflow manager — captura el *why* detrás de decisiones de diseño, no solo el *what* |
| Feb 10 | rizomas | Explicaciones rizomáticas — no jerárquicas, para ideas técnicas complejas |
| Feb 12 | charly-vibes.github.io | Home Page |
| Feb 14 | bichos | Framework bio-mimético multi-agente para QA autónomo usando swarm intelligence (propuesta) |
| Feb 19 | fotos | Screenshot capture + anotación con LLM vision, OCR, MCP server para integración con agentes IA |
| Feb 24 | homebrew-charly | Homebrew tap para herramientas charly-vibes |
| Feb 24 | scoop-charly | Scoop bucket para herramientas charly-vibes |

### Parte 2 — La aceleración y la saturación (marzo–mayo, $67 → $1,276/mes)

Claude entra. Los proyectos se vuelven ambiciosos (paranoid, dont). Dont nace de un paper externo (Anthropic «vibe physics») — no de la cascada local, señal de que ya estás leyendo el fenómeno. La creación se acelera: 7 repos en abril. Espectacular intenta poner orden con SDD.

*Repos involucrados:* khipu, flathub, canticos, paranoid, dont, atril, ruta, paseos, tRAGar, superficies, pretender, miblioteca, espectacular

| Fecha | Repo | Propósito |
|---|---|---|
| Mar 4 | khipu | Desenreda traces de ejecución de agentes LLM en patrones y antipatrones reutilizables |
| Mar 20 | flathub | Issue tracker y nuevos submissions |
| Abr 2 | canticos | Scripts de utilidad personal — clon de ZoomIt para GNOME, dashboard de IA, herramientas de video, whisper |
| Abr 7 | paranoid | App Android única con múltiples mini-apps como Activities nativas en Kotlin |
| Abr 16 | atril | Visores web para el ecosistema wai — spec file browser y grafo de dependencias de beads |
| Abr 18 | dont | Herramienta de disciplina epistémica para workflows LLM — claims con máquina de estados verificable |
| Abr 21 | ruta | Pi package para workflow de inmersión en specs de 7 días con extensiones, constants y skills |
| Abr 23 | paseos | (charly-vibes project — sin propósito definido) |
| Abr 29 | tRAGar | RAG del lado del cliente en el browser con transformers.js — zero-server, OPFS, Spanish-aware |
| May 4 | superficies | Catálogo de diseño para explorar dimensiones de web design con live preview |
| May 5 | pretender | Code quality checker multi-lenguaje — métricas ciclomática, cognitiva, ABC, nesting |
| May 6 | miblioteca | PWA para capturar fotos de lomos de libros con OCR para catalogación personal |
| May 12 | espectacular | Capa de verificación behavioral — enforce spec-test correspondence via CLI ah |

### Parte 3 — La pausa... y el reinicio (junio–septiembre)

Parás a fin de mayo. Extraés los datos en junio. Aparece el gap de enero 1-10. Pero después de la pausa, volvés — pero con un cambio de régimen: de Claude CLI bajo suscripción a OpenRouter pay-per-token, con herramientas más formalizadas (testaruda, vampiro, genesis, dulce-de-leche).

*Repos nuevos en esta fase:*
| Fecha | Repo | Propósito |
|---|---|---|
| Jul 7 | testaruda | Test selection engine language-agnostic — compute minimal test set from code change via provenance-semiring |
| Jul 24 | vampiro | CLI cross-language que verifica composición correcta entre boundaries (call, module, effect, law, retry, resource, trust) |
| Jul 27 | livin | CLI planeado para verificar que un test suite ejercita boundary values del código (zero, empty, singleton, etc.) |
| Jul 27 | crua | CLI planeado para verificar que el código respeta el modelo de costos de hardware (cache-line, dispatch, concurrencia) |
| Jul 27 | genesis | Crate Rust compartido de infraestructura cross-cutting CLI/AIX/self-healing para todo el tool suite |
| Jul 30 | dulce-de-leche | Un comando para instalar, configurar y actualizar todas las herramientas charly-vibes

## Patrón transversal

**Herramientas como respuesta a fricción.** Cada repo nace de una fricción del anterior:
- Fabbro → probar Vibe Coding, feedback loops con IA
- Nayra → algo que siempre quisiste, sin framework, 60 FPS
- WAI → muchos repos, configs repetidas, perder el hilo
- Bichos → Pydantic-ai, subscriptions limit, swarm intelligence
- Fotos → screenshots para feedback visual con IA
- Dont → paper externo de Anthropic (vibe physics), forzar duda y validez
- Espectacular → intentar poner orden con SDD, spec-test correspondence
- Khipu → traces de agentes imposibles de seguir
- Pretender → code quality sin revisión humana
- Testaruda → tests que no se ejecutan eficientemente
- Vampiro → composición entre lenguajes no verificada
- Genesis → shared infra duplicada entre tools
- Dulce de leche → instalar/configurar todo es tedioso

La pregunta que resuena: *¿cuándo una herramienta soluciona un problema y cuándo es un talismán contra la ansiedad?*

## Datos clave extraídos (v4, 2026-09-01)

- **133,819 interacciones** (deduplicado)
- Rango: 2026-01-11 → 2026-09-01
- **757 horas** con actividad, **141 días** activos, **56 proyectos**
- **Costo efectivo:** $3,782.58 (pay-per-token estimado)
- **Costo real:** $366.20
  - Suscripciones: $230.00 (Pro $20 + Max $100 + Pro $20)
  - Pay-per-token real: $136.20
- Gap enero 1-10: sin datos

### Mensual

| Mes | Reqs | Eff | Real | Sub | Herramienta principal |
|---|---|---|---|---|---|
| Ene | 929 | $0 | $0 | $0 | Amp |
| Feb | 719 | $0 | $0 | $0 | Amp |
| Mar | 263 | $0 | $0 | $0 | Amp |
| Abr | 20,671 | $1,110 | $110 | $110 | Claude CLI |
| May | 43,599 | $2,047 | $162 | $100 | Claude CLI |
| Jun | 8,271 | $325 | $24 | $20 | Claude CLI |
| Jul | 52,904 | $277 | $277 | $0 | OpenRouter (DeepSeek) |
| Ago | 6,040 | $23 | $23 | $0 | OpenRouter |
| Sep | 423 | $0.51 | $0.51 | $0 | OpenRouter |

### Cambio de régimen

- **Ene–Mar:** Amp + Gemini, $0
- **Abr–Jun:** Claude CLI, bajo suscripción ($20/$100/mes)
- **Jul–Sep:** OpenRouter, pay-per-token (DeepSeek V4 Flash domina)

### Sesiones Claude

- 1,884 sesiones totales
- 48% cortas (1-10 turns)
- 18% autónomas (con Agent)
- Sesión más larga: 1,001 turns (miblioteca, May 12)

### Top proyectos por costo efectivo

| Proyecto | Costo eff | Interacciones |
|---|---|---|
| miblioteca | $870 | 22,876 |
| dont | $403 | 15,523 |
| atril | $471 | 5,527 |
| wai | $147 | 4,437 |
| pretender | $78 | 4,466 |
| superficies | $71 | 1,898 |

### Skills más usados

| Skill | Usos |
|---|---|
| rule-of-5-universal | 115 |
| commit | 75 |
| issue-review | 38 |
| rule-of-5 | 22 |

## Contenido ya publicado

| Post | Cubre |
|---|---|
| Walk this WAI (Mar 2) | WAI, AIX, `--human`, filosofía de diseñar para la IA |
| Resonant Coding (Ene 25) | El método, Regla de los 5, Context Engineering |
| Sorcerer Algorithm (Feb 16) | Otro enfoque metodológico |

El post grande no debe repetir estos — debe contar la *experiencia* y el *viaje*, no la filosofía.

## Preguntas abiertas (resueltas)

1. **paseos** → ignorado por ahora, no tiene historia relevante
2. **Marzo (primeras 2 semanas, solo 263 interacciones)** → posiblemente un cambio de estructura en Claude que afectó los logs locales
3. **Detonante de la pausa de junio** → gradual, no hubo un momento puntual
4. **Paper de Anthropic que inspiró dont** → https://www.anthropic.com/research/vibe-physics