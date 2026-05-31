class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        if l < 3:
            return []
        nums.sort()
        res = []
        for i in range(l-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            j,k = i+1, l-1
            target = -nums[i]
            while(j<k):
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1 
                    k-=1 
                    while j<k and nums[j-1] == nums[j]:
                        j+=1 
                    
                    while j<k and nums[k+1] == nums[k]:
                        k-=1 
                elif nums[j] + nums[k] > target:
                    k -=1 
                else:
                    j+=1 
        
        return res 