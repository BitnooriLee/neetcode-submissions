class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True 

        res = 0 
        for i in range(len(nums)):
            if res < i:
                return False
            res = max(res, i+nums[i])

        return res >= len(nums)-1

          
        