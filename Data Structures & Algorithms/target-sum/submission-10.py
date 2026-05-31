class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        def backtrack(i, s):

            if i >= len(nums):
                if s == target:
                    return 1 
                else: return 0
            return (backtrack(i+1, s+nums[i]) + backtrack(i+1, s-nums[i]))
    

        return backtrack(0,0)
                    
        