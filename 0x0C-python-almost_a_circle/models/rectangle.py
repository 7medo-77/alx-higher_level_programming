#!/usr/bin/python3
"""
Module that defines a Rectangle class which inherits from the Base class
"""
from .base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class with 4 private instance
        attributes
        """
        self.__width = self.input_validator_dimension(width, "width")
        self.__height = self.input_validator_dimension(height, "height")
        self.__x = self.input_validator_axis(x, "x")
        self.__y = self.input_validator_axis(y, "y")
        super().__init__(id)

    def input_validator_dimension(self, dimension, attribute):
        """
        Input validation method for dimension data flow
        """
        if (not isinstance(dimension, int)):
            raise TypeError("{} must be and integer".format(attribute))
        elif (dimension <= 0):
            raise ValueError("{} must be > 0".format(attribute))
        else:
            return (dimension)

    def input_validator_axis(self, axis, attribute):
        """
        Input validation method for dimension data flow
        """
        if (not isinstance(axis, int)):
            raise TypeError("{} must be and integer".format(attribute))
        elif (axis < 0):
            raise ValueError("{} must be >= 0".format(attribute))
        else:
            return (axis)

    @property
    def x(self):
        """Getter Method for private attribute x"""
        return self.__x

    @property
    def y(self):
        """Getter Method for private attribute y"""
        return self.__y

    @property
    def width(self):
        """Getter Method for private attribute width"""
        return self.__width

    @property
    def height(self):
        """Getter Method for private attribute height"""
        return self.__height

    """
    Setter methods in Rectangle class
    """
    @x.setter
    def x(self, x):
        """Setter Method for private attribute x"""
        self.__x = self.input_validator_axis(x, "x")

    @y.setter
    def y(self, y):
        """Setter Method for private attribute x"""
        self.__y = self.input_validator_axis(y, "y")

    @width.setter
    def width(self, width):
        """Setter Method for private attribute x"""
        self.__width = self.input_validator_dimension(width, "width")

    @height.setter
    def height(self, height):
        """Setter Method for private attribute x"""
        self.__height = self.input_validator_dimension(height, "height")

    """
    Miscellaneous methods
    """
    def area(self):
        """Returns the area of the rectangle instance"""
        return (self.__width * self.__height)

    def display(self):
        """Prints the area of the rectangle instance with # symbol"""
        for i in range(0, self.__height):
            if (i == 0):
                print("\n" * self.__y, end="")
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """String representation of the instance"""
        return (
            "[{}] ({}) {}/{} - {}/{}".format(
                self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height
            )
        )

    def update(self, *args, **kwargs):
        """
        Update method that updates the attributes
        in the method's paramters
        """
        arg_dict = {1: "id", 2: "width", 3: "height", 4: "x", 5: "y"}
        if (args):
            for index, arg in enumerate(args):
                for key, value in arg_dict.items():
                    if index + 1 == key:
                        if (key == 2 or key == 3):
                            arg = self.input_validator_dimension(arg, value)
                            setattr(self, value, arg)
                        elif (key == 4 or key == 5):
                            arg = self.input_validator_axis(arg, value)
                            setattr(self, value, arg)
                        else:
                            setattr(self, value, arg)
        else:
            for attribute, integer in kwargs.items():
                for key, value in arg_dict.items():
                    if (value == attribute):
                        if (key == 2 or key == 3):
                            integer = self.input_validator_dimension(
                                integer, value)
                            setattr(self, value, integer)
                        elif (key == 4 or key == 5):
                            integer = self.input_validator_axis(integer, value)
                            setattr(self, value, integer)
                        else:
                            setattr(self, value, integer)

    def to_dictionary(self):
        """Return dictionary representation of an instance"""
        self_dict = {
            "x": self.x, "y": self.y, "id": self.id,
            "width": self.width, "height": self.height
        }
        return (self_dict)
