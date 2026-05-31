class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tmp = set()
        for num in nums:
            if num in tmp:
                return num
            else:
                tmp.add(num)
        return -1         