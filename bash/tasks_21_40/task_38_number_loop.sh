#!/usr/bin/env bash

read -rp 'Podaj ścieżkę do pliku wyjściowego: ' output_file_path
read -rp 'Podaj koniec przedziału 0..' n

if [[ $n -lt 0 ]]; then
  printf 'Koniec przedziału musi być nieujemny.\n'
  exit 1
fi

true > "$output_file_path" # Wyczyszczenie zawartości pliku

for (( i = 0; i <= n; i++ )); do
  printf "%d\n" "$i" >> "$output_file_path"
done

