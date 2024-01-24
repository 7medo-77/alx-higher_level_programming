#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

# """Module to instantiate a class"""


# class Square:
#     """
#     Function to instantiate a class Square,
#     with optional size attribute and with
#     error handling
#     """

#     def __init__(self, size=0, position=(0, 0)):
#         self.__size = size
#         self.__position = position

#     """
#     Getter function to get the value of size
#     """
#     @property
#     def size(self):
#         return (self.__size)

#     """
#     Setter function to set the value of size
#     """
#     @size.setter
#     def size(self, value):
#         self.__size = value
#         if not isinstance(self.__size, int):
#             raise ValueError("size must be an integer")
#         if self.__size < 0:
#             raise ValueError("size must be >= 0")

#     """
#     Getter function to get the value of position
#     """
#     @property
#     def position(self):
#         return (self.__position)

#     """
#     Setter function to set the value of position
#     """
#     @position.setter

#     def position(self, value):
#             if (not isinstance(value, tuple) or
#                     len(value) != 2 or
#                     not all(isinstance(num, int) for num in value) or
#                     not all(num >= 0 for num in value)):
#                 raise TypeError("position must be a tuple of 
#                   2 positive integers")
#             self.__position = value

#     # def position(self, value):
#     #     if isinstance(value, tuple) and len(value) == 2:
#     #         if (all((isinstance(i, int)) and (i > 0) 
#            for i in value)):
#     #             self.__position = value
#     #         else:
#     #             raise TypeError("position must be a tuple of 
#            2 positive integers")
#     #     else:
#     #         raise TypeError("position must be a tuple of 2 
#            positive integers")

#     """
#     Function to calculate the area of a square instance
#     """
#     def area(self):
#         return (self.__size ** 2)

#     """
#     Function to print square by # of size
#     """
#     def my_print(self):
#         if (self.__size == 0):
#             print()
#         else:
#             for i in range(0, self.__size):
#                 for s in range(0, self.__position[0]):
#                     print(" " if self.__position[1] == 0 else "_", end="")
#                 for c in range(0, self.__size):
#                     print("#", end="")
#                 print()
