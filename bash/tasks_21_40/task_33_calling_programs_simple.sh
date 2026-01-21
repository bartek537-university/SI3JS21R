#!/usr/bin/env bash

directory="$1"

if [[ -z "$directory" ]]; then
  printf 'Musisz wskazać ścieżkę katalogu\n'
  exit 1
fi

if [[ ! -d "$directory" ]]; then
  printf 'Wskazany katalog nie istnieje\n'
  exit 1
fi

directory_name=$(basename "$(cd "$directory" && pwd)")

# chmod u+x ./task_31_title_argument.sh
./task_31_title_argument.sh "$directory_name"
find "$directory"