#!/bin/bash

# Przykład: ./tasks_21_40/task_24_backup.sh ./tasks_21_40 ../backup 'yesterday'

input_directory=$1
output_directory=$2
threshold_date=$3

if [[ ! -e "$input_directory" ]]; then
  echo 'Katalog wejściowy nie istnieje.'
  exit 1
fi

if [[ ! -e "$output_directory" ]]; then
  echo 'Katalog docelowy nie istnieje.'
  exit 1
fi

if [[ -z "$threshold_date" ]]; then
  echo 'Nie podałeś daty.'
  exit 1
fi

find "$input_directory" \( \( -newerct "$threshold_date" \) -o \( -type d ! -empty \) \) -exec cp -R {} "$output_directory" \;
