---
title: "Resonant Coding: o cómo dejé de preocuparme y aprendí a amar el caos"
date: 2026-01-25
lang: es
translations:
  en: /en/resonant-coding
---

<nav class="progress-nav"><a href="#s1">1</a> <a href="#s2">2</a> <a href="#s3">3</a> <a href="#s4">4</a> <a href="#s5">5</a> <a href="#s6">6</a> <a href="#s7">7</a> <a href="#s8">8</a></nav>

Hay un fenómeno que ocurre cuando uno mira demasiado tiempo una pantalla con código que no entiende[^codigo-ajeno]. El cerebro empieza a hacer algo parecido a lo que hace cuando mirás nubes: busca patrones, caras, formas familiares. Solo que en vez de ver un conejo o el perfil de tu tía Marta, empezás a ver intenciones. Propósitos. Una lógica que seguramente está ahí, que tiene que estar ahí, porque alguien —o algo— lo escribió con algún objetivo en mente. El problema es cuando ese algo es un modelo de lenguaje y el objetivo era simplemente generar la secuencia de caracteres más probable dada una entrada, lo cual, si uno se detiene a pensarlo con la seriedad que merece, es una forma bastante perturbadora de crear las instrucciones que van a mover dinero, controlar sistemas, decidir cosas.

Esto no es una exageración paranoica[^paranoia]. O tal vez sí. Pero durante los meses que pasé liderando un equipo de desarrollo —un equipo nuevo, armado desde cero para dar soporte a un área que manejaba números con muchos ceros— esa paranoia se convirtió en algo parecido a una metodología, o al menos en algo que funcionaba mejor que no tener nada, que era exactamente lo que teníamos antes.

<span class="progress-marker" id="s1">⸻ 1/8 ⸻</span>

El contexto, porque el contexto siempre importa aunque uno preferiría que no: había presión desde arriba para usar Inteligencia Artificial y acelerar todo[^presion]. El equipo tenía pocos desarrolladores con experiencia, lo cual significaba que yo tenía que revisar casi todo. Y cuando digo "casi todo" me refiero a esa situación particular donde cada *pull request*[^pr] que llegaba era como abrir una caja de Pandora manufacturada por un oráculo estadístico que había leído todo internet pero no necesariamente había entendido nada de lo que leyó[^entender].

Los primeros meses fueron un desastre en cámara lenta. Código que a primera vista parecía razonable pero que, al examinarlo, revelaba estructuras que ningún programador humano hubiera elegido. Soluciones que funcionaban pero por las razones equivocadas. Patrones que olían a algo, pero no sabías a qué hasta que explotaban en producción en el peor momento posible, momento en el cual descubrías que el modelo había interpretado "validar la entrada del usuario" como "no tocar nada y esperar que no explote".

Hubo un momento —y esto es importante para entender por qué eventualmente dejé de confiar en las soluciones mágicas— donde la calidad del código que entregaba el equipo mejoró de forma drástica. Por aproximadamente cuarenta y ocho horas gloriosas pensé que habíamos logrado algo. Que el método que veníamos refinando estaba funcionando. Que éramos, finalmente, buenos en esto.

Después descubrí que Cursor[^cursor] se había actualizado.

No éramos nosotros. Era el modelo. Y si el modelo podía mejorar sin nuestra intervención, también podía empeorar. O cambiar de formas que no entendíamos. O ser reemplazado por otro modelo con otras idiosincrasias que tendríamos que aprender desde cero. Estábamos construyendo sobre arenas movedizas y celebrando cada vez que las arenas, por un momento, dejaban de moverse[^arenas].

<span class="progress-marker" id="s2">⸻ 2/8 ⸻</span>

Tengo que hacer un desvío acá porque sin este desvío nada de lo que sigue va a tener sentido, y además es el tipo de desvío que disfruto porque involucra ondas, y las ondas son hermosas de una manera que el código rara vez logra ser[^ondas-hermosas].

Hace unos años, una noche, en uno de esos pozos de YouTube donde uno termina sin saber cómo[^pozo], encontré un video de una demostración de física[^estacion]. Alguien agarra una soga —o una cuerda, o algo parecido— y la empieza a agitar. Al principio es puro caos. Movimiento sin forma, ondas que chocan entre sí, interferencia destructiva por todos lados. Pero si encontrás la frecuencia correcta, si agitás a exactamente el ritmo necesario, algo extraordinario pasa: el caos se ordena. Aparecen puntos que no se mueven —los nodos— y puntos que oscilan al máximo —los antinodos—. Ondas estacionarias. Patrones que se sostienen solos porque el sistema entró en resonancia.

Me quedé mirando ese video probablemente más veces de las que admitiría en público. La idea de que el caos contiene estructuras latentes esperando a que alguien encuentre la frecuencia correcta para revelarlas. Que el desorden no es ausencia de orden sino orden potencial buscando manifestarse[^potencial].

Y años después, mientras miraba otro *pull request* incomprensible y me preguntaba cómo carajo íbamos a salir de este pantano, me acordé de las ondas estacionarias. Y pensé: tal vez el problema no es la IA. Tal vez el problema es que estamos agitando la soga a cualquier frecuencia y esperando que aparezcan patrones. Para encontrar la frecuencia correcta, primero había que entender la soga.

<span class="progress-marker" id="s3">⸻ 3/8 ⸻</span>

Los modelos de lenguaje, para quien no haya tenido el placer de interactuar con ellos más allá del chat ocasional, son esencialmente máquinas de predicción de texto. Esto suena simple y en cierto sentido lo es: les das una secuencia de palabras y te devuelven la palabra más probable que sigue. Como el autocompletado del celular pero entrenado con una cantidad de datos que es difícil de conceptualizar sin recurrir a metáforas astronómicas[^datos].

El problema es que esta simplicidad fundamental genera comportamientos emergentes que parecen inteligencia, que a veces funcionan como inteligencia, pero que no son inteligencia en ningún sentido que un filósofo de la mente encontraría satisfactorio[^filosofo]. Son simulacros de razonamiento construidos a partir de patrones estadísticos. Y esto tiene consecuencias prácticas muy concretas:

**No tienen memoria.** Cada vez que les hablás es como si fuera la primera vez. El modelo que te ayudó a resolver un bug hace cinco minutos no tiene idea de que existís, ni de que hubo un bug, ni de que lo resolvieron juntos. Lo que algunas herramientas llaman "memoria" es en realidad un truco: guardan parte de la conversación anterior y la pegan silenciosamente al principio de cada mensaje nuevo. Es memoria prostética, artificial, y tiene límites[^memoria].

**Su atención es limitada.** Tienen una ventana de contexto —la cantidad de texto que pueden procesar a la vez— y cuanto más larga es la entrada, peor funcionan. La mejor manera de pensar esto es imaginar que tenés un balde de agua y tenés que lavar platos[^balde]. Para un plato, el balde sobra. Para diez, el agua empieza a enturbiarse. Para cien, el agua está tan sucia que los últimos platos salen peor de lo que entraron. Y si en algún momento tirás algo grasoso al balde —información irrelevante, contexto que no viene al caso— el agua queda inutilizable para todo lo que sigue. Además, la degradación no es uniforme: las partes del principio y las partes del final del contexto reciben más atención que el medio, lo cual explica por qué a veces el modelo "olvida" instrucciones que le diste tres párrafos antes[^atencion].

**Son probabilísticos.** Para la misma entrada pueden dar salidas diferentes. Esto suena menor pero tiene implicaciones profundas: no podés confiar en que un resultado que funcionó una vez va a funcionar de nuevo. Cada interacción es un dado siendo tirado, y a veces sale siete y a veces sale una serpiente que te come el prompt[^dados].

<span class="progress-marker" id="s4">⸻ 4/8 ⸻</span>

En algún momento del verano, durante unas vacaciones que pasé leyendo sobre IA en vez de descansando —porque aparentemente tengo una relación disfuncional con el tiempo libre—, encontré dos líneas de pensamiento que eventualmente convergieron en lo que ahora llamo Resonant Coding. Una venía de Steve Yegge, un programador que lleva décadas escribiendo sobre software con una mezcla de brillantez técnica y opiniones que oscilan entre lo visionario y lo deliberadamente provocador[^yegge]. La otra venía de Dex Horthy y su concepto de *Context Engineering*, que es básicamente la idea de que el contexto que le das a un modelo importa más que cualquier otra cosa[^context].

De Yegge tomé algo que él llama la Regla de los 5, que no es tanto una regla como un proceso iterativo de refinamiento. La versión simplificada es: cuando generás algo, lo pasás por cinco filtros sucesivos. Primero un borrador donde lo importante es que esté todo, aunque esté desprolijo. Después una revisión de exactitud donde arreglás errores factuales. Después claridad, donde simplificás y eliminás ambigüedades. Después casos límite, donde pensás en todo lo que podría salir mal. Y finalmente excelencia, donde pulís y optimizás[^cinco].

De Horthy tomé la obsesión por el contexto. La formalización de lo que ya intuía con la metáfora del balde: que la calidad de lo que le das al modelo determina la calidad de lo que te devuelve, y que si el problema es demasiado grande para un solo balde, tenés que dividirlo en partes más pequeñas y usar agua limpia para cada una.

Estos dos conjuntos de ideas, combinados con la desesperación profesional que ya mencioné y una cantidad moderada de cafeína, cristalizaron en algo que parecía funcionar. No inventamos nada nuevo —simplemente pegamos dos ideas que ya existían y les pusimos un nombre pretencioso—, pero a veces la innovación es exactamente eso: ver que dos piezas encajan cuando nadie las había puesto juntas.

<span class="progress-marker" id="s5">⸻ 5/8 ⸻</span>

No voy a describir el método como una serie de pasos numerados porque eso sería traicionar el espíritu de cómo realmente funciona, que es más caótico, más iterativo, más parecido a una espiral que a una escalera. Pero hay tres movimientos generales que se repiten:

Primero está lo que podríamos llamar investigación —aunque "reconocimiento del terreno" captura mejor la sensación. Antes de hacer cualquier cosa, hay que entender el problema. Y acá es donde el modelo puede ayudar: le pedís que investigue el código existente, que mapee dependencias, que encuentre documentación relevante, que te cuente qué mierda está pasando en este sistema que heredaste de alguien que ya no trabaja acá[^herencia]. El modelo hace este trabajo bastante bien porque es esencialmente lectura y síntesis, que es exactamente para lo que fue entrenado.

Pero —y este pero es crucial— el documento que genera el modelo tiene que ser revisado. No aceptado, revisado. Con la Regla de los 5 o con algo parecido, no importa, pero con la convicción firme de que el modelo pudo haber entendido mal, pudo haber inventado cosas, pudo haber mezclado información de diferentes proyectos porque en su entrenamiento leyó código parecido y se le cruzaron los cables[^alucinaciones]. La revisión humana acá no es opcional; es el punto entero del ejercicio.

Después viene algo parecido a planificación, que es usar el documento de investigación (ya revisado) para generar un plan de acción. El truco acá es que cada tarea del plan tiene que ser lo suficientemente pequeña como para caber en un solo balde. Si una tarea es "implementar el sistema de autenticación", es demasiado grande. Si es "agregar la validación del token JWT en el endpoint de login", estamos mejor[^beads]. Y cada una de estas tareas pequeñas pasa, de nuevo, por la Regla de los 5, porque un plan mal definido puede generar miles de líneas de código incorrecto y para ese punto ya es tarde[^tarde].

Y finalmente está la implementación, que para este punto debería ser casi mecánica. Cada tarea está tan bien definida que el modelo no tiene espacio para inventar. Y acá es donde los modelos brillan de verdad: pueden editar veinte archivos en segundos, pueden crear baterías de tests, pueden refactorizar estructuras completas. Lo que a un humano le llevaría horas. Pero solo porque el trabajo difícil —el de pensar— ya se hizo antes[^pensar].

<span class="progress-marker" id="s6">⸻ 6/8 ⸻</span>

Sé lo que parece: otro método más que promete eficiencia. Pero la narrativa dominante sobre la IA en programación me molesta profundamente: la idea de que estas herramientas te permiten "ir más rápido". No es falso, exactamente, pero tampoco es verdad de la forma en que usualmente se presenta. Es como decir que un auto te permite llegar más rápido a destino: cierto, pero solo si sabés manejar, si conocés el camino, si el auto está en buen estado, si las rutas están despejadas. Si no se cumplen esas condiciones, el auto te puede llevar muy rápidamente a cualquier lado, incluyendo un barranco[^barranco].

Con la IA pasa lo mismo. Sí, puede generar código más rápido de lo que cualquier humano podría escribirlo. Pero generar código no es lo mismo que resolver problemas. Y si generás código sin entender el problema, lo que obtenés es una solución rápida a la pregunta equivocada, que es peor que no tener solución porque ahora tenés que deshacer lo que hiciste antes de poder avanzar.

El método que describo no es un atajo. Es un proceso que toma más tiempo que tirarle un prompt al modelo y esperar que salga algo bueno. Pero ese tiempo se recupera multiplicado porque los errores se detectan temprano, porque el trabajo no tiene que rehacerse, porque cuando algo se implementa ya se sabe que es lo correcto[^correcto].

<span class="progress-marker" id="s7">⸻ 7/8 ⸻</span>

El método ya tenía forma. Faltaba el nombre.

Durante un tiempo dudé del nombre. "Resonant Coding" suena pretencioso, lo sé. Hubo versiones alternativas: *Structured Prompting*, que era demasiado genérico; *Context-First Development*, que sonaba a consultora de management; "El Método del Balde", que era demasiado literal y además nadie iba a tomar en serio algo que se llama así[^nombres].

Pero seguía volviendo a la imagen de las ondas estacionarias. A la idea de que hay una frecuencia correcta esperando a ser encontrada. A la diferencia entre agitar la soga caóticamente y agitarla con precisión.

El *Vibe Coding* que se popularizó[^vibe] propone algo así como dejarse llevar, confiar en el modelo, iterar hasta que algo funcione. No digo que no sirva —hay situaciones donde esa aproximación es perfectamente válida— pero para trabajo serio, para sistemas que tienen que funcionar, para código que va a ser mantenido por otros humanos, necesitás algo más riguroso. Necesitás encontrar la resonancia[^resonancia].

<span class="progress-marker" id="s8">⸻ 8/8 ⸻</span>

Debería probablemente cerrar con alguna conclusión elegante pero la verdad es que no tengo una. Lo que tengo es un proceso que funciona mejor que no tener proceso, que se puede refinar, que genera artefactos reutilizables[^artefactos], que obliga a pensar antes de actuar. No es perfecto. Hay días donde todo falla igual. Hay modelos que se resisten a cooperar. Hay problemas que son genuinamente difíciles y ningún método los hace fáciles.

Pero cuando funciona —cuando el contexto está bien construido, cuando el plan está bien definido, cuando cada tarea cabe en su balde y el agua está limpia— hay un momento donde todo hace clic. Donde el modelo hace exactamente lo que necesitás que haga. Donde el código que genera es el código que habrías escrito vos, solo que más rápido y probablemente con menos errores. En esos momentos uno entiende, visceralmente, lo que significa encontrar la frecuencia correcta. Y después, invariablemente, llega el siguiente *pull request* incomprensible, y hay que empezar de nuevo.

Hay una pregunta que me persigue últimamente, una que no tiene respuesta fácil y que prefiero dejar resonando en vez de cerrar con una conclusión falsa: ¿qué pasa con los que vienen después? No hablo solo de los programadores —aunque también— sino de toda una generación que va a entrar al mercado laboral cuando estas herramientas sean ubicuas[^ubicuas]. Los call centers ya están desapareciendo. El otro día me llamó el banco y me atendió una voz que sonaba humana pero era un robot. La conversación fue más fluida que la mayoría de las que tuve con humanos en ese contexto[^callcenter]. Los trabajos de entrada, esos que servían para aprender el oficio equivocándose en cosas que no importaban demasiado, están evaporándose. Y mientras tanto seguimos formando gente como si el mundo de mañana fuera igual al de ayer. Pero no son solo los jóvenes los que sufren esta transición.

No hay nada más cercano a mi imagen personal del infierno que ir a un banco y esperar horas viendo jubilados pidiendo ayuda para entender cómo sacar su propio dinero. Alguien del banco —con esa cara de quien ya perdió toda esperanza— los guía hacia una pantalla que bien podría ser un cartel dibujado con crayones por lo bien que funciona. O les dicen que usen el celular, sabiendo que sus dedos no pueden pegarle a las letritas ni navegar las laberínticas aplicaciones donde para ver tu saldo tenés que ser Indiana Jones de la tecnología[^bancos]. Y acá hay algo que me da una pizca de optimismo: tal vez, solo tal vez, la IA pueda usarse para diseñar interfaces que contemplen a todo el mundo. Que se adapten. Que guíen. Que sean sencillas de verdad, no sencillas-para-el-que-las-diseñó.

Pero todo esto tiene un costo, y no hablo solo del costo humano[^costo]. Cada prompt, cada iteración, cada balde de agua limpia que usamos consume tokens, y los tokens cuestan dinero[^tokens]. Es fácil olvidarlo cuando la herramienta funciona bien, pero hay una economía nueva emergiendo acá, una donde el recurso escaso no es el tiempo de máquina sino la capacidad de contexto, y donde ser estratégico en cómo usás tus tokens puede ser la diferencia entre un proyecto viable y uno que se come el presupuesto antes de entregar nada.

¿Qué pasa cuando se acaban? ¿Cuando el modelo que usabas sube de precio o desaparece? ¿Qué habilidades estamos dejando de desarrollar porque es más fácil pedirle al modelo que las simule?[^habilidades] ¿Nos volvemos más eficientes o simplemente más dependientes?[^dependencia]

No tengo respuestas. Sospecho que nadie las tiene todavía. Pero me parece que estas son las preguntas que deberíamos estar haciéndonos ahora, mientras todavía hay tiempo de influir en cómo se responden.

---

Para una guía práctica del método, ver [Resonant Coding: Guía práctica](resonant-coding-guia.html).

---

## Notas

[^codigo-ajeno]: El código ajeno, como la letra de un médico, opera bajo la suposición implícita de que alguien en algún momento supo lo que significaba. Esta suposición es frecuentemente incorrecta.

[^paranoia]: La distinción entre paranoia y cautela razonable se ha vuelto borrosa en los últimos años. Tal vez siempre lo fue y solo ahora tenemos vocabulario para discutirlo. O tal vez la realidad se volvió suficientemente extraña como para que la paranoia sea la respuesta adaptativa correcta.

[^presion]: "Acelerar" es una de esas palabras que en contextos corporativos significa simultáneamente todo y nada. Puede significar "producir más" o "gastar menos" o "despedir gente" o "adoptar la tecnología de moda" o alguna combinación de las anteriores. En este caso significaba "usar IA para todo" sin mucha clarificación sobre qué era "todo" ni cómo se medía el éxito.

[^pr]: Un *pull request*, para los afortunados que no trabajan en software, es el mecanismo por el cual alguien propone cambios al código y otros los revisan antes de aceptarlos. En teoría es un proceso ordenado de validación colectiva. En la práctica es donde van a morir las relaciones interpersonales, las expectativas de horarios razonables, y cualquier ilusión de que la programación es una disciplina racional.

[^entender]: Hay un debate filosófico genuino sobre si los modelos de lenguaje "entienden" algo o simplemente procesan patrones estadísticos de una manera que simula entendimiento. Mi posición personal, que no voy a defender en detalle porque este ya es un texto largo, es que la pregunta está mal formulada: el "entendimiento" humano probablemente también es procesamiento de patrones, solo que en un sustrato diferente. Esto no resuelve nada pero al menos distribuye el misterio de forma más equitativa.

[^cursor]: Cursor es un editor de código —algo así como un Photoshop pero para programar— que integra modelos de lenguaje directamente en el flujo de trabajo. Es la herramienta que estábamos usando para todo.

[^arenas]: La sensación de construir sobre arenas movedizas no es exclusiva de trabajar con IA. Es, me atrevería a decir, la condición fundamental de cualquier trabajo técnico en el siglo XXI. Los frameworks cambian, los lenguajes evolucionan, las "mejores prácticas" de hace tres años son los antipatrones de hoy. La diferencia con la IA es la velocidad: lo que antes cambiaba en años ahora cambia en meses.

[^ondas-hermosas]: No voy a intentar explicar por qué las ondas son hermosas porque eso requeriría un ensayo separado sobre estética y física, y este texto ya tiene demasiadas digresiones. Pero confíen en mí: son hermosas. Busquen *standing waves* en YouTube y pierdan media hora. Vale la pena.

[^pozo]: El algoritmo de recomendaciones de YouTube es, en cierto sentido, el modelo de lenguaje original: una máquina de predicción optimizada para mantenerte mirando. A las tres de la mañana, cuando las defensas están bajas y la voluntad es un concepto abstracto, el algoritmo gana. Siempre gana.

[^estacion]: El video específico era de algo llamado "Estación de Ondas", una demostración de la Semana de la Física de la UBA. [Acá está](https://www.youtube.com/watch?v=6zBknO95rB4). No sé cómo llegué ahí desde lo que fuera que estaba viendo antes. Probablemente empecé con algo sobre cocina o música. Así funciona el pozo.

[^potencial]: Esta idea —que el desorden contiene orden latente— aparece en tantos contextos diferentes que probablemente sea una de esas verdades fundamentales sobre cómo funciona el universo, o al menos sobre cómo funciona nuestra percepción del universo. Desde la termodinámica hasta la teoría del caos, desde la cristalografía hasta la evolución biológica, hay estructuras emergiendo de lo que parece ruido. El truco es siempre encontrar las condiciones correctas para que la estructura se manifieste.

[^datos]: Según [información filtrada y luego confirmada por Microsoft](https://the-decoder.com/gpt-4-architecture-datasets-costs-and-more-leaked/), GPT-4 fue entrenado con aproximadamente 13 billones de tokens (trillions en inglés), lo que equivale a unos 10 billones de palabras. Para ponerlo en perspectiva: si leyeras un libro por día desde que nacés hasta que morís, no llegarías ni cerca. La [Biblioteca del Congreso de Estados Unidos](https://www.loc.gov/about/general-information/) tiene aproximadamente 25 millones de libros catalogados. Los modelos actuales han "leído" órdenes de magnitud más que eso. Lo que no significa que hayan entendido algo de lo que leyeron, pero ese es otro problema.

[^filosofo]: Los filósofos de la mente llevan décadas discutiendo qué significa "entender" y "ser consciente". No han llegado a ningún consenso. Lo que sí han establecido es que la pregunta es mucho más difícil de lo que parece, y que cualquiera que te dé una respuesta simple probablemente no haya pensado suficiente en el problema.

[^memoria]: La memoria prostética de los modelos de lenguaje tiene un límite duro: la ventana de contexto. Cuando la "conversación" acumulada supera ese límite, hay que recortar. Lo cual significa decidir qué partes de la memoria conservar y cuáles descartar. Hay sistemas sofisticados para hacer esto —resúmenes automáticos, vectorización semántica, bases de datos de embeddings— pero todos son aproximaciones. Algo siempre se pierde.

[^balde]: Esta metáfora me vino durante una conversación sobre camping. Estábamos discutiendo la logística de lavar platos en el campo y alguien mencionó que con agua limitada hay que ser estratégico: primero los vasos, después los platos, al final las ollas grasosas. Y de repente todo hizo clic. El contexto de un modelo de lenguaje funciona exactamente igual: hay que ser estratégico con qué le metés y en qué orden, porque una vez que el agua se ensucia no hay vuelta atrás.

[^atencion]: Este fenómeno está documentado en el paper ["Lost in the Middle: How Language Models Use Long Contexts"](https://arxiv.org/abs/2307.03172) de Liu et al. (2023). La versión corta es que los modelos prestan más atención al principio y al final del contexto, y tienden a "olvidar" lo que está en el medio. Esto tiene implicaciones prácticas obvias: si querés que el modelo preste atención a algo, ponelo al principio o al final, no en el medio.

[^dados]: La metáfora del dado es imperfecta porque los dados son uniformemente aleatorios, mientras que los modelos de lenguaje tienen distribuciones de probabilidad complejas y no uniformes. Pero captura la esencia: el resultado no está determinado de antemano, y el mismo input puede producir outputs diferentes.

[^yegge]: Steve Yegge trabajó en Amazon y Google, escribió algunos de los posts más influyentes (y polémicos) sobre cultura de ingeniería, y tiene la particularidad de combinar *insights* genuinamente brillantes con tomas tan calientes que generan *flame wars* de semanas. Su Regla de los 5 está enterrada en un [repositorio de GitHub](https://github.com/steveyegge/gastown/blob/main/internal/formula/formulas/rule-of-five.formula.toml) escrito para que lo lean máquinas, no personas.

[^context]: El documento de Context Engineering de Horthy está [disponible públicamente](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) y es probablemente la mejor introducción al tema que existe. Advertencia: es técnico, detallado, y si empezás a leerlo es difícil parar.

[^cinco]: Los cinco pasos —borrador, exactitud, claridad, casos límite, excelencia— no tienen que aplicarse siempre en ese orden ni siempre completamente. A veces un documento necesita más trabajo en claridad que en exactitud. A veces los casos límite son obvios y el esfuerzo tiene que ir en otra parte. El punto es tener una estructura de revisión, no seguirla ciegamente.

[^herencia]: El código heredado —*legacy code* en la jerga— es el eufemismo que usamos para referirnos al código que alguien escribió antes, que nadie entiende completamente, y que nadie se atreve a tocar por miedo a romper algo. Toda empresa de software suficientemente vieja tiene montañas de legacy code. Es como los estratos geológicos: podés ver la historia de la organización en las capas de decisiones técnicas cuestionables.

[^alucinaciones]: Las "alucinaciones" de los modelos de lenguaje —cuando generan información incorrecta con total confianza— son probablemente el problema más difícil de resolver porque son difíciles de detectar. Un error obvio salta a la vista. Una información sutilmente incorrecta puede pasar todos los controles y explotar meses después. Es como una bomba de tiempo semántica.

[^tarde]: Hay un dicho que circula en la comunidad de programación, de origen incierto: "Semanas de programación pueden ahorrarte horas de planificación." Es sarcástico, obviamente, pero captura una verdad profunda sobre cómo tendemos a subestimar la planificación y sobreestimar nuestra capacidad de arreglar las cosas sobre la marcha.

[^beads]: Yegge otra vez al ataque: [beads](https://github.com/steveyegge/beads) es un *issue tracker* pensado específicamente para agentes de IA. La idea es que las tareas tienen que ser lo suficientemente pequeñas y bien definidas como para que un agente pueda tomarlas y ejecutarlas sin intervención humana. Es la formalización de lo que describimos acá como "caber en un balde".

[^pensar]: La paradoja de usar IA para programar es que el trabajo que automatiza —escribir código— es relativamente fácil, mientras que el trabajo que no automatiza —decidir qué código escribir— es lo genuinamente difícil. Los modelos pueden generar implementaciones, pero no pueden generar requerimientos. Pueden escribir soluciones, pero no pueden entender problemas. Al menos no todavía. Aunque "todavía" es una palabra cada vez más cargada en este contexto.

[^barranco]: Esto no es una metáfora teórica. He visto proyectos donde la velocidad de generación de código superó la capacidad de revisión, y el resultado fue un sistema que nadie entendía, que nadie podía mantener, y que eventualmente tuvo que ser descartado y reescrito desde cero. La velocidad sin dirección es solo una forma más rápida de perderse. En un próximo post sobre lo que estoy llamando provisionalmente [Resonant Development](/es/resonant-development) quiero explorar cómo combinar estas ideas con *spec-driven development* para atacar exactamente este problema: cómo escalar la revisión cuando el código crece más rápido de lo que cualquier humano puede leer.

[^correcto]: "Correcto" es una palabra complicada en software. ¿Correcto según qué especificación? ¿Según qué casos de uso? ¿Correcto ahora o correcto cuando las condiciones cambien? El método que describo no resuelve estas ambigüedades, pero al menos las hace explícitas. Y explicitar las ambigüedades es el primer paso para resolverlas.

[^nombres]: El proceso de nombrar cosas es, según la [famosa cita de Phil Karlton](https://martinfowler.com/bliki/TwoHardThings.html) que circula desde los años 90, una de las dos cosas más difíciles en ciencias de la computación (la otra es invalidar cachés). Lo de los errores off-by-one es un agregado posterior de Leon Bambrick. Que sean tres cosas es parte del chiste.

[^vibe]: El término *Vibe Coding* fue acuñado por Andrej Karpathy en un tweet, pero el concepto fue desarrollado en profundidad en el libro [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/) de Steve Yegge y Gene Kim. Yo venía probando el *CHOP* (*Chat Oriented Programming*) desde que apareció el video de Steve un año antes, así que esperaba la salida del libro con ansiedad. El libro es excelente y vale la pena leerlo, aunque mi metodología va en una dirección ligeramente diferente.

[^resonancia]: Hay algo profundamente satisfactorio en la idea de que trabajar bien con una herramienta es encontrar su frecuencia de resonancia. Implica que la herramienta tiene una forma correcta de ser usada, que no es arbitraria, que puede ser descubierta. Es una visión optimista, tal vez ingenuamente optimista, pero es la que me permite seguir haciendo esto.

[^artefactos]: Los "artefactos" que genera el proceso —documentos de investigación, planes de acción, prompts refinados— tienen valor más allá de su uso inmediato. Pueden reutilizarse, adaptarse, servir de base para futuros proyectos. Es una forma de capital intelectual que se acumula. Esto es importante porque significa que el tiempo invertido no se pierde: se invierte. Mantengo una colección de estos prompts en [incitaciones](https://github.com/charly-vibes/incitaciones), por si a alguien le sirve como punto de partida.

[^ubicuas]: "Ubicuo" es una de esas palabras que suenan a jerga corporativa pero que no tienen buen reemplazo. Significa "que está en todas partes al mismo tiempo". Como el aire, o la ansiedad, o pronto los modelos de lenguaje.

[^callcenter]: Hay algo profundamente irónico en que los call centers —esos lugares que durante décadas fueron sinónimo de trabajo alienante, scripts robóticos leídos por humanos agotados, y esperas infinitas con música de ascensor— estén siendo reemplazados por robots que, en muchos casos, hacen el trabajo mejor. No sé si esto es progreso o simplemente un cambio de quién sufre. Probablemente ambas cosas.

[^bancos]: La experiencia bancaria para personas mayores es un caso de estudio en cómo no diseñar tecnología. Sistemas pensados por gente joven para gente joven, desplegados en contextos donde la mayoría de los usuarios tienen más de sesenta años, dedos que ya no responden como antes, y una relación con la tecnología que oscila entre la desconfianza y el terror. Cada cajero automático con interfaz confusa, cada app que requiere doce pasos para ver el saldo, cada empleado que responde "tiene que hacerlo por la app" es una pequeña crueldad sistémica.

[^costo]: El costo humano de la automatización es un tema que merece más espacio del que puedo darle acá. Hay libros enteros sobre esto. Mi posición personal, para lo que valga, es que la tecnología en sí no es buena ni mala —es una herramienta— pero las decisiones sobre cómo se implementa y quién se beneficia son profundamente políticas. Pretender que son puramente técnicas es una forma de evadir la responsabilidad.

[^tokens]: Para dar una idea concreta: en el momento de escribir esto, usar GPT-4 cuesta aproximadamente $30 por millón de tokens de entrada y $60 por millón de tokens de salida. Un token es aproximadamente tres cuartos de una palabra en inglés (en español la proporción es peor porque las palabras son más largas). Una sesión de trabajo intensiva puede consumir varios millones de tokens fácilmente. Claude, el modelo que usa la herramienta con la que escribí buena parte de este texto, tiene precios similares. Anthropic ofrece planes mensuales con límites de uso; cuando llegás al límite, o pagás más o esperás al mes siguiente. Es una economía nueva con reglas nuevas, y la mayoría de la gente la está navegando a ciegas.

[^habilidades]: Esta es la pregunta que más me inquieta. Hay habilidades que se desarrollan solo a través de la práctica repetida: la capacidad de leer código ajeno, de detectar patrones problemáticos, de anticipar cómo va a fallar algo antes de que falle. Si delegamos esa práctica al modelo, ¿qué pasa con nuestra capacidad de hacerla nosotros? No tengo una respuesta, pero sospecho que la respuesta correcta involucra usar las herramientas sin dejar de ejercitar los músculos que las herramientas podrían atrofiar.

[^dependencia]: Hay algo que bordea la adicción y que no sé si tiene nombre todavía. Me descubro pidiéndole cosas a los modelos todo el tiempo, porque *parecería* que dan resultado: que me expliquen cómo se relaciona el concepto de forma en Simondon con el de Gombrowicz, cómo saber si soy adicto a la IA, cómo hacer para dejar de trabajar estando en el sur del planeta, cómo estar más tranquilo, qué plantas plantar en el jardín que sean nativas, cómo conseguir clientes, cómo cambiar de trabajo, dónde aprender sobre crypto, qué actividad física hacer si no me gusta el ejercicio, cómo aprender a escribir, cómo hacer un post en LinkedIn, cómo renunciar, cómo gastar menos en tokens, cómo saber si estoy deprimido, cómo entender las leyes de sucesión, cómo entender a un bebé de un año, cómo replicar mi voz, cómo traducir un libro, de dónde viene mi apellido, cómo armar una SaaS, cómo trabajar menos, cuál es el ancho óptimo para una ducha, cómo dejar de pensar. Pregunta tras pregunta, token tras token, como quien fuma un cigarrillo más pensando que va a ser el último.

