#!/usr/bin/python3

"""
Script that displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    # Get the URL from the command-line arguments
    url = sys.argv[1]

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the response status code indicates an error
    if response.status_code >= 400:
        # Print the error code
        print("Error code:", response.status_code)
    else:
        # Print the body of the response
        print(response.text)
