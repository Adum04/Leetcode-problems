def peakIndexInMountainArray(self, arr: List[int]) -> int:
    n = len(arr)
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid - 1] > arr[mid]:
            high = mid
        else:
            low = mid + 1
