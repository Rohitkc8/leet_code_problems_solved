class Solution:
    def maxProfit(self,prices: List[int]) -> int:
        max_profit=0
        min_=prices[0]
        nax_=0
        for i in range(1,len(prices)):
            min_=min(prices[i],min_)
            max_=max(prices[i],min_)
            max_profit=max(max_profit,max_-min_)
        return max_profit

            
