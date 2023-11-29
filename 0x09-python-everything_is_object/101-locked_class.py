#!/usr/bin/python3
""" Locked class """


class LockedClass:
    """ Lock creation of attributes, only allow specific """
    __slots__ = ['first_name']

    def __init__(self):
        """Initiate method"""
        pass
