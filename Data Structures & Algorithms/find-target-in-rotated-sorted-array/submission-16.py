class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0 
            else: -1 

        l,r = 0, len(nums)-1

        while(l<=r):
            m = l + (r-l)//2
            
            if target == nums[m]:
                return m 
            if  nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1 
                else:
                    r = m - 1
            else:
                if nums[l] <= target < nums[m]:
                    r = m -1 
                else:
                    l = m +1
    


        return -1 
                
        