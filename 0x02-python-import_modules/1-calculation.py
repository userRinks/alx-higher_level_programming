#!/usr/bin/python3

"""
This program imports calculation functions from calculator_1.py
and prints the results of various mathematical operations.
"""

from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    result_add = add(a, b)
    result_sub = sub(a, b)
    result_mul = mul(a, b)
    result_div = div(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, result_add))
    print("{:d} - {:d} = {:d}".format(a, b, result_sub))
    print("{:d} * {:d} = {:d}".format(a, b, result_mul))
    print("{:d} / {:d} = {:d}".format(a, b, result_div))

if __name__ == "__main__":
    main()
