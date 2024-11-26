def check(self, nums: List[int]) -> bool:
    rotation = 0
    n = len(nums)
    for i in range(0, n):
        if nums[i] > nums[(i + 1) % n]:
            rotation += 1
        if rotation > 1:
            return False
    return True
