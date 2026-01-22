#!/usr/bin/env bash

read -rp 'Podaj ścieżkę do pliku wyjściowego: ' output_file_path

find . -type d > "$output_file_path"