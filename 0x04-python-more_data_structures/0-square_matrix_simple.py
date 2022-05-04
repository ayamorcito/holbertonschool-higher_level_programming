#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_reloaded = [list(map(lambda x: x * x, row)) for row in matrix]
    return matrix_reloaded
