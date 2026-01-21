#!/bin/zsh

if [[ -z "$1" ]]; then
  echo 'Musisz podać katalog do oczyszczenia.'
  exit 1
fi

if [[ ! -d "$1" ]]; then
  echo 'Podany katalog nie istnieje.'
  exit 1
fi

find "$1" -type f -exec rm {} \;