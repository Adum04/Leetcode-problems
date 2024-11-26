def rearrangeArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    pos = 0
    neg = 1
    new = [0] * n
    for i in range(n):
        if nums[i] > 0:
            new[pos] = nums[i]
            pos += 2
        else:
            new[neg] = nums[i]
            neg += 2
    return new
