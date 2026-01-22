#!/usr/bin/env bash

if [[ -z "$1" ]]; then
  printf 'Musisz podać tekst.\n'
  exit 1
fi

declare -r words_to_remove=("ala" "kot")
pattern=$(printf '%s|' "${words_to_remove[@]}")

whole_words_removed=$(echo "$1" | gsed -E "s/\b($pattern)\b//g")
word_parts_removed=$(echo "$1" | gsed -E "s/($pattern)//g")

printf 'Usunięte całe słowa: %s\n' "${whole_words_removed}"
printf 'Usunięte części słów: %s\n' "${word_parts_removed}"

