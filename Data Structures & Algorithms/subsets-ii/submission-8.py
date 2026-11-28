class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #안포함했으면 계속 안포함 
        nums.sort()
        output = []
        def bt(i,tmp):
            if i >= len(nums):
                output.append(tmp[:])
                return
            # i 포함
            tmp.append(nums[i])
            bt(i+1,tmp)
            tmp.pop()
            # i 안포함

            #  i-1 같으면 안들어갔으면 계속 안들어가기 
            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            bt(i+1,tmp)  

        bt(0,[])
        return output


