---
title: "Walk this WAI: El origen"
date: 2026-03-02
lang: es
translations:
  en: /en/posts/the-origin-of-wai.html
---

# Walk this WAI: El origen

Este va a ser un post un poco más didáctico y explicativo, y quizá no tan experimental, pero eso no quita que no vaya a ser entretenido. La idea principal es contarles mi visión luego de estar experimentando por varios meses con IA, exprimiéndola al máximo para entender cómo sacarle provecho a algo que todavía no terminamos de comprender del todo. Y lo hago por una razón fundamental: no me gusta programar. Lo vengo diciendo [públicamente desde hace años](https://youtu.be/ioeMeQNEgL8?si=4b66Jm53aEtlQMfr&t=99), pero sigue siendo una herramienta esencial para lo que realmente me apasiona: resolver problemas.

¿Por qué no me gusta programar o codificar? Primero, porque soy lento escribiendo. Con el tiempo fui mejorando, pero mis manos siguen siendo muy lentas para la velocidad a la que va mi cabeza. Segundo, porque no tengo formación formal en sistemas, lo cual hace que todo parezca siempre demasiado complicado. Eso no quita que no sepa cosas: leí decenas de libros, vi centenares de charlas, [miles de artículos](https://ak.saxa.xyz/hipervinculos/), cursos... Pero esa falta de formación terminó siendo una ventaja, porque me permitió cuestionar cada gesto del proceso y buscar la manera de garantizar que las cosas funcionen. Algo que aprendí en todo este tiempo es que el mayor problema de los sistemas no son los sistemas, sino las personas, y lo mejor es siempre tratar de eliminarlas de los procesos[^humanos].

A medida que el costo de generar software se desploma, el verdadero desafío deja de ser la escritura del código y pasa a ser la **intencionalidad**. Geoff Huntley lo explica muy bien en su nota [The Burrowing](https://ghuntley.com/real/): la IA no solo está tocando nuestra puerta, está cavando por debajo de nuestros cimientos. Si no marcamos un camino claro de cómo trabajar ahora, corremos el riesgo de dejar a toda una generación de personas con menos experiencia sin un mapa para navegar este nuevo mundo donde las habilidades técnicas tradicionales se están comoditizando a una velocidad absurda. ¿Cómo formamos a alguien cuando el "picar código" ya no es la puerta de entrada?

## La Regla del Tres y el camino de menor esfuerzo

Cuando digo que hay que eliminar a las personas de los procesos, me refiero a quitar de en medio la posibilidad de que nos equivoquemos. Y para eso, terminé definiendo una regla que me ayuda a priorizar qué cosas hacer: la Regla del Tres. Si algo ocurre tres veces, deja de ser una anomalía estadística. Es una señal de que el sistema te está pidiendo a gritos que lo automatices para que no tengas que volver a pensar en ello nunca más.

El ejemplo más claro está en esas tareas repetitivas que hacemos mil veces por semana[^just]. ¿Cuántas veces nos hemos equivocado en un proceso de varios pasos solo por un simple olvido? ¿O peor aún: tener un manual de instrucciones que se desactualiza a los dos días? Para evitar eso, la mejor práctica es que la instrucción sea el comando mismo. Si el camino correcto es el más fácil de seguir, entonces se convierte en la norma. Es una forma de blindar el sistema contra nuestras propias limitaciones y garantizar que el orden de los pasos no dependa de nuestra memoria o de la paciencia de ese día.

## El quiebre: El grifo abierto

Esta misma obsesión por automatizar lo repetitivo fue la que me llevó a mi siguiente gran quiebre personal: la IA. Llegó como un autocompletado mágico que prometía mucho, y tuve la ventaja de vivirlo en un contexto donde no teníamos límites en lo que podíamos consumir. Estaba en un proyecto nuevo que me obligaba a aprender varios lenguajes y herramientas internas al mismo tiempo[^tech]. Al principio fue abrumador. Como líder del equipo, mi tarea era ver qué era posible y dónde estaban los puntos donde la herramienta fallaba o se volvía peligrosa; me sentía como alguien con un machete abriendo camino hacia algún lado.

Y había una única manera de hacerlo. Como proponen Steve Yegge y Gene Kim en su libro *Vibe Coding*: **Embrace the AI and stop looking at the code.**[^vibecoding]

Fue una decisión evaluada, no un capricho. El código, en realidad, no es el producto en sí (podemos programar en cualquier lenguaje), lo que realmente importa es que la funcionalidad sea la correcta. La imagen que me vino a la cabeza es esta: si queremos construir productos de calidad, ya sean vasos de plástico o un auto de F1, necesitamos una infraestructura que nos permita hacerlo con la mejor calidad posible. Con la programación siempre podemos mejorar la fábrica con la que construimos el producto en sí, y eso es una ventaja enorme cuando sabemos que podemos hacerlo. Como dije antes: no me gusta programar, me gusta crear cosas y resolver problemas. Y al igual que los monos que usan palitos para comer hormigas[^monos], nosotros podemos crear programas para mejorar nuestros productos.

## El Laboratorio: De Jams a Fabbro

Con esta idea de la fábrica en mente, empecé a experimentar qué tan lejos podía llegar[^tools]. El navegador es la interfaz universal para casi todo[^talk], así que siguiendo los pasos de Simon Willison, creé pequeñas herramientas que cabían en una sola página: las **Jams**[^jams]. Empecé con un limpiador de direcciones web y terminé con una aplicación que registraba el acelerómetro del celular en tiempo real. La premisa no era ver la calidad de lo que estaba haciendo, sino ver cómo podía crear funciones y cuánto tiempo me tomaba.

Pero crear funciones rápido tiene un costo: el tiempo de revisión. El desafío apareció cuando intentaba aceptar lo que la IA me proponía sin poder revisarlo de forma sencilla. Cuando me generaba un archivo enorme con mil cosas para mirar, ¿dónde diablos le ponía los comentarios?

Así nació **Fabbro**[^fabbro], una herramienta que me permite poner notas sobre el código igual que lo hacemos en Google Docs. Con ella empecé a probar una forma de trabajar guiada por especificaciones[^sdd]: yo definía qué tenía que hacer el programa en documentos simples y la IA se encargaba de implementarlo. Lo mejor de todo es que podía probar la misma herramienta mientras la construía, definiendo sus propias reglas. Resolví un problema concreto: poder dejarle feedback a la máquina desde cualquier lugar, con precisión quirúrgica, sin perderme en el código.

## Nayra y la autonomía

Con un sistema de revisión en marcha, empecé a confiar en la autonomía de la IA. Ya no solo le pedía trozos de código; empecé a organizarle las tareas por tickets[^beads] para que ella misma gestionara qué hacer y yo solo tuviera que supervisar. Ya sabiendo que con esta metodología podía generar cosas complejas en lenguajes que casi no conocía, me animé a ir por más.

Así nació **Nayra**[^nayra], un visualizador de eventos en una línea de tiempo. Siempre quise contrastar eventos (¿qué músicos existían cuando Einstein era chico?), pero nunca tuve las ganas de sentarme a escribir el JavaScript necesario. Esta vez solo necesité charlar bastante con la máquina para ir estructurando el problema y definir qué funcionalidades quería. El resultado fue más allá de mi idea inicial: de un simple comparador de músicos, terminó mapeando tiempos del universo y un millón de detalles más, inspirado en un video de Kurzgesagt[^kurz] que me fascinaba desde hacía años.

## El nacimiento de WAI

Pero con cada nuevo proyecto aparecía la misma tarea tediosa de configurar todo desde cero[^setup]. Tenía que andar unificando las "habilidades" de cada herramienta —porque cada una quiere sus propios archivos de configuración— y el proceso se volvía repetitivo. Además, me pasaba que a mitad de semana me quedaba sin créditos en todas partes; tenía que esperar al siguiente período o seguir cargando más dinero... Ya me tenían enganchado.

Por eso creé **WAI**[^wai], una herramienta para que el proceso de desarrollo sea más predecible. La idea principal era estandarizar todas las prácticas que fui aprendiendo en estos años en algo que fuera \"AI-first\". No es para que uno la use directamente, sino para que la IA la utilice siguiendo mis reglas. Empecé a explorar lo que llamo **AIX** (experiencia de la IA): consultarle constantemente qué le parece poco intuitivo o qué necesita para trabajar mejor en otros proyectos.

Incluso empecé a organizar toda la información siguiendo un método de gestión de conocimiento[^para] para ver si era efectivo para la IA. Con el tiempo, agregué un subcomando llamado `way` para verificar que el repositorio tenga configuradas buenas prácticas de \"presión interna\"[^pressure], enfocándome siempre en crear la infraestructura necesaria para generar calidad.

## Reflejar y construir

Uno de los comandos que más uso en WAI es `reflect`[^reflect]. Le pide a la IA que analice nuestras conversaciones anteriores para detectar patrones, vicios o detalles del proyecto que pueden facilitar las tareas futuras. Es como tener una memoria colectiva que no falla. De WAI nunca vi una línea de código; está implementada en un lenguaje del que no sé nada[^rust], pero funciona y es estable en todas las plataformas.

Con todas estas herramientas y la experiencia acumulada, me animé a un proyecto más difícil: **Fotos**[^fotos]. Quería una aplicación para sacar capturas de pantalla y anotarlas, pero con superpoderes: reconocimiento de texto e integración con IA para anotaciones automáticas. En mi sistema operativo no existía nada parecido. En una sola tarde, dándole feedback constante a la máquina, resolví problemas de compilación y empaquetado que me hubiesen costado muchísimo resolver, y terminé instalando la aplicación en mi propia computadora.

Hoy, mi estrategia de consumo se estabilizó en el plan Pro de 100 USD. Es lo más efectivo en precio y calidad. Todavía no llegué a consumir todo el presupuesto semanal y cada vez tengo más procesos ejecutándose de manera autónoma. Al final, se trata de subir el nivel de abstracción: dejar de preocuparnos por cómo se escribe el código para enfocarnos en cómo estructurar las ideas. Es lo que llamo **Resonant Coding**. 

El código ha dejado de ser el fin para volver a ser lo que siempre debió ser: el medio para resolver problemas. Pero hay un peligro latente, lo que Steve Yegge llama el *AI Vampire*[^vampire]: la tentación de usar esa productividad extra para producir diez veces más cosas mediocres y terminar agotados. Ahora que podemos generar funcionalidad en mucho menos tiempo, el verdadero valor está en capturar ese tiempo para nosotros. En lugar de correr más rápido, podemos dedicarnos a construir cosas de mejor calidad y, sobre todo, dedicar más tiempo a pensar. Porque al final del día, la IA puede ejecutar a toda velocidad, pero la dirección y el sentido siguen siendo humanos.

---

[^humanos]: Eliminar a las personas de los procesos no es odio, es pragmatismo. La gente olvida, se cansa, se equivoca. El código automatizado no.

[^just]: El uso de herramientas como [just](https://just.systems/) permite codificar estas recetas. Algunas de las buenas prácticas que aplico incluyen: flujos de trabajo automatizados, configuración viva de ambientes, chequeos de salud (doctor) y procesos complejos multi-paso.

[^tech]: En ese momento me tocó aprender Go, TypeScript, BigQuery y todas las reglas internas de la compañía de manera acelerada. La IA fue el catalizador para que eso fuera posible.

[^vibecoding]: *Vibe Coding*, de Steve Yegge y Gene Kim (IT Revolution Press, 2025). La frase original es "Abraza la IA y deja de mirar el código". Es un cambio de paradigma donde el programador se convierte en un director de orquesta que supervisa la intención en lugar de cada línea de código.

[^monos]: La analogía del palito y la hormiga: somos animales de herramientas. La IA es simplemente el palito más largo y refinado que hemos encontrado hasta ahora.

[^tools]: En el trabajo usábamos Cursor pero no teníamos Claude Code, así que contraté la versión Pro por mi cuenta. Aproveché para usar Gemini CLI y ampcode (aprovechando una oferta de crédito gratuito).

[^talk]: Me refiero a *The Birth and Death of JavaScript* de Gary Bernhardt. Una joya.

[^jams]: [Jams](https://charly-vibes.github.io/jams/): aplicaciones que viven en una sola página inspiradas en Simon Willison.

[^fabbro]: [Fabbro](https://charly-vibes.github.io/fabbro/): Una interfaz de terminal (TUI) para comentar código que ahora también cuenta con una [versión web](https://charly-vibes.github.io/fabbro-web/). 

[^sdd]: Conocido como *Spec Driven Development* (SDD). En este caso, usaba archivos en formato Gherkin dentro de una carpeta de especificaciones para que la IA tuviera una guía clara de la funcionalidad esperada.

[^beads]: Hecho a través de un sistema de tickets para que la IA sepa exactamente en qué trabajar en cada momento sin perder el contexto.

[^nayra]: [Nayra](https://charly-vibes.github.io/nayra/): Un visualizador de eventos históricos y cronologías en una línea temporal que utiliza OpenSpec.

[^kurz]: [The History of the Entire World](https://www.youtube.com/watch?v=dGiQaabX3_o), un video de Kurzgesagt que muestra la inmensidad del tiempo. 

[^setup]: Hablo de configurar herramientas como beads, openspec y archivos específicos como AGENTS.md, CLAUDE.md o carpetas como .claude, .amp y .gemini.

[^wai]: WAI: Un CLI (interfaz de línea de comandos) agnóstico y simple que intenta ser el puente entre el humano y la máquina.

[^para]: El [Método PARA](https://fortelabs.com/blog/para/): Proyectos, Áreas, Recursos y Archivos, de Tiago Forte. 

[^pressure]: [BackPressure](https://ghuntley.com/pressure/), un concepto de Geoff Huntley sobre la infraestructura y la calidad del software.

[^reflect]: Comando que codifica las prácticas de años y guía a la IA para que las siga sin que yo tenga que recordarlas todas.

[^rust]: WAI está escrita en Rust, un lenguaje conocido por su rendimiento y seguridad, pero cuya sintaxis nunca tuve el tiempo (ni las ganas) de aprender.

[^fotos]: [Fotos](https://github.com/charly-vibes/fotos): Mi herramienta diaria para capturar y procesar información visual con la ayuda de agentes.

[^vampire]: [The AI Vampire](https://steve-yegge.medium.com/the-ai-vampire-eda6e4f07163), de Steve Yegge. Una advertencia sobre cómo usar el tiempo ganado para pensar en lugar de solo producir más.
