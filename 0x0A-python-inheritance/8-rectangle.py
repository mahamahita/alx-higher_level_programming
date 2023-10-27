#!/usr/bin/python3

"""A class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

# Import the BaseGeometry class from 7-base_geometry


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
