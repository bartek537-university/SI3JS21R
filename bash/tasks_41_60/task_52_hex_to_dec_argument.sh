#!/usr/bin/env bash

declare -rA factors=( ['0']=0 ['1']=1 ['2']=2 ['3']=3 ['4']=4 ['5']=5 ['6']=6 ['7']=7 ['8']=8 ['9']=9
                     ['A']=10 ['B']=11 ['C']=12 ['D']=13 ['E']=14 ['F']=15 )

convert_hex_to_dec() {
  local number="$1"
  local result=0

  local multiplier=1
  for (( i = 1; i <= "${#number}"; i++ )); do
    local char="${number: -i:1}"
    (( result += factors[$char] * multiplier ))
    (( multiplier *= 16 ))
  done

  printf "%d" $result
}

convert_hex_to_dec "$1"