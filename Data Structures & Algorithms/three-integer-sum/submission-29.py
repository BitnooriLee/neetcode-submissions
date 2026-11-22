class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0 
        while(i < len(nums)):
            while(i > 0 and i+1 < len(nums) and nums[i-1] == nums[i]):
                i += 1
            target = -nums[i]
            j,k = i+1,len(nums)-1
            while(j<k):
                if nums[j] + nums[k] == target:
                    output.append([nums[i],nums[j],nums[k]])
                    while(k-1 > j and nums[k] == nums[k-1]):
                        k-=1
                    k-=1
                    while(j+1 < k and nums[j] == nums[j+1]):
                        j+=1
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:

                    j+=1
            i+=1
        return output

            
        