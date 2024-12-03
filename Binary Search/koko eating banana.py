# Brute force solution
import math


def total_hours(piles, hourly):
    total = 0
    for i in range(len(piles)):
        total = total + math.ceil(piles[i] / hourly)
    return total


def mineating(piles, hourly):
    low = 1
    high = max(piles)
    for i in range(low, high + 1):
        th = total_hours(piles, i)
        if th <= hourly:
            return i


#  optimal solution


def total_hours(piles, hourly):
    total = 0
    n = len(piles)
    for i in range(n):
        total = total + math.ceil(piles[i] / hourly)
    return total


def mineating(piles, hourly):
    low = 1
    high = max(piles)
    while low <= high:
        mid = (low + high) // 2
        if total_hours(piles, mid) <= hourly:
            high = mid - 1
        else:
            low = mid + 1
    return low


print(mineating(piles, hourly))
