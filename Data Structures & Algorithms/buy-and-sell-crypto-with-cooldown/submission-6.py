class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #caching O(2^n) -> O(n)
        # state -> buying / selling
        # If buy -> i+1
        # If sell -> i+2 
        dp = {} # key= (i, buying), val = max_profit 

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i,buying)] # max profix stored 
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i, buying)] = max(buy, cooldown) #caching
            else: 
                sell = dfs(i+2, not buying) + prices[i]
                cooldonw = dfs(i+1, buying)
                dp[(i, buying)] = max(sell, cooldonw)
            return dp[(i,buying)]
        return dfs(0, True)
        