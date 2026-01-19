# Revisar Post

Revisa un post existente para mejorar su calidad.

## Instrucciones

1. Lee el archivo `.agents/personalidad.md` para entender el estilo y tono esperado
2. Lee el post especificado en $ARGUMENTS o lista los posts disponibles si no se especifica
3. Analiza el post considerando:
   - Claridad y coherencia
   - Gramática y ortografía
   - Consistencia con el estilo definido en `.agents/personalidad.md`
   - Estructura y formato Markdown
   - SEO básico (título, encabezados)
4. Presenta un resumen de sugerencias al usuario
5. Pregunta si desea aplicar las correcciones automáticamente
6. Si el usuario acepta, aplica las correcciones manteniendo la voz del autor

## Argumentos

$ARGUMENTS - Nombre del archivo del post a revisar (ej: `mi-post.md`)

## Ejemplo

```
/revisar-post ejemplo.md
```
