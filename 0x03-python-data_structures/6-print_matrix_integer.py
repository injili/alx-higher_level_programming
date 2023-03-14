#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                print("{:d}".format(int(matrix[i][j])), end=" " if j < len(matrix[i]) - 1 else "\n")
    else:
        print("")
