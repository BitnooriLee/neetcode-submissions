class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def maxi(start, end):
            pr1, pr2 = 0,0 
            for i in range(start,end):
                cur = max(pr1, pr2+nums[i])
                pr2 = pr1
                pr1 = cur 
            return pr1 
            
        return max(maxi(0,len(nums)-1), maxi(1,len(nums)))