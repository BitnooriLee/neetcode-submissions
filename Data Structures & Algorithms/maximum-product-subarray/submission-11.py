class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    

        cur_min = cur_max = ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_min, cur_max = cur_max, cur_min
            cur_max = max(num, cur_max*num)
            cur_min = min(num, cur_min*num)
            ans = max(ans, cur_max)
        return ans