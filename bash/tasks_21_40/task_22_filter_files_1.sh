#!/usr/bin/env bash

read -rp 'Podaj ścieżkę do katalogu wejściowego: ' input_folder

if [[ ! -d "$input_folder" ]]; then
  printf 'Taki katalog nie istnieje'
  exit 1
fi

read -rp 'Podaj ścieżkę do pliku wyjściowego: ' output_file

find "$input_folder" \( -type f -o -type d \) > "$output_file" # Tylko katalogi i pliki.
