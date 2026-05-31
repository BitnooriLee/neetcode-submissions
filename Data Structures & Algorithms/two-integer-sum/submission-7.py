from collections import defaultdict 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict()

        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]],i]
            else:
                dic[nums[i]] = i 
        
        return [0,0]
        