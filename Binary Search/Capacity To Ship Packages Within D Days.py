def finddays(cap, weights):
    n = len(weights)
    load = 0
    days = 1
    for i in range(n):
        if load + weights[i] > cap:
            days += 1
            load = weights[i]
        else:
            load = load + weights[i]
    return days


def shipdays(weights, days):
    n = len(weights)
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        fd = finddays(mid, weights)
        if fd <= days:
            high = mid - 1
        else:
            low = mid + 1
    return low


weights = [1, 2, 3, 1, 1]
days = 4
print(shipdays(weights, days))
