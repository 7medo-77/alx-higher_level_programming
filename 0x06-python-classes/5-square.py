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

    """
    Getter function to get the value of size
    """
    @property
    def size(self):
        return (self.__size)

    """
    Setter function to set the value of size
    """
    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(self.__size, int):
            raise ValueError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    """
    Function to calculate the area of a square instance
    """
    def area(self):
        return (self.__size ** 2)

    """
    Function to print square by # of size
    """
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(0, self.__size):
                for x in range(0, self.__size):
                    print("#", end="")
                print()
