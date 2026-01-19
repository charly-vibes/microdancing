# Blog justfile - comandos iguales para CI y local

set shell := ["bash", "-euo", "pipefail", "-c"]

# Directorios
content_dir := "content/posts"
output_dir := "public"
template_dir := "templates"

# Comando por defecto
default: build

# Construir el sitio completo
build:
    ./scripts/build.sh build

# Limpiar archivos generados
clean:
    ./scripts/build.sh clean

# Construir un post específico
build-post file:
    ./scripts/build.sh post {{file}}

# Regenerar solo el índice
build-index:
    ./scripts/build.sh index

# Servidor local de desarrollo (requiere python)
serve: build
    @echo "Sirviendo en http://localhost:8000"
    python3 -m http.server 8000 --directory {{output_dir}}

# Crear un nuevo post
new slug:
    #!/usr/bin/env bash
    set -euo pipefail
    post_date=$(date +%Y-%m-%d)
    file="{{content_dir}}/{{slug}}.md"
    if [ -f "$file" ]; then
        echo "Error: $file ya existe"
        exit 1
    fi
    printf '%s\n' "---" "title: \"{{slug}}\"" "date: $post_date" "---" "" "# {{slug}}" "" > "$file"
    echo "Creado: $file"

# Listar todos los posts
list:
    @ls -1 {{content_dir}}/*.md 2>/dev/null || echo "No hay posts"

# Watch y rebuild (requiere entr)
watch:
    @echo "Observando cambios en {{content_dir}}..."
    find {{content_dir}} {{template_dir}} -type f | entr -c just build

# Verificar que pandoc está instalado
check-deps:
    @command -v pandoc >/dev/null 2>&1 || { echo "Error: pandoc no instalado"; exit 1; }
    @echo "Dependencias OK"

# Build para CI (con verificación de dependencias)
ci: check-deps build
    @echo "Build CI completado"

# Previsualizar un post específico en el navegador
preview file: build
    @xdg-open {{output_dir}}/posts/$(basename {{file}} .md).html 2>/dev/null || \
     open {{output_dir}}/posts/$(basename {{file}} .md).html 2>/dev/null || \
     echo "Abre manualmente: {{output_dir}}/posts/$(basename {{file}} .md).html"
