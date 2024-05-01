#!/bin/bash
# Bash script sends a PUT request along with a custom header variable
curl -L -X PUT -d "You got me!" -H "Content-Type: text/plain" "0.0.0.0:5000/catch_me"
