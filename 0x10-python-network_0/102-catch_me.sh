#!/bin/bash
# Bash script sends a PUT request along with a custom header variable
curl  -X PUT "You got me!" -H "Content-Type: text/plain" "$1"
