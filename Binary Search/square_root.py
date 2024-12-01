def floorSqrt(self, n):
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid**2 == n:
            return mid
        if mid**2 > n:
            high = mid - 1
        else:
            low = mid + 1
    return high
