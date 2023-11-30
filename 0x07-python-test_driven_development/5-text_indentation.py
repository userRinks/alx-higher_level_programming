#!/usr/bin/python3
"""
Prints a text with 2 new lines after each '.', '?' or `:` character
"""


def text_indentation(text):
    """ Parameters: text (str): The input text.
    Raises:
        TypeError: If text is not a string.
    Returns: None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    index = 0

    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")

        if text[index].isspace() or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1

            while index < len(text) and text[index] == ' ':
                index += 1
            continue

        index += 1
