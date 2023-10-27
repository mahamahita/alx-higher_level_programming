#!/usr/bin/python3

"""A class MyInt that inherits from int and modifies equality operations."""


class MyInt(int):
    """A class representing MyInt that inherits from int and modifies equality operations."""

    def __eq__(self, value):
        """Override the equality (==) operation.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if the real part of the MyInt object is not equal to the value, otherwise False.
        """
        return self.real != value

    def __ne__(self, value):
        """Override the inequality (!=) operation.

        Args:
            value (int): The value to compare with.

        Returns:
            bool: True if the real part of the MyInt object is equal to the value, otherwise False.
        """
        return self.real == value
