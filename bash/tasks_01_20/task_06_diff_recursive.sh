files=()

while read -r -d '' file; do
  files+=("$file")
done < <(find ~ -type f -maxdepth 1 -print0)

echo "${files[@]}"

for a in "${files[@]}"; do
  for b in "${files[@]}"; do
    diff "$a" "$b"
  done
done
