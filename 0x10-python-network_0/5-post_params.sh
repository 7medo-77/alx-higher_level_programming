#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
