#!/usr/bin/env bash

case $1 in
utworz)
  touch test.txt
  ;;
usun)
  rm test.txt 2>/dev/null || :
  ;;
*)
  printf 'Nieznane polecenie.\n'
  exit 1
  ;;
esac