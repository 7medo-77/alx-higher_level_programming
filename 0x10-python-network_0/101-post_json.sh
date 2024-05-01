#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl --data-raw @"$2" "$1"
