class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        mp = set()
        for n in nums:
            if n in mp:
                return True
            mp.add(n)

        return False


        