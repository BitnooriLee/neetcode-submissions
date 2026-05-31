class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            if target - nums[i] in dic:
                ans = sorted([i,dic[target - nums[i]]])
                return ans
            else:
                dic[nums[i]] = i 

        return [-1,-1]
        
        