def maxSubArray(self, nums: List[int]) -> int:
    maxi = float("-inf")
    sum = 0
    n = len(nums)
    for i in range(0, n):
        sum += nums[i]
        if sum > maxi:
            maxi = sum
        if sum < 0:
            sum = 0
    return maxi
