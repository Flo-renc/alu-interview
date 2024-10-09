#!/usr/bin/python3
"""this function generates a pascals traingle """


def pascal_triangle(n):
    """
    generates pascal's triangle of height n 
    """
    if n <=0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1) #start with a row of 1's
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
