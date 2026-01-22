update_register() {
  printf 'Usuwanie wpisów w rejestrze...\n'
}

print_help() {
  printf 'Pomoc %s:\n' "$0" && grep ' .)\ #' "$0";
}

while getopts "ah" opt; do
  case "${opt}" in
    a) # Aktualizuje wpisy w rejestrze.
      update_register
      ;;
    h) # Wypisuje menu pomocy.
      print_help
      ;;
    *)
      print_help
      ;;
  esac
done