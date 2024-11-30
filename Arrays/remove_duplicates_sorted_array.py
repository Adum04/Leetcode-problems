def removeDuplicates(self, nums: List[int]) -> int:
    if not nums:
        return 0
    li = []
    for i in nums:
        if i not in li:
            li.append(i)
    nums[:] = li
    return len(nums)
