#!/usr/bin/env bash

declare -a transpose

input="./file.txt"
while IFS= read -r line; do
  i=0
  for field in $line; do
    ((i+=1))
    new_line="${transpose[$i]}$field "
    transpose[$i]="$new_line"
  done
done < "$input"

for line in "${transpose[@]}"; do
  last_char=$((${#line}-1))
  echo ${line:0:last_char}
done
