#!/bin/bash
# Displays the body of http GET request only if it has a status code of 200
if [[ $(curl -sIL "$1" | grep "HTTP/" | tail -n1 | cut -d ' ' -f 2) -eq 200 ]]; then curl -sL "$1"; fi
