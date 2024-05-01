#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -s -o /dev/null -w "%{http_code}" "$1"
