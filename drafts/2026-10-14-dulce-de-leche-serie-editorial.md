# Remando en dulce de leche — un relato y una serie de experiencias prácticas

Decisión editorial: 2026-10-14. Documento de trabajo; no es contenido publicado.

El proyecto tiene dos formas complementarias: **un post que recorre toda la historia** y **un post práctico propio para cada herramienta**. Ambos conservan la mirada crítica y la explicación técnica. El relato principal muestra cómo llegamos acá; cada tutorial permite experimentar un problema y entender qué cambia al incorporar una herramienta.

La base factual está en [la investigación del ecosistema](2026-10-14-dulce-de-leche-investigacion-estructura.md). Las decisiones anteriores de voz, cronología y escena → dato → pregunta están en [las resoluciones de septiembre](post-principal-resoluciones.md).

La reconstrucción desde Pi/terapia, git, tickets y whisper está en [la historia documentada](2026-10-14-historia-documentada.md). Sus localizadores y distinciones de fechas reemplazan las conjeturas cronológicas del primer esquema.

## 1. El post que cuenta la historia

Título de trabajo: **Remando en dulce de leche**.

Subtítulo posible: **Cómo fui construyendo herramientas para trabajar con agentes, y qué aprendí al intentar usarlas juntas.**

Pregunta que sostiene el recorrido: ¿qué pasa cuando cada límite de la IA encuentra una respuesta técnica, pero la suma de respuestas empieza a tener sus propios límites?

La historia debe incluir la exploración anterior a ddl, las herramientas que quedaron fuera del bundle, los intentos sin implementación, los cambios de rumbo y el estado actual. Ddl aparece cuando su necesidad se vuelve comprensible. La pertenencia al registro de hoy no decide qué experiencias merecen entrar en el pasado.

Voz: primera persona, crónica de exploración, humor en la precisión de las situaciones. Mantener dudas y resultados incómodos junto a lo que funcionó. Las escenas autobiográficas deben venir del autor o de registros confirmados; los ejemplos inventados se identifican como ejemplos.

### Apertura: encontrarse con el conjunto

Una escena actual y real que permita ver la acumulación: retomar un repo, recorrer un estado de herramientas o averiguar qué significa que un gate esté verde. La escena exacta está por elegir con el autor.

Mostrar el detalle que despierta una pregunta y volver al comienzo. No abrir con el inventario de nombres ni revelar toda la conclusión en el primer párrafo.

### I. Cuando todavía eran proyectos sueltos — enero y febrero

Jams y nayra: construir cosas que antes costaba empezar. Fabbro: cómo devolverle observaciones a la máquina. Incitaciones: conservar una práctica que acababa de funcionar. WAI: recuperar decisiones entre proyectos. Fotos: cerrar el circuito de feedback visual.

Bichos y rizomas pueden mostrar otras búsquedas: autonomía, organización de agentes y formas de explicar. Microdancing es parte del intento de entender y contar lo que estaba ocurriendo.

El aprendizaje de esta parte: producir rápido hizo visibles otros costos — feedback, contexto y coordinación. No afirmar que cada repo fue causado por el anterior cuando el registro solo demuestra proximidad temporal.

### II. Más velocidad, más cosas que verificar — marzo a mayo

Khipu y la dificultad de seguir traces. Dont y la disciplina de las afirmaciones; su inspiración en el paper externo de Anthropic debe conservarse, sin forzarla dentro de una cadena causal local. Pretender y la estructura del código. Espectacular y la relación entre comportamiento prometido y tests.

Atril, paranoid, tRAGar, superficies y miblioteca funcionan como escenarios donde aparecen las fricciones: infraestructura, interfaces, specs, review y comprensión. Canticos y ruta ayudan a situar las prácticas personales. Mencionar proyectos menores cuando aportan algo verificable al arco, sin inventarles una importancia que no tuvieron.

Acá entran las curvas de actividad, cambios de modelo y costos. Toda cifra lleva fecha de corte y definición: gasto pagado, costo equivalente estimado e interacciones no son intercambiables. Las resoluciones de septiembre también contienen discrepancias entre totales y filas mensuales; hay que reconciliarlas con los datos fuente antes de citarlas en el post.

La tensión: la velocidad para generar puede aumentar más que la capacidad de comprender y decidir. Contarla a partir de experiencias, sin presentar una explicación psicológica como dato medido.

### III. La pausa y la vuelta — junio y julio

La pausa fue gradual según las resoluciones anteriores. El reinicio y el cambio de régimen de uso deben aparecer: no conservar el cierre de junio como si todo hubiera terminado ahí.

Testaruda: qué tests vale la pena ejecutar ante un cambio. Vampiro: qué se rompe al componer piezas. Livin y crua: preguntas que llegaron a especificación sin convertirse todavía en aplicaciones. Genesis: la repetición de infraestructura entre herramientas. Ddl: instalar, configurar y mantener el conjunto.

Esta parte hace visible el costo de tener una familia de herramientas: releases, convenciones, drift y dependencias. No trasladar la cronología propuesta por los borradores a fechas definitivas sin verificarla en registros de repositorios.

### IV. El conjunto empieza a conversar — de la historia previa al estado de octubre

Turu convierte operaciones mecánicas de memoria en comportamiento determinista. Specodelic vuelve explícitas ciertas partes de una spec y sus claims de verificación. Wild explora compatibilidad de contratos; bajan, conocimiento con procedencia; gently, representación de grafos; funkalization, significado y autoridad de decisiones de diseño.

La historia documentada distingue whisper-skill (27 de julio), whisper-CLI (5 de septiembre), specodelic/bajan (28 de septiembre), wild (5 de octubre), gently (8 de octubre) y funkalization (13 de octubre), según las solicitudes y primeros artefactos disponibles. Evallerina, coffee y TV agregan evaluación e investigación; wanna, tambor y sunset muestran consumidores de los formatos. Las fechas de concepción o creación GitHub siguen siendo distintas de estas fechas de registro.

Mostrar dos o tres conexiones reales: ah/testaruda, OpenSpec/specodelic/ah e incitaciones/turu. Genesis compartido y distribución común tienen su lugar, pero son relaciones distintas de consumir resultados de otro tool.

### V. Volver a mirar lo construido

Confrontar la evaluación antigua con el estado observado: checksums incorporados, puentes existentes, documentación que puede quedar atrás y propuestas todavía abiertas. Explicar qué aprendimos de una crítica que también envejeció.

El cierre vuelve a la escena inicial con una pregunta más precisa: ¿qué evidencia permite decir que estas herramientas ayudan? Separar capacidades implementadas, tests propios, uso del autor y resultados para otras personas.

No hace falta resolver todos los proyectos para cerrar el relato. Sí hace falta nombrar qué sabemos, qué cambió y qué permanece abierto.

### Qué se lleva el lector

Una historia comprensible de decisiones y consecuencias, un mapa del ecosistema y criterios para evaluar prácticas similares. Cada herramienta recibe una explicación breve en su aparición histórica y un enlace a su experiencia práctica cuando exista. Los comandos extensos viven en los posts de herramientas.

El tamaño debe seguir la historia; como referencia editorial, 3.500–5.000 palabras antes de cortar repeticiones. Los posts publicados de Resonant Coding y Walk this WAI sirven como antecedentes: este recorrido cuenta qué ocurrió después de formular esas ideas.

## 2. Los posts por herramienta: tutoriales con una historia que avanza

La unidad narrativa es **un problema concreto que el lector aprende a resolver**. Cada post termina con un resultado observable y una explicación de su alcance. El nombre de la herramienta aparece después de que el lector entienda qué está en juego.

Audiencia: alguien que programa con agentes, puede ejecutar comandos y leer un archivo pequeño, pero no conoce nuestra suite. Cada post debe poder leerse de forma independiente.

### Secuencia editorial común

1. **Algo salió mal.** Mostrar un incidente real o un escenario didáctico declarado: decisión perdida, afirmación sin evidencia, cambio que deja un caso sin cubrir. Una situación específica, no una introducción genérica sobre IA.
2. **El intento razonable.** Mostrar qué hace el lector sin la herramienta y por qué ese intento es insuficiente en este caso. Comparar con una alternativa honesta, no una caricatura.
3. **La primera intervención.** Instalación o build mínimo con versión fijada; preparar los archivos necesarios y ejecutar una acción que ya revele algo útil.
4. **Leer lo que volvió.** Incluir salida real abreviada, explicar los campos decisivos y mostrar la decisión que permite tomar. Los bloques de comandos siempre cambian algo en la historia.
5. **Ponerlo a prueba.** Introducir un fallo deliberado o un caso límite y observar si el tool distingue ambas situaciones. El lector ve evidencia positiva y negativa.
6. **La reparación y el límite.** Corregir el problema, volver a ejecutar y explicar qué sigue fuera de la garantía. Incluir cuándo una solución más simple alcanza.
7. **Llevarlo al propio proyecto.** Dos o tres pasos de adaptación, con enlaces al reference para flags y opciones que no necesita este recorrido.

Estos movimientos no necesitan convertirse en los mismos siete encabezados en todos los posts. La serie debe tener coherencia sin que cada artículo suene producido por un molde.

Rango orientativo: 1.200–2.000 palabras para una CLI; más si el ejemplo necesita contexto. Prerrequisitos concretos, archivos completos pequeños, versión usada y forma de verificar el resultado. Sin salidas inventadas ni promesas sobre funciones todavía no implementadas.

## 3. Un ejemplo cercano que pueda reaparecer

Escenario didáctico candidato: **una pequeña biblioteca personal con importación de datos**. Una decisión explica cómo normalizar títulos, una spec promete rechazar entradas inválidas, un parser cambia, un test debe seleccionarse y un componente devuelve una forma que otro no acepta.

Este escenario conecta con proyectos existentes, pero no se presenta como un incidente autobiográfico. Puede tener fixtures pequeños y un requisito distinto por artículo. No obliga a instalar la suite completa: cada tutorial entrega su punto de partida y sus propios archivos.

WAI/turu/dont pueden tratar las decisiones y claims; OpenSpec/specodelic/ah, el requisito de importación; pretender/testaruda/vampiro/wild, código, tests y contratos. Fotos/fabbro usan escenas visuales o de review cuando eso sea más natural. Un solo ejemplo no tiene que justificar todos los tools.

## 4. Propuestas concretas para cada herramienta

Son briefs editoriales, no afirmaciones de que los ejemplos ya se ejecutaron. Los límites técnicos vienen de la investigación actual y deberán volver a comprobarse con la versión usada al escribir cada tutorial.

| Herramienta | Título de trabajo / situación | Recorrido práctico y resultado | Tensión crítica |
|---|---|---|---|
| WAI | **¿Por qué habíamos decidido eso?** Volver a un proyecto que ya no recordamos | Capturar una decisión con alternativas, cerrar la sesión y reconstruirla al retomar | Qué aporta frente a README, git log y una nota sencilla; recuperación medida en el ejemplo, sin prometer tiempos generales |
| turu / whisper | **La nota estaba, pero en la rama equivocada** | Resolver scopes, guardar una entrada y recuperarla con un presupuesto; mostrar rama/worktree y una revisión de distill | Routing determinista frente a calidad semántica de la memoria; qué queda fuera del presupuesto |
| dont | **Eso parecía un hecho** Una afirmación cambia una decisión técnica | Registrar claim, duda y evidencia; recorrer un rechazo y un gate aceptado | Un registro válido puede contener mala evidencia; el tool no reemplaza el juicio sobre fuentes |
| beads | **La tarea que estaba terminada hasta que miramos sus dependencias** | Descomponer un cambio, bloquearlo por una dependencia, resolverla y observar trabajo disponible | Cuándo el grafo ayuda y cuándo es más trabajo que una lista; declarar la configuración concreta usada |
| OpenSpec | **El cambio empezó como un párrafo** | Proponer una modificación pequeña, revisar su alcance y archivar sus deltas | Especificar no elimina decisiones; enseñar también cuándo el cambio es demasiado pequeño para este proceso |
| specodelic | **Una spec que puede contradecirse sola** | Dar estructura a un requisito, lintarlo y verificar un claim ejecutable con un contraejemplo y una reparación | Mostrar la frontera entre modelo verificado y aplicación; evitar el ejemplo vacío que solo prueba sintaxis |
| espectacular / ah | **El test pasaba. La promesa no tenía test** | Quitar un contrato o romper correspondencia, observar el gate y restaurar un test que pueda fallar por el motivo correcto | Correspondencia y test verde frente a calidad de la prueba; incluir el papel de Properties/sync si el ejemplo lo necesita |
| pretender | **El cambio pequeño que volvió enorme una función** | Medir un cambio estructural, interpretar el finding y comparar una reparación con el baseline | Las métricas pueden orientar y también incentivar cambios cosméticos; discutir el comportamiento preservado |
| testaruda | **¿Tengo que correr todos los tests por esto?** | Preparar dependencias, cambiar una función, seleccionar y explicar tests; repetir con una dependencia sin resolver | Comparar con la suite completa en el fixture y mostrar fallback; no extrapolar ahorro o recall al universo de proyectos |
| vampiro | **Dos piezas correctas que no encajan** | Construir un seam defectuoso en una combinación soportada, ejecutar check, interpretar y reparar | Distinguir análisis de composición de prueba de leyes; no enseñar `prove` como una función completa |
| incitaciones | **La instrucción que tuve que repetir por tercera vez** | Convertir una práctica en skill, instalarla y ensayarla en casos donde deba y no deba activarse | Corpus válido frente a comportamiento útil; un evaluador debe detectar el fallo y no premiar solo el formato |
| ddl | **Instalar todo también era un proyecto** | En workspace descartable, instalar un subconjunto, inspeccionar estado y recorrer una configuración/migración aplicable | Qué se centraliza y qué sigue afuera; verificar la integridad y las excepciones del método de instalación usado |
| genesis | **El mismo error, escrito de seis maneras** | Crear un CLI pequeño que use envelope y una capacidad compartida; provocar un error y comprobar el contrato de salida | Ganancia de consistencia y costo de acoplamiento/versiones; tutorial de biblioteca, no de usuario final |
| wild | **Compatible según quién** | Extraer contratos de un fixture soportado, introducir una incompatibilidad y comparar el resultado de check | Contratos extraídos y evidencia de compatibilidad frente a supuestos y cobertura del extractor |
| bajan | **Tengo la respuesta. ¿De dónde salió?** | Ingerir una fuente pequeña, extraer y consultar claims, seguir su procedencia | Procedencia de una afirmación frente a verdad; empezar determinista y aislar cualquier variante LLM |
| gently | **El diagrama que sí entra en la terminal** | Representar una dependencia pequeña, renderizar y cambiar una arista para ver el efecto | Un dibujo legible no demuestra que el modelo sea correcto; formatos realmente soportados |
| fotos | **El agente necesitaba ver lo que yo estaba viendo** | Capturar un defecto visual y anotarlo; recorrer el feedback visual en una plataforma soportada | Qué información entrega la imagen, qué sigue requiriendo juicio; separar captura de corrección automática |
| fabbro | **Cómo señalar un problema sin reescribir el archivo** | Anotar un fragmento con FEM, extraer feedback y verificar que el comentario apunte al lugar esperado | Feedback explícito frente a interpretación y cambios del agente; completar el ciclo de review |
| funkalization | **Mover una caja no cambia una decisión** | Experimento de laboratorio con el tracer persistente y proyecciones actualmente disponibles; contrastar un cambio semántico con representación | No presentar la UI prevista como producto disponible; mostrar los gates y claims que siguen abiertos |
| livin | **Todos los tests verdes, ningún caso vacío** | Explicar el problema con un fixture y una prueba ejecutable común; explorar la especificación de la herramienta | Post de diseño con experimento reproducible, hasta que exista implementación; no inventar una CLI |
| crua | **Correcto, pero caro** | Mostrar un costo concreto en un ejemplo medido y leer cómo la propuesta pretende detectarlo | Experimento de diseño hasta que exista implementación; mediciones específicas al entorno, sin universalizar |

Homebrew y Scoop entran en el post de ddl y en los pasos de instalación pertinentes. Son canales de distribución; no necesitan un artículo propio salvo que haya una historia técnica independiente que justifique esa decisión.

## 5. Cómo se leen juntas las dos formas

El post histórico enlaza a un tutorial cuando una fricción da origen a una herramienta. El tutorial devuelve un enlace al episodio de origen y, cuando hace falta, a un tool vecino. Ninguno exige haber leído toda la serie.

Como apertura editorial de la serie, WAI y turu ofrecen problemas reconocibles de memoria; specodelic y ah permiten mostrar una promesa y una refutación; testaruda completa un recorrido de verificación. El resto puede ordenarse por la historia o por el ejemplo que resulte más convincente. Esto es una propuesta de lectura, no un calendario de tareas.

Funkalization, livin y crua requieren un tratamiento explícito de laboratorio mientras no tengan la capacidad necesaria para un tutorial de uso completo. Deben tener su lugar propio sin confundirse con herramientas maduras.

## 6. Criterio de revisión editorial

Un lector debería poder responder, después de cada artículo: qué ocurrió, por qué intentamos esto, qué ejecuté, qué observé, qué aprendí y qué puedo llevar a mi proyecto. Si solo recuerda una lista de comandos, falta la historia. Si solo recuerda una reflexión, falta el tutorial.

El post principal ya tiene escenas de intercambios documentados y una cronología tardía con fuentes. Los detalles autobiográficos y motivos iniciales que no aparecen en los registros necesitan testimonio del autor. Los posts prácticos necesitan ejemplos ejecutados con evidencia positiva y negativa. El próximo desarrollo editorial debe elegir un episodio y un fixture, antes de producir una introducción genérica o una serie de comandos sin resultado.
