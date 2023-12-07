#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [row[:] for row in matrix]
    for idx, row in enumerate(new_matrix):
        for idx1, col in enumerate(row):
            new_matrix[idx][idx2] = row[idx2] ** 2
    return new_matrix
