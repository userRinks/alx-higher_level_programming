#!/usr/bin/python3

"""
This script performs addition of two numbers and prints the result.
"""


if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2

    result = add(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, result))
