#!/usr/bin/python3
"""Python script which finds the peak element in an array"""


def find_peak(list_of_integers):
    """Function that finds peak in an array"""
    peak_list = []
    for index, num in enumerate(list_of_integers):
        if (index == 0 or index == len(list_of_integers) - 1):
            if (index == 0 and num > list_of_integers[index + 1]):
                peak_list.append(num)
            elif (index == len(list_of_integers) - 1 and
                    num > list_of_integers[index - 1]):
                peak_list.append(num)
        elif (num > list_of_integers[index + 1] and
                num > list_of_integers[index - 1]):
            peak_list.append(num)
    return (max(peak_list) if len(peak_list) > 0 else None)
