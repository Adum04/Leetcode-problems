def bdays(bloomday, m, k, days):
    total_blooms = 0
    count = 0
    n = len(bloomday)
    for i in range(n):
        if bloomday[i] <= days:
            count += 1
            if count == k:
                total_blooms += 1
                count = 0
        else:
            count = 0
    return total_blooms >= m


def mindays(bloomday, m, k):
    low = min(bloomday)
    high = max(bloomday)
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        possiblity = bdays(bloomday, m, k, mid)
        if possiblity:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans


bloomday = [1, 10, 3, 10, 2]
m = 3
k = 1
print(mindays(bloomday, m, k))
