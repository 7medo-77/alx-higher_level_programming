#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda r: list(map(lambda x: x ** 2, matrix[r])), range(len(matrix)))))
