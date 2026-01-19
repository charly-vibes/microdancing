# Nuevo Post

Crea un nuevo post para el blog.

## Instrucciones

1. Lee el archivo `.agents/personalidad.md` para entender el estilo y tono de escritura
2. Pregunta al usuario sobre el tema del post si no se especifica en $ARGUMENTS
3. Crea un archivo en `content/posts/` con el formato `slug-del-post.md`
4. El archivo debe incluir frontmatter YAML con:
   - `title`: Título del post
   - `date`: Fecha actual (YYYY-MM-DD)
5. Escribe el contenido siguiendo las guías de estilo en `.agents/personalidad.md`
6. Usa el comando `just build` para verificar que el post se genera correctamente

## Formato del archivo

```markdown
---
title: "Título del Post"
date: YYYY-MM-DD
---

# Título del Post

Contenido...
```

## Argumentos

$ARGUMENTS - Tema o título del post (opcional)
