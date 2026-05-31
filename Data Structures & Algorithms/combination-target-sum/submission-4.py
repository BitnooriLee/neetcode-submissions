class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        tmp = [] 
        l = len(nums)
        def bt(i,remain):
            if i >= l or remain < 0:
                return 
            if remain == 0:
                output.append(tmp[:])
                return
            tmp.append(nums[i])
            bt(i, remain - nums[i])
            tmp.pop()
            bt(i+1, remain)

        bt(0, target)

        return output