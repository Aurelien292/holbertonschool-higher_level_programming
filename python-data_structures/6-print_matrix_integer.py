def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{}".format(number)for number in row))
