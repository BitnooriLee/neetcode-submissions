class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(path, i):
            if i == len(nums):
                output.append(path)
                return
            
            dfs(path+[nums[i]],i+1)
            dfs(path, i+1)

        dfs([],0)

        return output

        