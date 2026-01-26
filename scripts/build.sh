#!/usr/bin/env bash
set -euo pipefail

CONTENT_DIR="${CONTENT_DIR:-content/posts}"
OUTPUT_DIR="${OUTPUT_DIR:-public}"
TEMPLATE_DIR="${TEMPLATE_DIR:-templates}"
BASE_PATH="${BASE_PATH-/microdancing}"
LANGUAGES=("es" "en")

build_post() {
    local input_file="$1"
    local lang="$2"
    local filename=$(basename "$input_file" .md)
    local output_file="${OUTPUT_DIR}/${lang}/posts/${filename}.html"

    mkdir -p "${OUTPUT_DIR}/${lang}/posts"

    pandoc "$input_file" \
        --standalone \
        --template="${TEMPLATE_DIR}/post.html" \
        --metadata-file="${TEMPLATE_DIR}/metadata-${lang}.yaml" \
        -V base-path="$BASE_PATH" \
        -o "$output_file"

    echo "Built: $output_file"
}

build_index() {
    local lang="$1"
    local posts_html=""
    local content_lang_dir="${CONTENT_DIR}/${lang}"

    for post in "${content_lang_dir}"/*.md; do
        [ -f "$post" ] || continue
        local filename
        filename="$(basename "$post" .md)"

        local title
        title=$(grep -m1 '^title:' "$post" | sed 's/^title: *["'\'']\{0,1\}\([^"'\'']*\)["'\'']\{0,1\} *$/\1/' || true)
        if [ -z "$title" ]; then
            title=$(grep -m1 '^# ' "$post" | sed 's/^# //' || true)
        fi
        if [ -z "$title" ]; then
            title="$filename"
        fi

        local date
        date=$(grep -m1 '^date:' "$post" | sed 's/^date: *["'\'']\{0,1\}\([^"'\'']*\)["'\'']\{0,1\} *$/\1/' || true)

        local summary
        summary=$(awk '
            BEGIN { state=0 }
            /^---$/ { if(state==0){state=1} else if(state==1){state=2}; next }
            state < 2 { next }
            /^[[:space:]]*$/ { next }
            /^[[:space:]]*#/ { next }
            {
                print;
                exit;
            }
        ' "$post" | sed 's/<[^>]*>//g' | awk '{for(i=1;i<=30;i++) printf "%s ", $i; print ""}')

        title="${title//&/&amp;}"
        title="${title//</&lt;}"
        title="${title//>/&gt;}"
        summary="${summary//&/&amp;}"
        summary="${summary//</&lt;}"
        summary="${summary//>/&gt;}"

        posts_html+="<li class=\"post-card\"><a href=\"posts/${filename}.html\">"
        posts_html+="<h2>${title}</h2>"
        [ -n "$date" ] && posts_html+="<p class=\"date\">${date}</p>"
        if [ -n "$summary" ]; then
            posts_html+="<p>${summary}...</p>"
        fi
        posts_html+="</a></li>
"
    done

    # Load nav labels from metadata
    local nav_home nav_about
    nav_home=$(grep -m1 '^nav-home:' "${TEMPLATE_DIR}/metadata-${lang}.yaml" | sed 's/^nav-home: *["'\'']\{0,1\}\([^"'\'']*\)["'\'']\{0,1\} *$/\1/' || echo "Home")

    mkdir -p "${OUTPUT_DIR}/${lang}"
    awk -v posts="$posts_html" -v lang="$lang" -v nav_home="$nav_home" -v base_path="$BASE_PATH" '{
        gsub(/\{\{posts\}\}/, posts)
        gsub(/\{\{lang\}\}/, lang)
        gsub(/\{\{nav-home\}\}/, nav_home)
        gsub(/\{\{base-path\}\}/, base_path)
        print
    }' "${TEMPLATE_DIR}/index.html" > "${OUTPUT_DIR}/${lang}/index.html"

    echo "Built: ${OUTPUT_DIR}/${lang}/index.html"
}

copy_assets() {
    if [ -d "${TEMPLATE_DIR}/assets" ]; then
        cp -r "${TEMPLATE_DIR}/assets" "${OUTPUT_DIR}/"
        echo "Copied assets"
    fi
}

build_redirect() {
    sed "s|{{base-path}}|${BASE_PATH}|g" "${TEMPLATE_DIR}/redirect.html" > "${OUTPUT_DIR}/index.html"
    echo "Built: ${OUTPUT_DIR}/index.html (redirect)"
}

clean() {
    rm -rf "${OUTPUT_DIR}"
    echo "Cleaned ${OUTPUT_DIR}"
}

build_all() {
    mkdir -p "${OUTPUT_DIR}"

    for lang in "${LANGUAGES[@]}"; do
        local content_lang_dir="${CONTENT_DIR}/${lang}"
        [ -d "$content_lang_dir" ] || continue

        for post in "${content_lang_dir}"/*.md; do
            [ -f "$post" ] || continue
            build_post "$post" "$lang"
        done

        build_index "$lang"
    done

    copy_assets
    build_redirect
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
        build_post "$2" "$3"
        ;;
    index)
        build_index "$2"
        ;;
    *)
        echo "Usage: $0 {build|clean|post <file> <lang>|index <lang>}"
        exit 1
        ;;
esac
