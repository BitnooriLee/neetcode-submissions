class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n-2):
            target = -nums[i]
            if i > 0 and nums[i-1] == nums[i]:
                continue #i dup remove 
            l,r = i+1, n-1 
            while(l<r):
                s = nums[l] + nums[r] 
                if s == target:
                    result.append([nums[i],nums[l],nums[r]])
                    l += 1 
                    r -= 1 
                    while r >= 0 and nums[r] == nums[r+1]:
                        r -=1 
                    while l+1 < n-1 and nums[l] == nums[l-1]:
                        l +=1 
                elif s > target:
                    r-=1
                else:
                    l+=1


        return result
       