#!/bin/bash
# Bash script which uses a DELETE method for HTTP request
curl -sI "$1" | grep "Allow" | cut -d ':' -f 2:-1
