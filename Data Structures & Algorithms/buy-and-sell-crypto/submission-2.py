class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        stock = 0
        for i in range(1, len(prices)):
            if prices[stock] < prices[i]:
                profit = prices[i] - prices[stock]
                max_profit = max(max_profit, profit)
            else:
                stock = i
                
            
        return max_profit

        