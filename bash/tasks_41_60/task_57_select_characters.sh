#!/usr/bin/env bash

read -rp 'Podaj ciąg minimum 5 znaków: ' text

if [[ "${#text}" -lt 5 ]]; then
  printf 'Musisz podać conajmniej 5 znaków.\n'
  exit 1
fi

echo "${text:0:1}_${text:2:1}_${text:4:1}..."
echo "ostatnia: ${text: -1}"
echo "przedostatnia: ${text: -2:1}"
echo "przedprzedostatnia i przedostatnia: ${text: -3:2}"
