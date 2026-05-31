class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []
        for i in range(l-2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            target = -nums[i]
            j,k = i+1, l-1
            while(j<k):
                if nums[j] + nums[k] == target:
                    res.append([nums[i],nums[j],nums[k]])
                    while(j+1 < l and nums[j] == nums[j+1] and k > j):
                        j+= 1
                    j+=1
                    while(k > 0 and nums[k] == nums[k-1] and k > j):
                        k -= 1
                    k-=1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j+= 1

        return res