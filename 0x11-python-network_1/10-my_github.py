#!/usr/bin/python3

"""
This script takes GitHub credentials (username and \
        personal access token) as input and uses the GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://github.com/Aevy21'

    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        user_info = response.json()
        print("User ID:", user_info['id'])
    else:
        print("Failed to retrieve user information. Status code:", response.status_code)
