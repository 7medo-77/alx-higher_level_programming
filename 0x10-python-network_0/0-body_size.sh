#!/usr/bin/env bash
# Bash script which displays the size of the body of the HTTP response
curl -I "$1" | grep 'Length' | cut -d ":" -f 2 | sed "s/\s//g"
