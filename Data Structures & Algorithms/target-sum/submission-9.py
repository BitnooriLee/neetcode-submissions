class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0 
        def dfs(i, s):
            nonlocal res
            if i >= len(nums):
                if s == target:
                    res += 1 
                    return
                else: return 
            dfs(i+1, s+nums[i])
            dfs(i+1, s-nums[i])
    
        dfs(0,0)

        return res 
                    
        