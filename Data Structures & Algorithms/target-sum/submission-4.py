class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        output = 0 

        def dfs(i,cur):
            if i == len(nums):
                if cur == target:
                    return 1 
                else: return 0 
            return dfs(i+1, cur - nums[i]) + dfs(i+1, cur + nums[i])
    
        return dfs(0,0)