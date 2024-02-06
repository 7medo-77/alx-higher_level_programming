#!/usr/bin/python3
"""
print sorted list
"""


class MyList(list):
    """
    Custom class
    """
    def print_sorted(self):
        """method that prints a sorted list"""
        print(sorted(self))
