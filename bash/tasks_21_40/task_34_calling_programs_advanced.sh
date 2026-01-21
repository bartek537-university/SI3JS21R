#!/usr/bin/env bash

read -rp 'Podaj ścieżkę do katalogu: ' directory_path

if [[ ! -d "$directory_path" ]]; then
  printf 'Katalog o podanej ścieżce nie istnieje.\n'
  exit 1
fi

read -rp 'Podaj ścieżkę do pliku wyjściowego: ' output_file_path

directory_name=$(basename "$(cd "$directory_path" && pwd)")
./task_31_title_argument.sh "$directory_name"

ls "$directory_path" > "$output_file_path"
