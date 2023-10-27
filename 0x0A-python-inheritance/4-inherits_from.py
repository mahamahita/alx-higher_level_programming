#!/usr/bin/python3

"""A function that checks if an object is an instance of a class that inherits from a specified class."""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherits from a specified class.

    This function takes an object and a class as arguments and checks if
    the object is an instance of a class that inherits (directly or indirectly)
    from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.

    Returns:
        bool: True if obj is an instance of a class that inherits from a_class,
        otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
