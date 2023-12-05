#!/usr/bin/python3
"""
script that adds command line args to a Python[] and saves it to a JSON file.
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Load existing list from the file or create an empty list
myList = load_from_json_file("add_item.json")

# Add command line arguments to the list
myList.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(myList, "add_item.json")
