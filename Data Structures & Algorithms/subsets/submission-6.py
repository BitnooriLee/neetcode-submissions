class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        tmp = []
        def backtrack(i):
            if i == len(nums):
                res.append(tmp[:])
                return 
            backtrack(i+1)
            tmp.append(nums[i])
            backtrack(i+1)
            tmp.pop()

        backtrack(0)

        return res 
        