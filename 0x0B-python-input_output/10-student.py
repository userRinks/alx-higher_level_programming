#!/usr/bin/python3
"""
Module defining the Student class.
"""


class Student:
    """
    Student class with public instance attributes and a to_json method.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve (or None)

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        # If attrs is None, retrieve all attributes
        if attrs is None:
            return self.__dict__

        # If attrs is a list, retrieve only the specified attributes
        filtered_attrs = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_attrs[attr] = getattr(self, attr)
        return filtered_attrs
