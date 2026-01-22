#!/usr/bin/env bash

file_path="$1"

if [[ -z "$file_path" ]]; then
  printf 'Musisz podać ścieżkę do pliku.\n'
  exit 1
fi

if ! [[ -f "$file_path" ]]; then
  printf 'Podany plik nie istnieje.\n'
  exit 1
fi

remove_quotations() {
  local text="$1"
  local text_length="${#text}"

  for (( i = 0; i < "$text_length" / 2; i++ )); do
    if [[ "${text:0:1}" == "${text: -1:1}" ]]; then
      text="${text:1:-1}"
    fi
  done

  printf '%s' "$text"
}

while IFS= read -r line || [[ -n "$line" ]]; do
  printf '%s\n' "$(remove_quotations "$line")"
done < "$file_path"