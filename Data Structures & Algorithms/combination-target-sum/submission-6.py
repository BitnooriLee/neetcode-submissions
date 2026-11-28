class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def bt(i, _target, tmp):
            if i >= len(nums) or _target < 0:
                return 
            if _target == 0:
                output.append(tmp[:])
                return
            tmp.append(nums[i])
            bt(i, _target - nums[i], tmp)
            tmp.pop()
            bt(i+1, _target, tmp) # 여기선 i를 안씀 
        
        bt(0,target,[])

        return output