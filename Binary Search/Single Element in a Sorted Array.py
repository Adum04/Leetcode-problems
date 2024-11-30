def singleNonDuplicate(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1 or nums[0] != nums[1]:
        return nums[0]
    if nums[n - 2] != nums[n - 1]:
        return nums[n - 1]
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        elif nums[mid] == nums[mid - 1]:
            if mid % 2 == 0:
                high = mid - 2
            else:
                low = mid + 1
        elif nums[mid] == nums[mid + 1]:
            if mid % 2 == 0:
                low = mid + 2
            else:
                high = mid - 1
