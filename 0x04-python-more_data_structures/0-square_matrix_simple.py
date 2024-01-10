#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    length = len(matrix) - 1
    cpy = matrix.copy()

    i = 0
    while (i <= length):
        cpy[i] = list(map(lambda x: x ** 2, cpy[i]))
        i += 1
    return (cpy)
