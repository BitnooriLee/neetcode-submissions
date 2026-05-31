class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        visited = [False]*len(nums)
        def bt():
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                path.append(nums[i])
                bt()
                path.pop()
                visited[i] = False
            
        bt()

        return res