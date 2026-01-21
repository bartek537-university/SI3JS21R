#!/usr/bin/env bash

set_title() {
  printf '\e]0;%s\a' "$1"
}

if [[ -z "$1" ]]; then
  printf 'Musisz podać tytuł.\n'
  exit 1
fi

set_title "$1"
