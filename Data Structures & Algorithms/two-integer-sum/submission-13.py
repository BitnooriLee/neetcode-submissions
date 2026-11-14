class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = defaultdict(int)

        for i in range(len(nums)):
            if target - nums[i] in dic and dic[target - nums[i]]!= i:
                    return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i

        return [-1,-1]

                    
                
            
        


        