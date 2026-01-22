#!/usr/bin/env bash

if [[ -z "$1" ]]; then
  printf 'Musisz podać nazwę pliku.\n'
  exit 1
fi

if ! [[ -f "$1" ]]; then
  printf 'Podany plik nie istnieje.\n'
  exit 1
fi

declare -r words_to_remove=("ala" "kot")
pattern=$(printf '%s|' "${words_to_remove[@]}")

whole_words_removed=$(gsed -E "s/\b($pattern)\b//g" "$1")
word_parts_removed=$(gsed -E "s/($pattern)//g" "$1")

printf 'Usunięte całe słowa: %s\n' "${whole_words_removed}"
printf 'Usunięte części słów: %s\n' "${word_parts_removed}"
