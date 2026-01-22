#!/usr/bin/env bash

file_path="$1"

if [[ -z "$file_path" ]]; then
  printf 'Musisz podać ścieżkę do pliku.\n'
  exit 1
fi

if ! [[ -f "$file_path" ]]; then
  printf 'Taki plik nie istnieje.\n'
  exit 1
fi

declare -r words_to_replace=( 'ala' 'basia' )
declare -r replacement_text='janek'

pattern=$(printf '%s|' "${words_to_replace[@]}")

text_before_replacement=$(cat "$file_path")
text_after_replacement=$(gsed -E "s/\b($pattern})\b/$replacement_text/g" "$file_path")

printf 'Tekst przed zamianą\n%s\n\n' "$text_before_replacement"
printf 'Tekst po zamianie\n%s\n\n' "$text_after_replacement"
