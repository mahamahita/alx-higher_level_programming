#!/usr/bin/python3

"""A function that checks if an object is an instance of a specified class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    This function takes an object and a class as arguments and checks if
    the object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) == a_class
