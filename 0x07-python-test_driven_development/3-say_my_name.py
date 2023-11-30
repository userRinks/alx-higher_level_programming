#!/usr/bin/python3
""" Print My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string stating the first and last name.

    Parameters:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to empty string

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        str: A formatted string indicating the full name.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print ("My name is {} {}".format(first_name, last_name))
