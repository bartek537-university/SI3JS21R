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

true > "$output_file"

for (( i = 0; i <= n; i++ )); do
  printf '%d\n' "$i" >> "$output_file"
done