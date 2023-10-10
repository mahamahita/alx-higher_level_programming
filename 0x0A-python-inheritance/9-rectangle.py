#!/usr/bin/python3
""" a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        return self.__width * self.__height

    def __str__(self):

        return "[Rectangle] {}/{}".format(self.__width, self.__height)

