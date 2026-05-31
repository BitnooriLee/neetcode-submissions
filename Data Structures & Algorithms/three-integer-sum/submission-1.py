class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) 
        result = []
        for i in range(n-1):
            target = -nums[i]
            l,r = i+1, n-1
            while(l<r):
                if (nums[l] + nums[r]) == target:
                    #no duplicate 
                    if [nums[i],nums[l],nums[r]] not in result:
                        result.append([nums[i],nums[l],nums[r]])
                    l += 1
                elif (nums[l] + nums[r]) > target:
                    r -= 1
                else:
                    l += 1  
        return result

 
        