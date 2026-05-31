class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while(l<r):
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m # m 포함 
            else:
                l = m + 1 # m 포함 안됨 

        return nums[r]