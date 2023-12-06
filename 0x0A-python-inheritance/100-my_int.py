#!/usr/bin/python3
"""A rebellious integer class with inverted equality operators."""


class MyInt(int):
    """
    MyInt class overrides equality operators for rebellious behavior.
    """

    def __eq__(self, other):
        """Override the equality operator (==)."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator (!=)."""
        return super().__eq__(other)
