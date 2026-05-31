class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        nums.sort()

        def bt(i):
        
            output.append(path[:])
            prev = None
            for j in range(i, len(nums)):
                if prev == nums[j]:
                    continue
        
                path.append(nums[j])
                prev = nums[j]
                bt(j+1) 
                path.pop()

        bt(0)

        return output

        
      