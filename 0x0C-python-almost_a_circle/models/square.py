#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square 
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Args:
            size: size of square
            x: x position 
            y: y position 
            id: id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriden method
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """the size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """ the size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Assigns attributes
        """
        lst = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + lst[len(args):len(lst)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

