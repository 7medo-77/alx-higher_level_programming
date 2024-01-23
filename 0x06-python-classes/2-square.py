#!/usr/bin/python3
"""Module to instantiate a class"""


class Square:
    """
    Function to instantiate a class Square,
    with optional size attribute and with
    error handling
    """

    def __init__(self, size=0):
        try:
            self.__size = size
            if size is None:
                size = 0
        except TypeError:
            print("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
