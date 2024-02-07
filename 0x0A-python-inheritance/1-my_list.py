#!/usr/bin/python3
"""
print sorted list
"""


class MyList(list):
    """
    Custom class
    """
    def __init__(self):
        """Constructor method from parent class"""
        super().__init__()

    def print_sorted(self):
        """method that prints a sorted list"""
        print(sorted(self))
