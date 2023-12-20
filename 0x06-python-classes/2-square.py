#!/usr/bin/python3

class Square:
    """
    A class representing a square.

    Attributes:
    - __size (int): Private instance attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Parameters:
        - size (int, optional): The size of the square. Default is 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

