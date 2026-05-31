class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i,remain):
            if i == len(nums) and remain == 0:
                return 1 
            if i == len(nums) and remain != 0:
                return 0
            
            if (i,remain) in dp:
                return dp[(i,remain)]
            
            way = dfs(i+1, remain+nums[i]) + dfs(i+1, remain-nums[i])
            dp[(i,remain)] = way
            return way 
        
        return dfs(0,target)