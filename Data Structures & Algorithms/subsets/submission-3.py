class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
    
        def backtrack(i):
            nonlocal res,path
            if i == len(nums):
                res.append(path[:])
                return

            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            backtrack(i+1)
            
        backtrack(0)

        return res


        