dp = []
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = defaultdict(lambda : -1)
        def cost(i,n,bought):
            if i >= n:
                return 0
            if (i, bought) in dp:
                return dp[(i, bought)]
            #if bought previously, we have 2 option:-
            # sell the prvious stock today or skip this day
            if bought:
                dp[(i,bought)] = max(cost(i+1,n,False) + prices[i] - fee, cost(i+1,n,bought))
            
            #else if we can buy a new stock, then we again have 2 option:-
            #buy the current stock or skip over it
            else:
                dp[(i,bought)] = max(cost(i+1,n,True) - prices[i], cost(i+1,n,bought))
                
            return dp[(i,bought)]
        
        return cost(0,len(prices),False)        