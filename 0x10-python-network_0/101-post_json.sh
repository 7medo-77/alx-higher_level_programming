#!/bin/bash
# Bash script sends a GET request along with a custom header variable
curl --json @"$2" "$1"
