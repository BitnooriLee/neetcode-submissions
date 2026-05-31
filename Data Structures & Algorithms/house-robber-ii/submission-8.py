class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        def maxi(start,end):
            prev2 = 0
            prev1 = 0

            for i in range(start,end):
                cur = max(prev1, prev2+nums[i])
                prev2 = prev1
                prev1 = cur 

            return prev1
        return max(maxi(1,len(nums)), maxi(0,len(nums)-1))