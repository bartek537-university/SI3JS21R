#!/usr/bin/env bash

print_case() {
  printf ' %2s. %s\n' "$1" "$2"
}

print_menu() {
  printf -- '--------( Menu )--------\n'

  print_case '1' 'Opcja pierwsza.'
  print_case '2' 'Opcja druga.'
  print_case '3' 'Opcja trzecia.'

  printf -- '------------------------\n'
}

print_menu

while true; do
  read -rp ': ' selected_option
  case "$selected_option" in
  1)
    printf 'Wybrano opcję pierwszą.\n'
    ;;
  2)
    printf 'Wybrano opcję drugą.\n'
    ;;
  3)
    printf 'Wybrano opcję trzecią.\n'
    ;;
  *)
    printf 'Musisz wybrać jedną z dostępnych opcji.\n'
    ;;
  esac
done
