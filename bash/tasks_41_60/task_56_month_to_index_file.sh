#!/usr/bin/env bash

file_name="$1"

if [[ -z "$file_name" ]]; then
  printf 'Musisz podać nazwę pliku.\n'
  exit 1
fi

if ! [[ -f "$file_name" ]]; then
  printf 'Podany plik nie istnieje.\n'
  exit 1
fi

month_name=$(< "$file_name")

declare -Ar months=(
  ['styczeń']=1
  ['luty']=2
  ['marzec']=3
  ['kwiecień']=4
  ['maj']=5
  ['czerwiec']=6
  ['lipiec']=7
  ['sierpień']=8
  ['wrzesień']=9
  ['październik']=10
  ['listopad']=11
  ['grudzień']=12
)

month_number=${months["${month_name,,}"]}

if [[ -z "$month_number" ]]; then
  printf 'Miesiąc nie został odnaleziony.\n'
  exit 1
fi

printf 'Miesiąc %s ma numer %s.\n' "${month_name}" "$month_number"
