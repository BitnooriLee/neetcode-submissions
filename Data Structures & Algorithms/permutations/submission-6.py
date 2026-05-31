class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        visited = [False]*len(nums)
        def bt():
            if len(path) == len(nums):
                output.append(path[:])
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

        return output
            
        