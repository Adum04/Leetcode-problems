def majorityElement(self, nums: List[int]) -> int:
    n = len(nums)
    candidate = nums[0]
    count = 0
    for i in range(0, n):
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = nums[i]
            count = 1
    return candidate
