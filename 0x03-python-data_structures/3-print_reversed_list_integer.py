#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        rev_int = len(my_list) - 1
        for x in my_list:
            print('{:d}'.format(my_list[rev_int]))
            rev_int = rev_int - 1
