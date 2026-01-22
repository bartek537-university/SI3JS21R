output_file="$1"

if [[ -z "$output_file" ]]; then
  printf 'Musisz podać ścieżkę pliku wyjściowego\n'
  exit 1
fi

read -rp 'Podaj n: ' n

if [[ n -lt 0 ]]; then
  printf 'n musi być nieujemne\n'
  exit 1
fi

numbers=( "$(seq 0 "$n")" )

true > "$output_file"

for number in "${numbers[@]}"; do
  printf '%s\n' "$number" >> "$output_file"
done