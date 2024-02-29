#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl in silent mode (-s), and displays the size of the body of the response in bytes.
curl -s "$1" | tail -c +$(($(curl -sI "$1" | awk '/Content-Length/{print $2}') + 1)) | wc -c
