#!/usr/bin/python3

"""A class Square that inherits from Rectangle (9-rectangle.py)."""


# Import the Rectangle class from 9-rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
