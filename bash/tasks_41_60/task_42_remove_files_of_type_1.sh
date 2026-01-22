read -rp 'Podaj typ plików (rozszerzenie): .' file_extension

if [[ -z "$file_extension" ]]; then
  printf 'Musisz podać typ plików do usunięcia.\n'
  exit 1
fi

find . -name "*.${file_extension}" -exec rm {} \;