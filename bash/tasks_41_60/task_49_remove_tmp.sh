if [[ -z "$1" ]]; then
  printf 'Musisz podać katalog do przeszukania.\n'
  exit 1
fi

find "$1" -type f -name '*.tmp' -exec rm {} \;