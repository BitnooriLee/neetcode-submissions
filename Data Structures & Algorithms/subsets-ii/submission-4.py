class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def bt(start):
            res.append(path[:])
            
            prev = None
            for i in range(start,len(nums)):
                if prev == nums[i]:
                    continue
                path.append(nums[i])
                prev = nums[i]
                bt(i+1)
                path.pop()
                
        bt(0)

        return res
        