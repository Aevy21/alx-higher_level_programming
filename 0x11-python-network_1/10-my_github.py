#!/usr/bin/python3

"""
A script that uses GitHub API to display the user's id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'

    response = requests.get(url, auth=(username, password))
    user_info = response.json()
    print(user_info.get('id'))
