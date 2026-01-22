#!/usr/bin/env bash

read -rp 'Podaj ścieżkę pierwszego pliku: ' first_path

if ! [[ -f "$first_path" ]]; then
  printf 'Podany plik nie istnieje.\n'
  exit 1
fi

read -rp 'Podaj ścieżkę drugiego pliku: ' second_path

if ! [[ -f "$second_path" ]]; then
  printf 'Podany plik nie istnieje.\n'
  exit 1
fi

read_file() {
  local -n lines="$1"
  lines=()

  while IFS= read -r line || [[ -n $line ]]; do
    lines+=("$line")
  done < "$2"
}

read_file first_lines "$first_path"
read_file second_lines "$second_path"

# shellcheck disable=SC2154
(( max_lines = "${#first_lines[@]}" > "${#second_lines[@]}" ? "${#first_lines[@]}" : "${#second_lines[@]}"))

for (( i = 0; i < max_lines; i++ )); do
  printf '%s%s\n' "${first_lines[i]}" "${second_lines[i]}"
done
