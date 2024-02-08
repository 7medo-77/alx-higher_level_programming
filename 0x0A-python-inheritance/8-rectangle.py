#!/usr/bin/python3
"""
Module which defines a child class Rectangle which inherits from parent
class BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """
    Rectangle class with private attributes
    """
    def __init__(self, width, height):
        """Constructor method initializing Rectangle object"""
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width
