#!/bin/bash
# Bash script which displays the size of the body of the HTTP response
curl -sI "$1" | grep 'Length' | cut -d ":" -f 2 | sed "s/\s//g"
