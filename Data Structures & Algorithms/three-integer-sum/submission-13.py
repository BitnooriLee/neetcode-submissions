class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n-2): # n-3 
            l,r = i+1, n-1 
            if i >0 and nums[i] == nums[i-1]:
                continue
            #target = -nums[i]
            
            while(l<r):
                s = nums[l]+nums[r]
                if s == -nums[i]:
                    output.append([nums[i],nums[l],nums[r]])
                    while(l<r and nums[l] == nums[l+1]):
                        l+=1
                    while(l<r and nums[r] == nums[r-1]):
                        r-=1

                    l+=1
                    r-=1
                elif s < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return output 
        

#O(n^2)
#O(m) output list. O(1) or O(n) depending on sorting algo 
        