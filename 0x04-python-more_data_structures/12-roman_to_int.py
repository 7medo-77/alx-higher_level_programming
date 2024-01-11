#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string):
        return (0)
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    rolling_sum = 0
    for char in roman_string:
        for key, value in roman_dict.items():
            if (char == key):
                rolling_sum += value
    return (rolling_sum)
