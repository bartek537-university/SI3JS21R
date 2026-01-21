#!/usr/bin/env bash

printf 'Wybierz lokalizację\n'
printf ' 0. ~/Downloads\n'
printf ' 1. /var/log\n'

read -rp ': ' option

case "$option" in
  0)
    path="${HOME}/Downloads"
    ;;
  1)
    path='/var/log'
    ;;
  *)
    printf 'Błędna opcja\n'
    exit 1
    ;;
esac

cd "$path" || exit 2
ls
