def findMin(self, nums: List[int]) -> int:
    n = len(nums)
    low = 0
    high = n - 1
    minimum = float("inf")
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] < minimum:
            minimum = nums[mid]
        if nums[low] < minimum:
            minimum = nums[low]
        if nums[high] < minimum:
            minimum = nums[high]
        if nums[low] < nums[mid] > nums[low]:
            low = mid + 1
        else:
            high = mid - 1
    return minimum
