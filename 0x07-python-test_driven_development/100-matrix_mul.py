#!/usr/bin/python3
"""
Matrix multiplication - only Matrix product (two matrices)
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list of lists, or if an element
        is not an int or float.
        ValueError: If m_a or m_b is empty, or if the matrices can't be
        multiplied.
    """
    # Check if m_a is empty or a matrix with only one row and one column
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    # Check if m_b is empty or a matrix with only one row and one column
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # Check if m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Check if m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # Check if m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a contains only integers or floats
    if not all(isinstance(e, (int, float)) for row in m_a for e in row):
        raise TypeError("m_a should contain only integers or floats")

    # Check if m_b contains only integers or floats
    if not all(isinstance(e, (int, float)) for row in m_b for e in row):
        raise TypeError("m_b should contain only integers or floats")

    # Check if each row of m_a has the same size
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")

    # Check if each row of m_b has the same size
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose matrix b
    transposed_b = []
    for r in range(len(m_b[0])):
        new_row = []
        for c in range(len(m_b)):
            new_row.append(m_b[c][r])
        transposed_b.append(new_row)

    # Multiply matrices
    result = []
    for row in m_a:
        new_row = []
        for col in transposed_b:
            prod = 0
            for i in range(len(transposed_b[0])):
                prod += row[i] * col[i]
            new_row.append(prod)
        result.append(new_row)

    return result
