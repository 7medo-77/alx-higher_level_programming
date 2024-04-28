#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -d "email=test@gmail.com" -d "subject=I%will%always%be%here%for%PLD" "$1"
