class Solution:
    def jump(self, nums: List[int]) -> int:
        far,end = 0,0 #다음 점프로 갈 수 있는 최대 vs 이번에 갈 수 있는 마지막 
        jump = 0 

        if len(nums) <=1:
            return 0

        for i in range(len(nums)):
            far = max(far, i+ nums[i])
            if i == end:
                jump+=1 
                end = far 
            if end >= len(nums)-1:
                return jump       

        return -1   