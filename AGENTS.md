# Contexto del Repositorio

Este es un repositorio para un blog estático que transforma Markdown a HTML.

## Estructura

```
.
├── content/
│   └── posts/          # Posts en Markdown
├── templates/          # Plantillas HTML
│   ├── post.html       # Plantilla para posts individuales
│   ├── index.html      # Plantilla para el índice
│   ├── metadata.yaml   # Metadatos globales del sitio
│   └── assets/         # CSS y recursos estáticos
├── public/             # Salida generada (no commitear)
├── scripts/
│   └── build.sh        # Script de build
├── .agents/
│   ├── commands/       # Comandos para agentes
│   └── personalidad.md # Estilo de escritura (NO PUBLICAR)
└── .github/
    └── workflows/      # GitHub Actions
```

## Build System

El blog usa `pandoc` para convertir Markdown a HTML. Los comandos principales están en el `justfile`:

- `just build` - Genera el sitio completo
- `just clean` - Limpia archivos generados
- `just serve` - Servidor local de desarrollo
- `just new <slug>` - Crea un nuevo post

## Formato de Posts

Los posts deben estar en `content/posts/` con formato:

```markdown
---
title: "Título del Post"
date: YYYY-MM-DD
---

# Título

Contenido en Markdown...
```

## Comandos Disponibles

Los comandos para agentes están en `.agents/commands/` (symlinked a `.claude/commands/`):

- `/nuevo-post [tema]` - Crear un nuevo post
- `/revisar-post <archivo>` - Revisar un post existente
- `/actualizar-post <archivo>` - Actualizar un post

## Guía de Estilo

Ver `.agents/personalidad.md` para las guías de estilo y tono de escritura.

**IMPORTANTE**: El archivo `.agents/personalidad.md` contiene instrucciones privadas sobre el estilo de escritura y NO debe ser publicado ni incluido en el sitio generado.

## CI/CD

El sitio se despliega automáticamente a GitHub Pages cuando se hace push a `main`.
