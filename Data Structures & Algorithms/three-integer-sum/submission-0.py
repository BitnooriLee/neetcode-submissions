class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)-1):
            if i >0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            
            while(j<k):
                cur = nums[j]+nums[k]
                if target == cur:
                    output.append([nums[i],nums[j],nums[k]])
                    while j<k and (nums[j] == nums[j+1]):
                        j +=1
                    while j<k and (nums[k] == nums[k-1]):
                        k -=1
                    j+=1 
                    k-=1 
                elif target < cur:
                    k -= 1
                else:
                    j += 1
        
        return output
