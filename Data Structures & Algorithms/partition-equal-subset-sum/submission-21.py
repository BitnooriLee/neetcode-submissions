class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2 != 0:
            return False
        if len(nums) == 1:
            return False
        target = total//2 

        dp = [False] * (target+1)
        dp[0] = True

        for n in nums:
            for t in range(target, n-1, -1): # n까지 
                dp[t] = dp[t] or dp[t-n]
            if dp[target]:
                return True
        return dp[target]
            


        