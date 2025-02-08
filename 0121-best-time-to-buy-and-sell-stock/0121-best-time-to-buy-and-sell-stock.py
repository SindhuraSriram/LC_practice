class Solution:
    def maxProfit(self, prices):
        maximum_profit = 0
        lowest_price = prices[0]
        
        for day in range(len(prices)):
            lowest_price = min(prices[day], lowest_price)
            price_difference = prices[day] - lowest_price
            maximum_profit = max(price_difference, maximum_profit)
        
        return maximum_profit