---
title: "Boceto v2: Serie de posts — 6 meses de aprendizaje con IA"
date: 2026-06-10
status: boceto-v2
---

# Boceto v2: Serie de posts — 6 meses aprendiendo a trabajar con IA (y la decisión de parar)

> Este boceto captura todos los puntos que querés cubrir. La estructura definitiva la armamos después. Acá está el inventario completo de temas, organizado por ahora en categorías lógicas pero sin orden narrativo todavía.

---

## Inventario de temas a cubrir

### 📊 Datos duros y visualizaciones

- **Gráfica de uso de tokens en el tiempo.** Usar `canticos/bin/llm-dashboard.py` que ya genera dashboards con: costo diario por modelo, sesiones por día, heatmap de actividad, skills más usados. Extraer los datos como series temporales para integrarlos en los posts.
- **Línea de tiempo: creación de repos superpuesta al uso de tokens.** Que se vea cómo explota la cantidad de repos justo cuando el uso de tokens se dispara (abril 2026). Mostrar que no es coincidencia: más repos → más tokens → más repos.
- **Cambio de modelos en el tiempo.** Claude Opus 4.5/4.6, Sonnet, Haiku, Gemini, etc. Cada modelo se usó en distintas fases y el dashboard ya trackea `model` por cada turno. Se puede generar una línea de tiempo de "qué modelo usaba y cuándo" para correlacionar con los resultados.
- **Líneas de código generadas.** Usar `git log --stat` o similar en todos los repos para mostrar el volumen de producción y cómo se aceleró.

### 🔄 La trampa de la abundancia

- **El momento donde tener demasiados repos es peor que no tener ninguno.** Entrar a la lista de repos y no saber qué hace cada uno. Sentirse como un jardinero que plantó cien semillas y no se acuerda qué es cada brote.
- **Crear herramientas para suplantar limitaciones de la IA.** Cada vez que la IA hacía algo mal, la respuesta era crear una nueva herramienta para "solucionarlo" en vez de cambiar la forma de trabajar. Herramientas que no iban a ningún lado porque el problema no era técnico, era de proceso.
- **Features que nadie usa.** La explosión de features sin propósito real. La velocidad permite construir cualquier cosa, pero no te dice *qué* construir. La pregunta "¿esto realmente se necesita?" se vuelve invisible cuando el grifo de tokens está abierto.
- **Perder el hilo.** No poder seguir lo que la IA generaba. PRs que nadie terminaba de leer. Código que funcionaba pero nadie entendía cómo. La paradoja de la IA es que cuanto más productiva te hace, menos entendés tu propio sistema.

### 🏗️ El beneficio real: infraestructura

- **Despreocuparse de la infraestructura es donde la IA brilla de verdad.** No en el código de lógica de negocio, sino en todo el trabajo *alrededor* del código: CI/CD, empaquetado, builds, scripts de deploy, flatpak, firmado de APKs.
- **Fotos como caso estrella.** Tauri 2, Flatpak, GNOME extension, MCP server, keychain integration, soporte Wayland/X11. Un proyecto con una complejidad de infraestructura enorme que, sin IA, probablemente nunca se hubiera intentado hacer solo. El deploy funciona y no hay que pensarlo.
- **Paranoid como segundo caso.** Android, keystore, builds para múltiples targets. Infraestructura que tradicionalmente requiere semanas de configuración, resuelta en sesiones.
- **La pregunta incómoda:** ¿cuánto de lo aprendido es transferible si la IA hace la infraestructura invisible? ¿Qué pasa cuando el workflow de deploy se rompe y no sabés cómo arreglarlo?

### 👤 El desarrollador solitario

- **Todos los proyectos son unipersonales.** No hay otros contribuidores. El usuario es el único humano en el loop.
- **Explorar nuevas formas de trabajo en solitario.** Cuando no hay equipo, no hay code reviews humanos, no hay discusiones de diseño, no hay "¿por qué hiciste esto así?". Todo el feedback viene de la IA. ¿Cómo se desarrolla el juicio técnico sin interlocutores humanos?
- **El problema de abrir proyectos al público.** Cuando no hay otros contribuidores, no hay documentación para onboarding, no hay issues de otros, no hay PRs de otros. El repositorio es un jardín privado hecho público, no un proyecto open source real. ¿Cómo se transiciona de uno a otro?
- **La soledad del juicio.** Sin colegas, la pregunta "¿esto está bien?" solo tiene dos respuestas: la tuya y la de la máquina. ¿Cómo calibrar cuándo confiar en cada una?

### 🖼️ El infierno de las UIs web

- **Las UIs web son el punto más frágil del desarrollo con IA.** Porque son visuales, porque requieren consistencia estética, porque la IA no "ve" lo que genera de la misma forma que el humano.
- **Nayra y el timeline explorer.** Primer intento de spec-driven development aplicado a UI. La lucha por encontrar un lenguaje común con la IA para describir interfaces.
- **Superficies y el diseño visual.** El repositorio lleno de screenshots de verificación. Cada iteración requiriendo capturas para que la IA "vea" lo que generó. El loop: prompt → código → screenshot → "no, el botón está corrido 3px" → prompt → código → screenshot → ...
- **La falta de un lenguaje compartido.** Con backend, el lenguaje de la IA (funciones, tipos, tests, JSON) es cercano al humano. Con UI, la IA no tiene un buen modelo de "esto se ve bien" y el humano no tiene un buen modelo de "esto se construye así". La brecha es más ancha.

### 🎛️ CLI tools: el patrón `--human`

- **Dont como caso de estudio de diseño de CLI para IA.** La decisión de que el output default sea JSON y que `--human` sea el flag opcional. Invertir el patrón tradicional (donde `--json` es el opt-in) porque el consumidor principal ya no es un humano, es otro LLM.
- **WAI como tratado diplomático.** Diseñado para que lo lea la IA, no el humano. El usuario principal no respira.
- **La evolución:** primero CLI para humanos, después CLI para máquinas, después CLIs que hablan entre sí. El lenguaje cambia porque el interlocutor cambió.

### 📋 Spec-Driven Development: la fricción

- **Espectacular como caso de fricción agregada.** SDD suena bien en teoría, pero en la práctica agrega burocracia. Cada feature requiere especificación + test contract + validación + supersession management. El proceso se vuelve más pesado que el problema que resuelve.
- **La pregunta:** ¿cuándo el SDD es valioso y cuándo es un talismán contra la ansiedad? ¿Cuándo la formalización del proceso ayuda y cuándo se convierte en un fin en sí mismo?
- **Nayra y el primer intento de OpenSpec.** La inspiración original. Por qué OpenSpec ya no existe como repo (humanlayer/openspec dio de baja el repo). ¿Qué queda de esa idea?
- **El equilibrio entre especificación y velocidad.** Cuanto más especificás, menos podés iterar. Cuanto menos especificás, más te perdés. No hay respuesta correcta, solo trade-offs que cambian con el tiempo.

### 🤖 Procesos autónomos sin propósito

- **El momento donde la IA empieza a generar código sin que nadie se lo pida.** Workflows autónomos que producen código que nadie pidió, para problemas que nadie tiene. La herramienta empieza a crear su propia demanda.
- **Bichos y la exploración de organizaciones de agentes.** Múltiples IAs hablando entre sí. ¿Qué pasa cuando el output de un agente es el input de otro? ¿Quién es responsable del resultado final? ¿Tiene sentido?
- **Khipu y la necesidad de desenredar.** Cuando el sistema es tan complejo que necesitás una herramienta para entender qué están haciendo tus herramientas. Khipu como meta-herramienta: "untangle agent traces into patterns."
- **El vértigo de la autonomía.** El código se genera solo. Los PRs se crean solos. Las features se proponen solas. El humano queda como un espectador que aprueba o rechaza, pero ya no conduce.

### 🧠 Lo que aprendí (y lo que no)

- La diferencia entre **velocidad de producción** y **velocidad de comprensión**. Puedo generar código 10x más rápido, pero no puedo entenderlo 10x más rápido. Esa asimetría es el problema fundamental.
- La diferencia entre **tener herramientas** y **saber usarlas**. 70 skills, ~30 repos, pero ¿cuántos se usan realmente? El catálogo como síntoma de ansiedad.
- La diferencia entre **resolver un problema** y **evitar la incomodidad de no saber**. Muchas herramientas fueron para no tener que enfrentar la pregunta incómoda.
- **Lo que la IA no puede hacer (todavía)** : decidir qué merece ser construido, sentir la fricción de un diseño incorrecto, tener intuición sobre lo que va a escalar, saber cuándo parar.
- **Lo que la IA sí puede hacer (y muy bien)** : infraestructura, refactors mecánicos, tests, documentación, exploración de alternativas, code review. El trabajo aburrido que un humano no haría o haría mal.

---

## Materiales disponibles

### Para el historial de herramientas y costos hora a hora

`scripts/usage-tracker.py` extrae datos de:

- **Claude** (~/.claude/projects/ + dashboard cache) → modelo, tokens, costo por turno
- **Pi** (~/.pi/agent/sessions/) → 450 sesiones con provider (Codex, Claude CLI, Gemini CLI, OpenRouter, Copilot) + modelo + costo
- **Codex** (~/.codex/) → history.jsonl + SQLite logs
- **Gemini** (~/.gemini/tmp/) → actividad por timestamp
- **Amp** (~/.amp/file-changes/) → cambios autónomos

Produce:
- `data/usage_hourly.json` → 597 buckets hora a hora con interacciones, tokens, costos, tools, modelos
- `data/tool_timeline.json` → primera/última vez de cada herramienta
- `data/daily_summary.json` → 122 días de resumen diario

```bash
python3 scripts/usage-tracker.py
```

### Para la línea de tiempo de repos

```bash
gh repo list charly-vibes --json name,createdAt
```

Da la fecha de creación de cada repo. Se puede superponer con las gráficas de uso.

### Para líneas de código

```bash
# En cada repo
git log --shortstat --reverse --format="%ai" | ...
```

O usar `cloc` o `tokei` para snapshot por fecha.

### Para el timeline de modelos

`llm-dashboard.py` ya trackea el modelo por cada turno. Se puede extraer una serie temporal de qué modelo predominaba en cada período.

---

## Posibles títulos / ejes narrativos

- "El año en que dejé de escribir código" (título del post grande)
- "La trampa de la abundancia" (el momento de muchos repos, mucho uso, poco entendimiento)
- "Contra la burocracia del spec" (SDD, espectacular, cuándo la formalización ayuda y cuándo estorba)
- "El usuario que no respira" (CLIs para IAs, el patrón `--human`, WAI, dont)
- "El jardín que nadie riega" (proyectos unipersonales, abrir al público)
- "El botón que está 3px a la izquierda" (la fragilidad de las UIs con IA)
- "El despliegue que funciona solo" (infraestructura como beneficio real)
- "Herramientas contra la ansiedad" (cuándo un skill es una herramienta y cuándo es un talismán)
- "La caminata" (Walk this WAI — el cierre, la decisión de parar)

---

## Estado del material

Algunos repos están sin documentar: `superficies`, `ruta`, `paseos`, `tRAGar`, `pretender`, `miblioteca`, `espectacular`, etc. Algunos tienen readme, otros no. Algunos son experimentos que nacieron y murieron el mismo día.

Para el post principal, cada repositorio cuenta una historia —incluso los que no tienen readme— porque la ausencia de documentación también es un dato sobre la velocidad a la que se estaba produciendo.

Lo que no tiene historia que contar, no se fuerza.

---

## Datos reales extraídos (2026-06-10)

Ejecutando `scripts/usage-tracker.py` sobre los datos locales:

**72,392 interacciones únicas**, **597 horas**, **122 días de actividad**, **~$2,608 en costos.**

### Timeline de herramientas

| Herramienta | Primera vez | Última vez | Interacciones | Costo |
|---|---:|---:|---:|---:|
| **Gemini CLI** | 2023-06-26 | 2026-05-21 | 1,112 | $0 |
| **Amp** (autónomo) | 2025-12-18 | 2026-05-05 | 2,782 | $0 |
| **Claude CLI** | 2026-03-16 | 2026-06-10 | 55,123 | **$2,122.41** |
| **Codex** (GPT-5.4/5.5) | 2026-04-14 | 2026-06-05 | 12,948 | $484.10 |
| **Copilot** | 2026-04-14 | 2026-04-16 | 2 | $0 |
| **OpenRouter** | 2026-06-05 | 2026-06-10 | 425 | $1.55 |

### Tendencia mensual

```
2023-06  ▏ 1 interacción      Gemini, una prueba aislada
2025-12  ██ 105                Amp empieza, Gemini esporádico
2026-01  ██████████ 1,077      Nacen jams, incitaciones, nayra (sin Claude aún)
2026-02  ████████ 806          WAI, bichos, rizomas
2026-03  ███████ 739   $67     Claude CLI entra, Resonant Coding, Algoritmo Brujo
2026-04  ██████████████████████████████ 22,059  $1,260  — EXPLOSIÓN
2026-05  ██████████████████████████████████████████████████████ 45,714  $1,276  — PICO
2026-06  ██████ 1,891  $5      — LA PAUSA (datos hasta el 10)
```

El cambio entre enero (1,077 interacciones, $0) y abril (22,059, $1,260) es de **20x en interacciones** y de **$0 a $1,260/mes en costos.** La pausa de junio se ve clarísimo: 1,891 interacciones en 10 días, proyectando ~5,700/mes — una caída del 87% respecto al pico de mayo.

### Modelos usados

| Modelo | Interacciones | Dónde se usó |
|---|---|---|
| Claude Sonnet 4.6 | ~12,932 | Claude CLI + Pi/Claude |
| GPT-5.4 (Codex) | ~9,787 | Pi/Codex |
| GPT-5.5 (Codex) | ~3,014 | Pi/Codex |
| Claude Opus 4.7 | ~2,226 | Claude CLI |
| Claude Opus 4.6 | ~2,041 | Claude CLI |
| Gemini 3 Pro | ~553 | Pi/Gemini |
| DeepSeek V4 Flash | ~378 | Pi/OpenRouter |
| Otros | ~461 | Varios |

---

*Próximo paso: definir la estructura narrativa con todos estos elementos integrados.*