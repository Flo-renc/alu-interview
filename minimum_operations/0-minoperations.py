#!/usr/bin/python3
"""
minoperations module
=====================

This module provides a function `minOperations` that calculates the minimum
number of operations required to generate exactly `n` 'H' characters in a
text file starting with a single 'H'. The only operations allowed are:

    1. Copy All
    2. Paste

    The solution is based on breaking down the problem using prime
    factorizationto ensure the least number of operations

    Functions:
        ----------
        - minOperations(n): Returns the minimum number of operations needed to
          achieve exactly `n` 'H' characters.
"""


def minOperations(n):
    if n <= 1:
        return 0
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
