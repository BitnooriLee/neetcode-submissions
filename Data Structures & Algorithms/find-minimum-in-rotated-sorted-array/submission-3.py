class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l,r = 0, len(nums)-1
        while(l<r): # l==r 이면 이때가 최소값임 
            m = l + (r-l)//2 
            if nums[m] > nums[r]:
                l = m + 1 
            else:
                r = m 
                #m 자체가 최소값이 될 수 있음 

        return nums[l]