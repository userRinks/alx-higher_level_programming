#!/usr/bin/python3
"""
Module defining the append_after function.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line with specific string

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in each line.
        new_string (str): Str to insert after lines with the search string
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
        file.truncate()
