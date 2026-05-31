class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        target = len(nums)-1
        current = target -1 

        while(current >= 0):
            if nums[current] >= (target - current):
                target = current 
            current -= 1 

        return target == 0

            
        