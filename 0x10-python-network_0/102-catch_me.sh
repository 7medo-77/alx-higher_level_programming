#!/bin/bash
# Bash script sends a PUT request along with a custom header variable
curl -L -X PUT -d "user=98" "0.0.0.0:5000/catch_me"
