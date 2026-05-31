class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output =[]
        res = []
        l = len(nums)
        def bt(start):
            output.append(res[:])

            prev = None
            for i in range(start,l):
                if prev == nums[i]:
                    continue
                res.append(nums[i])
                prev = nums[i]
                bt(i+1)
                res.pop()
        bt(0)

        return output
        