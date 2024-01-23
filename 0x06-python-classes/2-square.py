
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
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
