class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return 0
        far,end = 0,0
        cnt = 0 
        for i in range(l):
            far = max(far, nums[i]+i)
            if i == end:
                cnt+=1
                end =far
            if end >= l-1:
                return cnt 
        return -1
                
        
        