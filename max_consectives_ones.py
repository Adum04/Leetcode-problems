def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    n = len(nums)
    maxi = 0
    curr = 0
    for i in nums:
        if i == 1:
            curr += 1
        else:
            maxi = max(curr, maxi)
            curr = 0

    maxi = max(maxi, curr)
    return maxi
