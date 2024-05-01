#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl --data-binary @"$2" "$1"
