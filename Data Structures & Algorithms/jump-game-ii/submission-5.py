class Solution:
    def jump(self, nums: List[int]) -> int:
        far = 0 
        end = 0 
        jump = 0 
        if len(nums)<= 1:
            return 0

        for i in range(len(nums)):
            far = max(far, i+nums[i])
            if i == end:
                jump+= 1
                end = far
            if end >= len(nums)-1:
                return jump 
            
            
        return -1


        
        