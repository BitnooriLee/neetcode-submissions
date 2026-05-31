class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        l = len(nums)
        visitied = [False]*l
        def bt():
            if len(tmp) == l:
                res.append(tmp[:])
                return 
            for i in range(l):
                if visitied[i]:
                    continue
                tmp.append(nums[i])
                visitied[i] = True
                bt()
                tmp.pop()
                visitied[i] = False


        bt()

        return res

        