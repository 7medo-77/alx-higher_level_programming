#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -s -H "Content-Type: application/json" --data @"$2" "$1"
