#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    A class that inherits from list and provides additional methods.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        Returns:
            None.
        """
        print(sorted(self))
