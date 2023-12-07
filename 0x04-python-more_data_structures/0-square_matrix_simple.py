#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idx1, col in enumerate(row):
            new_matrix[idx][idx1] = row[idx1] ** 2
    return new_matrix
