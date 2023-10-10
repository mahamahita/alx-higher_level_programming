#!/usr/bin/python3
""" a class MyList that inherits from list"""

class MyList(list):
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))

