class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0 
        nums.sort()
        res = []
        while (i<len(nums)-2):
            while(i > 0 and i<len(nums)-2 and nums[i] == nums[i-1]):
                i+=1
            target = -nums[i]
            j = i+1 
            k = len(nums)-1
            while(j<k):
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1 
                    k -= 1
                    while(j<k and nums[j] == nums[j-1]):
                        j += 1 
                    while(j<k and nums[k] == nums[k+1]):
                        k -= 1 
                elif nums[j] + nums[k] < target:
                    j += 1 
                else:
                    k -= 1 
            i+=1 
        return res