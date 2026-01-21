#!/usr/bin/env bash

directory="$1"

if [[ -z "$directory" ]]; then
  printf 'Musisz podać ścieżkę do katalogu docelowego.\n'
  exit 1
fi

if [[ ! -d "$directory" ]]; then
  printf 'Podany katalog nie istnieje.\n'
  exit 1
fi

find . -type f -name '*.txt' -exec cp {} "$directory" \;