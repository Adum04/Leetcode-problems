def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
    new_grid = [i for row in grid for i in row]
    n = len(new_grid)
    ans = []
    res = []
    for i in new_grid:
        if i not in ans:
            ans.append(i)
        else:
            res.append(i)
    for i in range(1, n + 1):
        if i not in new_grid:
            res.append(i)
    return res
