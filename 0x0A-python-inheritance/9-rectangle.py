#!/usr/bin/python3
"""
Module which defines a child class Rectangle which inherits from parent
class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class with private attributes
    """
    def __init__(self, width, height):
        """Constructor method initializing Rectangle object"""
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """Method which returns the area of Rectangle"""
        return (self.__height * self.__width)

    def __str__(self):
        """Method which returns the string representation of class Rectangle"""
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__width\
                                    , self.__height))
