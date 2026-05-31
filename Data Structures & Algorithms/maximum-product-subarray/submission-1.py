class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMin, curMax = 1,1 
    
        for n in nums:
            tmp = curMax 
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(tmp*n, curMin*n, n)
            res =max(res, curMax)
        return res


        