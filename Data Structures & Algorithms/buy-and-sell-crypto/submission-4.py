class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0 
        for sell in range(1,len(prices)):
            buy = 0 
            while(buy < sell):
                if prices[sell] > prices[buy]:
                    profit = max(profit, prices[sell] - prices[buy])
                buy += 1 

        return profit
            
                
            
        