class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        left = [1] * len(nums)
        right = [1] * len(nums)
        # 왼쪽 곱 
        for i in range(len(nums)-1):
            left[i+1] = left[i]*nums[i]

        # 오른쪽 곱 
        for j in range(len(nums)-2,-1,-1):
            right[j] = right[j+1]*nums[j+1]

        for i in range(len(nums)):
            output.append(left[i]*right[i])
            
        return output
            
