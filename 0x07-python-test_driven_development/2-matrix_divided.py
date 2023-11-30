#!/usr/bin/python3

"""Matrix Division Function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix: A list of lists containing integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: Matrix contains non-numeric elements.
        TypeError: Matrix contains rows of unequal sizes.
        TypeError: div is not an integer or float.
        ZeroDivisionError: div = 0.

    Returns:
        Matrix (list) representing the result of the division.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(e, (int, float))
                    for e in [num for row in matrix for num in row])):
        raise TypeError(
            "matrix must be a matrix (list of lists) of "
            "integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
