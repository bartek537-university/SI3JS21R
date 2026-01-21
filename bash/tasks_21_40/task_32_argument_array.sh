original_arguments=( "$@" )

if [[ "${#original_arguments[@]}" -ne 5 ]]; then
  printf 'Musisz podać dokładnie 5 parametrów.'
  exit 1
fi

shifted_arguments=( "${original_arguments[@]:2}" "${original_arguments[@]:0:2}" )

echo "${shifted_arguments[@]}"

