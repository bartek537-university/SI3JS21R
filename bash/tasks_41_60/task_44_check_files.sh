#!/usr/bin/env bash

read -rp 'Podaj typ plików (rozszerzenie): .' file_extension

shopt -s nullglob # W przypadku nieznalezienia plików, w tablicy nie zostanie zapisany wzorzec.
files=( ./*."$file_extension" )

if [[ "${#files}" -gt 0 ]]; then
  ./task_43_remove_files_of_type_2.sh . "$file_extension"
  printf "Nie wszystkie pliki z rozszerzeniem .%s w bieżącym katalogu.\n" "${file_extension}"
else
  printf "Nie znaleziono plików z rozszerzeniem .%s w bieżącym katalogu.\n" "${file_extension}"
fi
