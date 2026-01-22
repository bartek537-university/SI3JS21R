input_directory="$1"
file_extension="$2"

if [[ -z "$input_directory" ]]; then
  printf 'Musisz podać katalog wejściowy.\n'
  exit 1
fi

if [[ -z "$file_extension" ]]; then
  printf 'Musisz podać typ plików do usunięcia.\n'
  exit 1
fi

find "$input_directory" -name "*.${file_extension}" -exec rm {} \;