#!/usr/bin/python3
"""
a function that prints a square with the character #.
"""
def print_square(size):
    """
    Args:
        size: size of the square printed

    Returns:
        No return
    """
     if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
