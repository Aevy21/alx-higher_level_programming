# 0x11. Python - Network #1
## Using urllib in Python

## Introduction
This repository contains a Python script that demonstrates how to fetch a URL using the `urllib` package. The script fetches the contents of a URL and displays information about the response body.

## Requirements
- Python 3.x

## Installation
No installation is required. Just clone this repository or download the `fetch_url.py` script.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the directory containing the `fetch_url.py` script.
3. Run the script using the command: `python fetch_url.py`

## What the Script Does
The `fetch_url.py` script performs the following steps:
1. Imports the `urllib.request` module.
2. Defines the URL to fetch.
3. Opens a connection to the URL using `urllib.request.urlopen`.
4. Reads the response body and decodes it as UTF-8.
5. Displays information about the response body, including its type and content.

## Commonly Used Methods in urllib.request

The `urllib.request` module provides several commonly used methods for working with URLs:

1. `urlopen(url, data=None, timeout=<object object>)`: Opens a network object denoted by a URL for reading. Returns a file-like object with two additional methods: `geturl()` and `info()`.

2. `Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)`: Constructs a request object with optional data and headers.

3. `urlretrieve(url, filename=None, reporthook=None, data=None)`: Retrieves a URL and saves it locally. Returns a tuple `(filename, headers)`.

4. `pathname2url(path)`: Converts a path name to a URL-encoded string.

5. `url2pathname(path)`: Converts a URL-encoded string to a path name.

These methods provide the basic functionality for interacting with URLs and making HTTP requests in Python using the `urllib.request` module.

## Additional Notes
- This script uses the `with` statement to ensure that the connection to the URL is properly closed after use.
- Only the `urllib` package is used in this script. No additional packages are imported.
- The script is designed to be simple and educational, demonstrating basic usage of the `urllib` package.

