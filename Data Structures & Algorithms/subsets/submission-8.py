class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []

        def bt(i,tmp):
            if i >= len(nums):
                output.append(tmp[:]) #복사본
                return      
            bt(i+1,tmp)
            tmp.append(nums[i])
            bt(i+1,tmp)
            tmp.pop()
        bt(0,[])
        return output 
            


        