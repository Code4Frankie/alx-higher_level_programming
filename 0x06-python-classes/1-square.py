#!/usr/bin/python3
"""defining the Square class"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size
