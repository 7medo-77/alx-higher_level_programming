#!/bin/bash
# Bash script which uses a DELETE method for HTTP request
curl -sI "$1" | grep "Allow" | sed "s/\s//"| cut -d ':' -f 2-
