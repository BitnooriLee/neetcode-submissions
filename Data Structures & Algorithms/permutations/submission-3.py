class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l = len(nums)
        output = []
        res = []
        def bt(i,arr):
            if i == l:
                output.append(res[:])
                return

            for j in range(len(arr)):
                res.append(arr[j])
                newarr = []
                for k in range(len(arr)):
                    if j != k:
                        newarr.append(arr[k])
                bt(i+1,newarr)
                res.pop()

        bt(0,nums)
        return output