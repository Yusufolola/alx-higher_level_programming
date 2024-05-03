#!/bin/bash
#  script that sends a JSON POST request to a URL passed as the first argument
curl -sX "POST" -H "Content-Type: application/json" -d @"$2" "$1"