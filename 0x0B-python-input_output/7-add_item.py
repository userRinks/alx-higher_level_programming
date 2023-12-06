#!/usr/bin/python3
"""
Script to add all cmd-line arguments to Python list and save to JSON file
"""

import sys
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Filename for the JSON file
filename = "add_item.json"

# Check if the file exists, and load the existing list if it does
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
