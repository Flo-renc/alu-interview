#!/usr/bin/python3
def rain(walls):
    """
        Calculate how much water will be retained after it rains.
        walls: list of non-negative integers representing the heights of walls
        Return: integer indicating total amount of rainwater retained
    """

    if not walls:
        return 0

    n = len(walls)
    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = walls[0]
    for i in range(1, n):
        leftMax[1] = max(leftMax[i-1], walls[1])

    rightMax[n-1] = walls[n-1]
    for i in range(n -2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], walls[i])

    total_retention = 0
    for i in range(n):
        total_retention += min(leftMax[i], rightMax[i] - walls[i])


    return total_retention
