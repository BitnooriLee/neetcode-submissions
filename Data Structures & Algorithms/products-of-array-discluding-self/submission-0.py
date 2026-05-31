class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #using 2 array 
        pre = [1]*len(nums)
        pst = [1]*len(nums)



        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        for j in range(len(nums)-2, -1, -1):
            pst[j] = pst[j+1]*nums[j+1]

        output = []
        for k in range(len(nums)):
            output.append(pre[k]*pst[k])

        return output
        