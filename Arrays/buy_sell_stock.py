def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    maxi = 0
    mini = prices[0]
    for i in range(0, n):
        mini = min(mini, prices[i])
        maxi = max(maxi, prices[i] - mini)
    return maxi
