#!/usr/bin/python3
#!/usr/bin/python3
"""python3 -c 'print(_import("my_module").doc_)'"""


class Square:
    """python3 -c 'print(_import("my_module").MyClass.doc_)'"""
    def _init_(self, size=0, position=(0, 0)):
        if not type(size) == int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = (position[0], position[1])
    """python3 -c 'print(_import("my_module").my_function.doc_)'"""
    @property
    def position(self):
        return self.__position
    """python3 -c 'print(_import("my_module").my_function.doc_)'"""
    @position.setter
    def position(self, value):
        if not (type(value) == tuple and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    """python3 -c 'print(_import("my_module").my_function.doc_)'"""
    def area(self):
        return self.__size**2
    """python3 -c 'print(_import("my_module").my_function.doc_)'"""
    @property
    def size(self):
        return self.__size
    """python3 -c 'print(_import("my_module").my_function.doc_)'"""
    @size.setter
    def size(self, value):
        if not type(value) == int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """python3 -c 'print(_import("my_module").my_function.doc_)'"""
    def my_print(self):
        if self.__size == 0:
            print("")
            return
        for i in range(0, ):


# """Define a class Square."""


# class Square:
#     """Represent a square."""

#     def __init__(self, size=0, position=(0, 0)):
#         """Initialize a new square.

#         Args:
#             size (int): The size of the new square.
#             position (int, int): The position of the new square.
#         """
#         self.size = size
#         self.position = position

#     @property
#     def size(self):
#         """Get/set the current size of the square."""
#         return (self.__size)

#     @size.setter
#     def size(self, value):
#         if not isinstance(value, int):
#             raise TypeError("size must be an integer")
#         elif value < 0:
#             raise ValueError("size must be >= 0")
#         self.__size = value

#     @property
#     def position(self):
#         """Get/set the current position of the square."""
#         return (self.__position)

#     @position.setter
#     def position(self, value):
#         if (not isinstance(value, tuple) or
#                 len(value) != 2 or
#                 not all(isinstance(num, int) for num in value) or
#                 not all(num >= 0 for num in value)):
#             raise TypeError("position must be a tuple of 2 positive integers")
#         self.__position = value

#     def area(self):
#         """Return the current area of the square."""
#         return (self.__size * self.__size)

#     def my_print(self):
#         """Print the square with the # character."""
#         if self.__size == 0:
#             print("")
#             return

#         [print("") for i in range(0, self.__position[1])]
#         for i in range(0, self.__size):
#             [print(" ", end="") for j in range(0, self.__position[0])]
#             [print("#", end="") for k in range(0, self.__size)]
#             print("")
