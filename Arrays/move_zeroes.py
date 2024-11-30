def moveZeroes(self, nums: List[int]) -> None:
    # if len(nums) == 1:
    #     return nums
    n = len(nums)
    n_z = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[n_z] = nums[n_z], nums[i]
            n_z += 1
