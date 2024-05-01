#!/bin/bash
# Bash script sends a PUT request along with a custom header variable
curl -sL -X PUT "You got me!" -d "user_id=98" "0.0.0.0:5000/catch_me"
