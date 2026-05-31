class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def dfs(path,remain):
            if len(remain) == 0:
                output.append(path)
                return 

            for i in range(len(remain)):
                dfs(path + [remain[i]], remain[:i] + remain[i+1:])
    
        dfs([],nums)

        return output
        