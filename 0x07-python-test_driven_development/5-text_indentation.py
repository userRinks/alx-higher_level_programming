#!/usr/bin/python3
""" Indent by turning a sentence into a paragraph. """


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':' character.

    Parameters:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize the index
    c = 0

    # Skip leading spaces
    while c < len(text) and text[c] == ' ':
        c += 1

    # Iterate through the text
    while c < len(text):
        # Print the character
        print(text[c], end="")

        # Check for newline or specified characters
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1

            # Skip trailing spaces
            while c < len(text) and text[c] == ' ':
                c += 1
            continue

        # Move to the next character
        c += 1
