#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response.
awk '/^HTTP/{if ($2 ~ /^[0-9]+$/) print $2}' < <(curl -sI "$1")
