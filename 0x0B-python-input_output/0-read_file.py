#!/usr/bin/python3
"""
Module for reading a text file (UTF8) and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Function to read and print the content of a text file.

    Args:
        filename (str): The name of the file to read (default to empty).
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
