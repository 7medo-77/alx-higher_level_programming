#!/bin/bash
# Bash script sends a PUT request along with a custom header variable
curl -sL -H "Content-Type: text/plain" -X PUT "You got me!" "$1"
