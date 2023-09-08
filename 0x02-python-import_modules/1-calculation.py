#!/usr/bin/python3

"""
This function imports calculation functions from the file calculator_1.py and
prints the result.
"""

from calculator_1 import add, sub, mul, div

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
