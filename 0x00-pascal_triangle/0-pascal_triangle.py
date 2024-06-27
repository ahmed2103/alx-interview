#!/usr/bin/python3
"""module contains a function that returns a list of lists of integers"""


def pascal_triangle(n):
    """Returns Pascal's triangle up to n rows"""
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1] + [triangle[i - 1][j - 1] + triangle[i - 1][j]
                     for j in range(1, i)] + [1]
        triangle.append(row)

    return triangle
