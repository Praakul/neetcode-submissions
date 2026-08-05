class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            if prices[i] > lowest:
                profit = prices[i] - lowest
                if max_profit < profit:
                    max_profit = profit
            else:
                lowest = prices[i]
        return max_profit
             
            
