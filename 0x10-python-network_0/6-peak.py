#!/usr/bin/python3
"""Python script which finds the peak element in an array"""


import string

def find_peak(list_of_integers):
    peak_list = []
    for index, num in enumerate(list_of_integers):
        if (not list_of_integers[index - 1] or not list_of_integers[index + 1] ):
            if (not list_of_integers[index - 1] and num > list_of_integers[index + 1] ):
                peak_list.append(num)
            elif (not list_of_integers[index + 1] and num > list_of_integers[index - 1]):  
                peak_list.append(num)
        elif (num > list_of_integers[index + 1] and num > list_of_integers[index - 1]):
            peak_list.append(num)
    return (max(peak_list))
