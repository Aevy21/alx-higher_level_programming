#!/usr/bin/python3

"""
This script takes a URL and an email as input, sends a POST request to the URL.
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email parameter
    data = urllib.parse.urlencode({'email': email}).encode()

    # Send a POST request to the URL with the email parameter
    req = urllib.request.Request(url, data=data, method='POST')

    # Display the body of the response
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
        print(content)
