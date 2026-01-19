# Actualizar Post

Actualiza un post existente con nuevo contenido o correcciones.

## Instrucciones

1. Lee el archivo `.agents/personalidad.md` para mantener consistencia de estilo
2. Lee el post especificado en $ARGUMENTS
3. Pregunta al usuario qué cambios desea realizar:
   - Agregar nueva sección
   - Modificar contenido existente
   - Actualizar información desactualizada
   - Corregir errores
4. Realiza los cambios manteniendo:
   - El estilo original del post
   - La coherencia con `.agents/personalidad.md`
   - El formato Markdown correcto
5. Muestra un diff de los cambios antes de aplicarlos
6. Ejecuta `just build` para verificar que el post actualizado se genera correctamente

## Argumentos

$ARGUMENTS - Nombre del archivo del post a actualizar (ej: `mi-post.md`)

## Ejemplo

```
/actualizar-post ejemplo.md
```
