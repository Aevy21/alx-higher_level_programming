#!/usr/bin/python3

"""
Script that adds command line arguments to a Python list and saves it to a JSON file.
"""

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Load existing list from the file or create an empty list
myList = load_from_json_file("add_item.json")

# Add command line arguments to the list
myList.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(myList, "add_item.json")
