class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0 
        far, end = 0,0
        if len(nums) <=1:
            return 0 
        for i in range(len(nums)):
            far = max(far, nums[i]+i)
            if i == end:
                cnt+=1
                end = far 
            if end >= len(nums)-1:
                return cnt

        return -1 
        