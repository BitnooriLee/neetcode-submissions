class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        n1 = nums[1:]
        n2 = nums[:len(nums)-1]

        def maxi(n):
            prev2 = n[0]
            prev1 = max(n[0],n[1])

            for i in range(2,len(n)):
                cur = max(prev1, prev2+n[i])
                prev2 = prev1
                prev1 = cur 

            return prev1
        return max(maxi(n1), maxi(n2))