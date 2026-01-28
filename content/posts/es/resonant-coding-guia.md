---
title: "Resonant Coding: Guía práctica"
date: 2026-01-25
lang: es
---

Todo lo anterior suena bien en teoría, pero la teoría tiene esa particularidad molesta de disolverse cuando toca la realidad. Así que acá va cómo se materializa esto en el día a día, con la advertencia de que cualquier sistema que pretenda ser definitivo está condenado a fracasar, y este no es la excepción[^sistema].

Este documento es una expansión del método de tres pasos —investigación, planificación, implementación— descrito en [Resonant Coding](resonant-coding.html), con las estructuras adicionales que fuimos descubriendo que necesitábamos a medida que lo aplicábamos en proyectos reales.

## Estructura de carpetas

La primera decisión fue estructural: si el contexto es un balde que se ensucia, entonces hay que tener baldes separados para cada tipo de agua. En la práctica esto se traduce en carpetas con funciones específicas[^carpetas]:

- `research/` para los documentos de investigación, nombrados con fecha para poder rastrear la evolución del entendimiento
- `plans/` para los planes de implementación, también fechados, también versionados
- `specs/` para las especificaciones formales en formato Gherkin[^gherkin], que funcionan como documentación viva y tests ejecutables al mismo tiempo
- `handoffs/` para los documentos de traspaso entre sesiones, porque el modelo no recuerda nada y alguien tiene que recordar por él

## Procedimiento

La segunda decisión fue procedimental: antes de escribir código, escribir un plan. Siempre. Sin excepciones. El plan divide el trabajo en fases que puedan completarse en un tiempo razonable, con criterios de éxito explícitos —automatizados cuando se puede, manuales cuando no queda otra. Cada fase es un balde limpio: el modelo recibe solo el plan de esa fase y la información relevante, nada más. Para tareas con riesgo arquitectónico, a veces usamos *tracer bullets*[^tracer].

## Memoria

La tercera decisión fue sobre la memoria. Los modelos no recuerdan, pero los archivos sí. Al final de cada sesión de trabajo —o cuando hay que pasar el contexto a otra persona, o a otro modelo, o a uno mismo del futuro— se genera un documento de *handoff* que captura el estado actual: qué se hizo, qué se aprendió, qué queda pendiente, qué archivos son relevantes. Es memoria prostética externalizada, y funciona mejor de lo que tiene derecho a funcionar[^handoff].

## Decisiones de diseño

Para las decisiones de diseño que no son obvias —cuando hay múltiples caminos posibles y elegir uno implica descartar otros— mantenemos una carpeta de `debates/` donde se documentan las opciones consideradas, los pros y contras de cada una, y la razón por la que se eligió lo que se eligió. Esto parece burocracia hasta que, seis meses después, alguien pregunta "¿por qué hicieron esto así?" y la respuesta está escrita en vez de perdida en la cabeza de alguien que ya no trabaja acá[^debates].

## Flujo típico

El flujo típico termina siendo algo así:

1. Llega un requerimiento. Antes de tocar código, se crea un documento de investigación. El modelo lee el código existente, la documentación, lo que haya, y genera un resumen del estado actual. Ese resumen pasa por la Regla de los 5 hasta que sea confiable.

2. Con el documento de investigación como input —y solo ese documento, en una conversación nueva, con el balde limpio—, se genera un plan. El plan divide el trabajo en fases, cada fase tiene criterios de éxito, cada tarea es lo suficientemente pequeña como para caber en un solo balde. El plan también pasa por la Regla de los 5.

3. Se implementa fase por fase, cada una en su propia conversación, cada una validada antes de pasar a la siguiente. Si algo no funciona, se ajusta el plan, no se improvisa.

4. Al final de la sesión, se genera el *handoff*. El próximo que retome el trabajo —sea humano o modelo— tiene todo el contexto que necesita.

Hay una tentación constante de saltarse pasos, de ir directo al código porque "esto es simple" o "ya sé cómo hacerlo". A veces funciona. Más seguido de lo que me gustaría admitir, no funciona, y el tiempo que ahorraste salteando pasos lo perdés multiplicado arreglando lo que salió mal. El método es más lento al principio y más rápido al final. La pregunta es si tenés la paciencia para llegar al final[^paciencia].

---

## Notas

[^sistema]: Todo sistema de trabajo es una hipótesis sobre cómo funciona el mundo. Como toda hipótesis, debería estar sujeta a revisión cuando la evidencia lo contradice. El problema es que los humanos nos encariñamos con nuestros sistemas y los defendemos más allá de lo razonable. Intento recordarme esto regularmente. No siempre lo logro.

[^carpetas]: La estructura de carpetas parece un detalle menor hasta que tenés que buscar algo que escribiste hace tres meses y no lo encontrás. Nombrar las cosas con fechas en formato `YYYY-MM-DD` al principio del nombre tiene la ventaja de que se ordenan cronológicamente de forma automática, lo cual suena trivial hasta que te salva veinte minutos de búsqueda.

[^gherkin]: Gherkin es un formato para escribir especificaciones en lenguaje casi-natural que pueden ejecutarse como tests. La estructura es *Given-When-Then* (Dado-Cuando-Entonces) y obliga a pensar en términos de comportamiento observable en vez de implementación interna. Es uno de esos casos donde la restricción del formato mejora la calidad del pensamiento. Hay un insight de [Dex Horthy](https://www.youtube.com/watch?v=42AzKZRNhsk) que me parece fundamental: ahora que la mayor parte de nuestro trabajo es revisar lo que genera la IA en vez de escribir desde cero, necesitamos herramientas para *editar* —dejar comentarios, tachar, marcar como poco claro— en vez de herramientas para *escribir*. De esa frustración nació [fabbro](https://github.com/charly-vibes/fabbro), una herramienta que estoy desarrollando para anotar código y estructurar el feedback hacia los modelos. Para probar *spec-driven development* le pedí a la IA que describiera sus funcionalidades siguiendo el formato Gherkin, y terminé creando [nayra](https://github.com/charly-vibes/nayra) —un proyecto que siempre quise tener— específicamente para explorar herramientas más formales como [OpenSpec](https://github.com/humanlayer/openspec).

[^tracer]: El término *tracer bullet* viene de la balística: las balas trazadoras dejan un rastro visible que permite ajustar la puntería en tiempo real. En desarrollo, un *tracer bullet* es una implementación mínima que atraviesa todas las capas del sistema para verificar que la arquitectura funciona antes de invertir en construirla bien. La idea viene del libro *The Pragmatic Programmer* de Hunt y Thomas. Para tareas con riesgo arquitectónico —esas donde no sabés si la solución va a funcionar hasta que la probás— es más barato descubrir que tu arquitectura no funciona cuando tenés cien líneas de código que cuando tenés diez mil.

[^handoff]: El documento de handoff es, en cierto sentido, una carta que te escribís a vos mismo del futuro. O a otra persona. O a un modelo que va a retomar tu trabajo. La clave es incluir no solo qué hiciste sino qué aprendiste: los callejones sin salida que exploraste, las decisiones que tomaste, las cosas que te sorprendieron. El contexto que parece obvio hoy va a ser completamente opaco dentro de dos semanas.

[^debates]: Documentar decisiones de diseño es una de esas prácticas que todos saben que deberían hacer y casi nadie hace. La razón usual es que "no hay tiempo". La ironía es que el tiempo que no invertís documentando lo gastás multiplicado seis meses después tratando de reconstruir el razonamiento desde cero.

[^paciencia]: La paciencia es, probablemente, la habilidad más subestimada en desarrollo de software. No la paciencia pasiva de esperar que las cosas pasen, sino la paciencia activa de hacer las cosas bien aunque tome más tiempo. Es difícil porque todo conspira en contra: los deadlines, la presión, la ilusión de que "esta vez va a salir bien" aunque las últimas diez veces no salió. El método no te da paciencia, pero al menos te da una estructura donde la paciencia tiene sentido. Para practicar sin la presión de un proyecto real, empecé [jams](https://github.com/charly-vibes/jams): aplicaciones web simples y autocontenidas, perfectas para probar el flujo completo sin arriesgar nada importante.
