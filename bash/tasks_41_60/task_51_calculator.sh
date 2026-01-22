#!/usr/bin/env bash

is_numeric() {
  [[ "$1" =~ ^-?[0-9]+$ ]]
}

is_operator() {
  [[ "$1" =~ ^(\+|-|\*|/)$ ]]
}

read -rp 'Podaj pierwszą liczbę całkowitą: ' a
is_numeric "$a" || { printf 'Błędna liczba: %s\n' "$a"; exit 1; }

read -rp 'Podaj operację {+,-,*,=}: ' operation
is_operator "$operation" || { printf 'Błędna operacja: %s\n' "$operation"; exit 1; }

read -rp 'Podaj pierwszą liczbę całkowitą: ' b
is_numeric "$b" || { printf 'Błędna liczba: %s\n' "$b"; exit 1; }

if [[ "$operation" == '/' && "$b" -eq 0 ]]; then
  printf 'Nie można dzielić przez 0.\n'
  exit 1
fi

case "$operation" in
  +)
    result=$(( a + b ))
    ;;
  -)
    result=$(( a - b ))
    ;;
  \*)
    result=$(( a * b ))
    ;;
  /)
    result=$(( a / b ))
    ;;
esac

printf 'Wynik: %s\n' "$result"

