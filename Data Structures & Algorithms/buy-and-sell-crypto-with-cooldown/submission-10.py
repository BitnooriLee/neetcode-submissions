class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        
        def dfs(buying,i):
            if i >= len(prices):
                return 0
            if (buying,i) in dp:
                return dp[(buying,i)]
            if buying:
                buy = dfs(not buying,i+1) - prices[i]
                cooldown = dfs(buying,i+1)
                dp[(buying,i)] = max(buy, cooldown)
            if not buying:
                sell = dfs(not buying, i+2) + prices[i]
                cooldown = dfs(buying,i+1)
                dp[(buying,i)] = max(sell, cooldown)
            return dp[(buying,i)]
            

            



        

        return dfs(True, 0)
        