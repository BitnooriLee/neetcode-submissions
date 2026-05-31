class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 :
            return 0 

        dp = [float("inf")]*(amount+1)
        dp[0] = 1 
        for coin in coins:
            if amount >= coin:
                dp[coin] = 1 

        for i in range(amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[-1] if dp[-1] != float("inf") else -1