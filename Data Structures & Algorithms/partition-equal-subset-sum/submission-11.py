class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        if sum(nums)%2 != 0: 
            return False

        target = sum(nums)//2 

        #BF 
        s = {0}
        for i in range(len(nums)):
            tmp = set()
            for cur in s:
                nxt = cur + nums[i]
                if nxt == target:
                    return True
                if nxt < target:
                    tmp.add(nxt)
            s = s.union(tmp)

        return target in s
            
        