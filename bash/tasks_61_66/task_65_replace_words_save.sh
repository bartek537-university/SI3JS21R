#!/usr/bin/env bash

input_file_path="$1"
output_file_path="$2"

if [[ -z "$input_file_path" ]]; then
  printf 'Musisz podać ścieżkę do pliku wejściowego.\n'
  exit 1
fi

if ! [[ -f "$input_file_path" ]]; then
  printf 'Taki plik nie istnieje.\n'
  exit 1
fi

if [[ -z "$output_file_path" ]]; then
  printf 'Musisz podać ścieżkę do pliku wyjściowego.\n'
  exit 1
fi

declare -r words_to_replace=( 'ala' 'basia' )
declare -r replacement_text='janek'

pattern=$(printf '%s|' "${words_to_replace[@]}")

gsed -E "s/\b($pattern})\b/$replacement_text/g" "$input_file_path" > "$output_file_path"
