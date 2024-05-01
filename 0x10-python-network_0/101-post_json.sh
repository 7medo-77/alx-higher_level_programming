#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -H "Content-Type: application/json" --data-raw @"$2" "$1"
