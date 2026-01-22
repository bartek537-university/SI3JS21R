#!/usr/bin/env bash

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

read -rp 'Podaj nazwę miesiąca: ' month_name

month_name=$(echo "$month_name" | tr '[:upper:]' '[:lower:]')

if [[ -z "$month_name" ]]; then
  printf 'Musisz podać nazwę miesiąca.\n'
  exit 1
fi

month_number=${months["$month_name"]}

if [[ -z "$month_number" ]]; then
  printf 'Miesiąc nie został odnaleziony.\n'
  exit 1
fi

printf 'Miesiąc %s ma numer %s.\n' "$month_name" "$month_number"