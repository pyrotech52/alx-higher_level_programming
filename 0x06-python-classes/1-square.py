#!/usr/bin/python3
"""Square class definition"""


class Square:
    """A class representing a square.

    Attributes:
    - __size (int): Private instance attr. that reps. the size of d  sqr"""

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Parameters:
        - size (int): The size of the square.
        """
        self.__size = size
