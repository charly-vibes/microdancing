#!/usr/bin/env bash
set -euo pipefail

CONTENT_DIR="${CONTENT_DIR:-content/posts}"
OUTPUT_DIR="${OUTPUT_DIR:-public}"
TEMPLATE_DIR="${TEMPLATE_DIR:-templates}"

build_post() {
    local input_file="$1"
    local filename=$(basename "$input_file" .md)
    local output_file="${OUTPUT_DIR}/posts/${filename}.html"

    mkdir -p "${OUTPUT_DIR}/posts"

    pandoc "$input_file" \
        --standalone \
        --template="${TEMPLATE_DIR}/post.html" \
        --metadata-file="${TEMPLATE_DIR}/metadata.yaml" \
        -o "$output_file"

    echo "Built: $output_file"
}

build_index() {
    local posts_html=""

    for post in "${CONTENT_DIR}"/*.md; do
        [ -f "$post" ] || continue
        local filename
        filename="$(basename "$post" .md)"

        # Extract title from frontmatter (handles quotes), fallback to heading, then filename
        local title
        title=$(grep -m1 '^title:' "$post" | sed 's/^title: *["'\'']\{0,1\}\([^"'\'']*\)["'\'']\{0,1\} *$/\1/' || true)
        if [ -z "$title" ]; then
            title=$(grep -m1 '^# ' "$post" | sed 's/^# //' || true)
        fi
        if [ -z "$title" ]; then
            title="$filename"
        fi

        # Extract date from frontmatter (handles quotes)
        local date
        date=$(grep -m1 '^date:' "$post" | sed 's/^date: *["'\'']\{0,1\}\([^"'\'']*\)["'\'']\{0,1\} *$/\1/' || true)

        # Escape HTML special characters in title
        title="${title//&/&amp;}"
        title="${title//</&lt;}"
        title="${title//>/&gt;}"

        posts_html+="<li><a href=\"posts/${filename}.html\">${title}</a>"
        [ -n "$date" ] && posts_html+=" <span class=\"date\">${date}</span>"
        posts_html+="</li>
"
    done

    # Use awk instead of sed to avoid issues with special characters and newlines
    awk -v posts="$posts_html" '{gsub(/\{\{posts\}\}/, posts); print}' \
        "${TEMPLATE_DIR}/index.html" > "${OUTPUT_DIR}/index.html"
    echo "Built: ${OUTPUT_DIR}/index.html"
}

copy_assets() {
    if [ -d "${TEMPLATE_DIR}/assets" ]; then
        cp -r "${TEMPLATE_DIR}/assets" "${OUTPUT_DIR}/"
        echo "Copied assets"
    fi
}

clean() {
    rm -rf "${OUTPUT_DIR}"
    echo "Cleaned ${OUTPUT_DIR}"
}

build_all() {
    mkdir -p "${OUTPUT_DIR}"

    for post in "${CONTENT_DIR}"/*.md; do
        [ -f "$post" ] || continue
        build_post "$post"
    done

    build_index
    copy_assets
    echo "Build complete!"
}

case "${1:-build}" in
    build)
        build_all
        ;;
    clean)
        clean
        ;;
    post)
        build_post "$2"
        ;;
    index)
        build_index
        ;;
    *)
        echo "Usage: $0 {build|clean|post <file>|index}"
        exit 1
        ;;
esac
