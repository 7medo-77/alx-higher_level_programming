#!/bin/bash
# Bash script sends a PUT request along with a custom header variable
curl -L -H "Content-Type: text/plain" -X PUT "You got me!" "0.0.0.0:5000/catch_me"
