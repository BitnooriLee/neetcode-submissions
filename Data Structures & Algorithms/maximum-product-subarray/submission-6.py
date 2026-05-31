class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = cur_max = ans = nums[0]
        
        for n in nums[1:]:
            if n < 0:
                cur_min, cur_max = cur_max, cur_min
            cur_max = max(cur_max*n, n)
            cur_min = min(cur_min*n, n)
            ans = max(ans, cur_max)

        return ans
                
        