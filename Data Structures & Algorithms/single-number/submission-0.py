class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #no sort, no dic 
        tmp = set()

        for num in nums:
            if num in tmp:
                tmp.remove(num)
            else:
                tmp.add(num)
        output = tmp.pop()
        return output
                
        