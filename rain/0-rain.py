#!/usr/bin/python3
"""
0-rain Module

This module provides a function that calculates how much rainwater will
beretained between walls of varying heights, represented as a list of non-negative integers.

Each integer in the list corresponds to the height of a wall, and the amount of rainwater
retained is calculated based on how water would accumulate between the walls after a rainfall.

Function:
        rain(walls): Calculates the total amount of water retained between walls after it rains.
"""


def rain(walls):
    """
        Calculate how much water will be retained after it rains.
        walls: list of non-negative integers representing the heights of walls
        Return: integer indicating total amount of rainwater retained
    """

    if not walls or len(walls) < 3:
        return 0

    left_max, right_max = 0, 0
    left, right = 0, len(walls) - 1
    total_retention = 0

    while left <= right:
        if walls[left] <= walls[right]:
            if walls[left] >= left_max:
                left_max = walls[left]
            else:
                total_retention += left_max - walls[left]
            left += 1
        else:
            if walls[right] >= right_max:
                right_max = walls[right]
            else:
                total_retention += right_max - walls[right]
            right -= 1

    return total_retention
