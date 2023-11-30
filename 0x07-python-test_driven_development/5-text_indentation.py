#!/usr/bin/python3
"""
Prints a text with 2 new lines after each '.', '?' or `:` character
"""


def text_indentation(text):
    """
    Parameters:
        text (str): The input text.
    Raises:
        TypeError: If text is not a string.
    Returns: None
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the index
    index = 0

    # Skip leading spaces
    while index < len(text) and text[index] == ' ':
        index += 1

    # Iterate through the text
    while index < len(text):
        # Print the character
        print(text[index], end="")

        # Check for newline or specified characters
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")
            index += 1

            # Skip trailing spaces
            while index < len(text) and text[index] == ' ':
                index += 1
            continue

        # Move to the next character
        index += 1
