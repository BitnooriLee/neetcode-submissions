class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        l,r = 0, n-1
        while(l<r):
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m #m을 업뎃이 아니라 r을 업뎃이다!!
            else:
                l = m+1

        return nums[l]

        
        