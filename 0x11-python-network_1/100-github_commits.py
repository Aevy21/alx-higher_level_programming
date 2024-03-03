#!/usr/bin/python3

"""
Script to fetch commits of a repository using GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    # Get repository name and owner name from command-line arguments
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Construct the URL to fetch commits
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    # Send a GET request to fetch commits
    response = requests.get(url)

    # Check if the response status code indicates success
    if response.status_code == 200:
        # Parse the commits information
        commits = response.json()[:10]

        # Print the commit hashes and author names
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        # Print an error message
        print("Failed to fetch commits. Error code:", response.status_code)
