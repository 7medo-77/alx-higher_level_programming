#!/usr/bin/python3
"""
Module which opens, reads and prints and content of a file to stdout
"""


def read_file(filename=""):
    """Function that opens and reads content of the file"""
    with open(filename) as file_1:
        read_file = file_1.read()
        print(read_file, end="")
