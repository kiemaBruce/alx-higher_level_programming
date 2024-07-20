#!/bin/bash
# Sends a GET request to url and displays body of response. Also sends a header variable with a value
curl -sL -H "X-School-User-Id: 98" "$1"
