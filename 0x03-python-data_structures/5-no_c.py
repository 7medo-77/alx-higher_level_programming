#!/usr/bin/python3
def no_c(my_string):
    list_no = [i for i in my_string if i != 'c' and i != 'C']
    for i in list_no:
        if (i == list_no[-1:]):
            print("{}".format(i))
        else:
            print("{}".format(i), end="")
