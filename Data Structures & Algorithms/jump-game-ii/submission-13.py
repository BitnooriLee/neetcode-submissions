class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0 
        cnt = 0 
        cur_far = 0 
        next_far = 0

        for i in range(len(nums)):
            next_far = max(next_far, i + nums[i])
            if i == cur_far:
                cur_far = next_far
                cnt += 1 
            if cur_far >= len(nums)-1:
                return cnt

        return -1 

        