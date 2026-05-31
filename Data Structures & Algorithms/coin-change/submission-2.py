class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #basecase? 
        
        coins.sort()
        dp = [float("inf")]*(amount+1) # 동전을 더할 수 없는 상태 
        dp[0] = 0 
 

        for i in range(1,amount+1):
            
            for coin in coins:
                if i - coin >=0: #음수가 되는경우 고려 
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float("inf") else -1

        
