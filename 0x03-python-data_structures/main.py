#!/usr/bin/python3
# 5-no_c.py
# no_c = __import__('5-no_c').no_c
#
# print(no_c("Best School"))
# print(no_c("Chicago"))
# print(no_c("C is fun!"))
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
