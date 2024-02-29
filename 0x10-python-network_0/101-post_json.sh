#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the body, and displays the body of the response.
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
