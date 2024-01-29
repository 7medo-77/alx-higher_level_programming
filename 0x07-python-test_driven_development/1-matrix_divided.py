#!/usr/bin/python3
"""
Function to divide matrix
"""


def matrix_divided(matrix, div):
    index = 0
    new_matrix = matrix.copy()
    for list_ in new_matrix:
        for number in list_:
            if not isinstance(number, (float, int)):
                raise TypeError("matrix must be a "
                                "matrix (list of lists) of integers/floats")
            elif len(list_) != len(new_matrix[index - 1]) and index != 0:
                raise TypeError("Each row of the matrix "
                                "must be the same size")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            elif not matrix:
                raise TypeError("matrix_divided() missing "
                                "1 required positional argument: 'matrix'")
            elif not div:
                raise TypeError("matrix_divided() missing 1 "
                                "required positional argument: 'div'")
            else:
                number /= div
                number = round(number, 2)
        index += 1
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/1-matrix_divided.txt")
