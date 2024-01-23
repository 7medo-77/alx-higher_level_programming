#!/usr/bin/python3
"""Module to instantiate a class"""


class Square:
    """
    Function to instantiate a class Square,
    with optional size attribute and with
    error handling
    """

    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise ValueError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    """
    Function to calculate the area of a square instance
    """
    def area(self):
        return (self.__size ** 2)
