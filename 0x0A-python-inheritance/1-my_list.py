#!/usr/bin/python3
"""This module defines a class MyList that inherits from list."""

class MyList(list):
    """
    MyList is a child class of list.
    It inherits all the methods and properties of the list class.
    """

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        print(sorted(self))
)
