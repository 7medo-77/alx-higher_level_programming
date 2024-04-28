#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
