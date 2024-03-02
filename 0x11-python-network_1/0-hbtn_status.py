#!/usr/bin/python3

"""
This script fetches the status from https://alx-intranet.hbtn.io/status using urllib.
"""

import urllib.request

def fetch_status():
    """
    Fetches the status from https://alx-intranet.hbtn.io/status and prints it.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        content = response.read()

    print("- Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content.decode('utf-8'))

if __name__ == "__main__":
    fetch_status()
