class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(path,res):
            if len(path) == len(nums):
                output.append(path)
            for i in range(len(res)):
                dfs(path+[res[i]], res[:i]+res[i+1:])
    

        dfs([],nums)

        return output