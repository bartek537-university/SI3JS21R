#!/usr/bin/env bash

set_title() {
  printf '\e]0;%s\a' "$1"
}

read -rp 'Podaj swoje imię: ' user_name
set_title "$user_name"
