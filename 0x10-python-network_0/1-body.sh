#!/usr/bin/env bash
# Display only body of a 200 status code response

curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -sl "$1"
