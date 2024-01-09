#!/usr/bin/python3
# 5-no_c.py
# no_c = __import__('5-no_c').no_c
#
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1
print(list_result)
