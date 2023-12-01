#!/usr/bin/python3
"""
Module to perform lazy matrix multiplication using NumPy.
"""


import numpy as numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        np.ndarray: Resulting matrix.
    """

    return (numpy.matmul(m_a, m_b))
