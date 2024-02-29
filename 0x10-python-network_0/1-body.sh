#!/bin/bash
# This script takes a URL as input, sends a GET request to the URL using curl, and displays the body of the response for a 200 status code.

response=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$1")
if [ "$response" -eq 200 ]; then
    curl -s -X GET "$1"
fi
