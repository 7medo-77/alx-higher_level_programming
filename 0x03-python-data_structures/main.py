#!/usr/bin/python3
# 5-no_c.py
# no_c = __import__('5-no_c').no_c
#
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))
