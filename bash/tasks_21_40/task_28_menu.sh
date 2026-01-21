#!/usr/bin/env bash

print_option() {
  printf "%2d %s\n" "$1" "$2"
}

print_menu() {
  printf -- '------------( Menu )------------\n'
  print_option 1 'O programie'
  print_option 0 'Wyjdź z programu'
  printf -- '--------------------------------\n'
}

print_about() {
  printf -- '---------( O programe )---------\n'
  printf ' © Bartosz Bieniek\n'
  print_option 0 'Wyjdź do głównego menu'
  printf -- '--------------------------------\n'
}

menu_main() {
  print_menu
  while true; do
      read -r selected_option
      if [[ $selected_option == 0 ]]; then
        exit 0
      elif [[ $selected_option == 1 ]]; then
        menu_about
        print_menu
      else
        printf 'Musisz wybrać jedną z dostępnych opcji {0,1}.\n'
      fi
  done
}

menu_about() {
  print_about
  while true; do
      read -r selected_option
      if [[ $selected_option == 0 ]]; then
        return
      else
        printf 'Musisz wybrać jedną z dostępnych opcji {0}.\n'
      fi
  done
}

menu_main

