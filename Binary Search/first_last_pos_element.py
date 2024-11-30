def BSL(self, nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            index = mid
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return index


def BSR(self, nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    index = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            index = mid
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return index


def searchRange(self, nums: List[int], target: int) -> List[int]:
    ext_le = self.BSL(nums, target)
    ext_ri = self.BSR(nums, target)
    return [ext_le, ext_ri]
