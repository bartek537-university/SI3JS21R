#!/usr/bin/env bash

texts=()

while read -rp 'Podaj ciąg tekstu: ' text; do
  if [[ -z "$text" ]]; then
    break
  fi
  texts+=("$text")
done

printf '%s' "${texts[@]}"
printf '\n'