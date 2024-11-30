def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    matrix = [i for row in matrix for i in row]
    ans = False
    for i in matrix:
        if i == target:
            ans = True
    return ans
