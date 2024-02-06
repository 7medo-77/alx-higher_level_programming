#!/usr/bin/python3
"""
Function that reads a text file and prints it to stdout
"""


def read_file(filename=""):
    with open(filename) as file_1:
        read_file = file_1.read()
        print(read_file, end="")
