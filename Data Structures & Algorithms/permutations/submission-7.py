class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        used = [False] * len(nums)
        def bt(tmp):
            if len(tmp) == len(nums):
                output.append(tmp[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                else:
                    tmp.append(nums[i])
                    used[i] = True
                    bt(tmp)
                    tmp.pop()
                    used[i] = False

        bt([])

        return output
        