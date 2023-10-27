#!/usr/bin/python3

"""This module defines a custom list class called MyList."""


class MyList(list):
    """A class that inherits from the list class.

    This class provides additional methods and functionality on top of the
    standard list class.

    Attributes:
        Inherited from the list class.

    Methods:
        print_sorted: Print the list in sorted order.
    """

    def print_sorted(self):
        """Prints the elements of the list in sorted order.

        This method sorts the list and prints the sorted elements.

        Args:
            None

        Returns:
            None
        """
        print(sorted(self))
