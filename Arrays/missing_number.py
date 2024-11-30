def missingNumber(self, nums: List[int]) -> int:
    lst = {}
    n = len(nums)
    for i in range(0, n + 1):
        lst[i] = 0
    for i in nums:
        lst[i] += 1
    for k, v in lst.items():
        if v == 0:
            return k
