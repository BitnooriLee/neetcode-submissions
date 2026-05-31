class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = {} #idx, total 정수갯수 

        def dfs(i, total):
            if i == l:
                return 1 if total == target else 0
            if (i,total) in dp:
                return dp[(i,total)]
            ways = dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])
            dp[(i,total)] = ways
            return ways
        

        return dfs(0,0)