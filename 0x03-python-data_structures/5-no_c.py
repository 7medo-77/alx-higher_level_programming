#!/usr/bin/python3
def no_c(my_string):
    list_no = [i for i in my_string if i != 'c' and i != 'C']
    string = ''.join(list_no)
    return (string)
