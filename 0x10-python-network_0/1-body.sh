#!/usr/bin/bash
# Displays the body of http GET request only if it has a status code of 200
if [[ $(curl -sI "$1" | grep "HTTP/" | cut -d ' ' -f 2) -eq 200 ]]; then curl "$1"; fi
