class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        suf = [0] * n
        suf[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            suf[i] = max(suf[i+1], prices[i])
        max_profit = 0
        for i in range(n-1):
            max_profit = max(max_profit, suf[i+1] - prices[i])
        return max_profit
        