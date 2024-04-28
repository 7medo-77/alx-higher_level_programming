#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl -Hv "X-School-User-Id: 98" "$1"
