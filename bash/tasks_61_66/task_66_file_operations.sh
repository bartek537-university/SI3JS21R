#!/usr/bin/env bash

directory="$1"

if [[ -z "$directory" ]]; then
  printf 'Musisz podać ścieżkę do katalogu.\n'
  exit 1
fi

if ! [[ -d "$directory" ]]; then
  printf 'Podany katalog nie istnieje.\n'
  exit 1
fi

read -rp 'Czy kopiować zmienione pliki? [t/N]: ' should_copy_response

if [[ "$should_copy_response" == 't' ]]; then
  read -rp 'Podaj datę [YYYY-MM-DD]: ' selected_date_text
  threshold_timestamp=$(date -j -f '%Y-%m-%d' "$selected_date_text" +%s 2>/dev/null) || { printf 'Niepoprawna data.\n'; exit 1; }

  read -rp 'Podaj katalog wyjściowy: ' copy_output_directory
  [[ -d "$copy_output_directory" ]] || { printf 'Podany katalog nie istnieje.\n'; exit 1; }
fi

source_extension='txt'
target_extension='bmp'

find "$directory" -type f -name "*.$source_extension" -print0 |
while IFS= read -rd '' input_file_path; do
  result_file_path="${input_file_path%.*}.${target_extension}"
  should_copy_file=1

  if [[ "$should_copy_response" == 't' ]]; then
    if [[ $(stat -f %m "$input_file_path") -lt "$threshold_timestamp" ]]; then
      should_copy_file=0
    fi
  fi

  mv "$input_file_path" "$result_file_path"

  if [[ "$should_copy_file" -eq 0 ]]; then
    cp "$result_file_path" "$copy_output_directory"
  fi
done

