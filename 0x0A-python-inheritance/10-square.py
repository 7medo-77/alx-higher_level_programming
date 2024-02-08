#!/usr/bin/python3
"""
Module which defines a child class Rectangle which inherits from parent
class BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Rectangle class with private attributes
    """
    def __init__(self, size):
        """Constructor method initializing Rectangle object"""
        super().integer_validator("size", size)
        self.__size= size

    def area(self):
        """Method which returns the area of Rectangle"""
        return (self.__size ** 2)

    def __str__(self):
        """Method which returns the string representation of class Rectangle"""
        return ("[{}] {}/{}".format(self.__class__.__name__,\
                                     self.__size, self.__size))
