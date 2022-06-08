#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y ** 2, x)), matrix))

if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    new_matrix = square_matrix_simple(matrix)
    print(new_matrix)
    print(matrix)#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix is not None:

        new = []

        for rows in matrix:

            new.append(list(map(lambda x: x**2, rows)))

        return (new)

    return None

# return[[elem**2 in row] for row in matrix]

# return(list(map(lambda x: x**2, list)) for list in matrix)
