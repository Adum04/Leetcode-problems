import math


def thresh(nums, threshold, value):
    n = len(nums)
    total = 0
    for i in range(n):
        total += math.ceil(nums[i] / value)
    return total <= threshold


def smallestdivisor(nums, threshold):
    n = len(nums)
    low = 1
    high = max(nums)
    ans = high

    while low <= high:
        mid = (low + high) // 2
        th = thresh(nums, threshold, mid)
        if th:
            ans = mid
            high = mid - 1
        else:

            low = mid + 1
    return ans


nums = [44, 22, 33, 11, 1]
threshold = 5
print(smallestdivisor(nums, threshold))
