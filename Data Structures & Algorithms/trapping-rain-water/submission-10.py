class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0 
        l,r = 0, len(height)-1
        left_max, right_max = float("-inf"),float("-inf")
        while(l<r):
            left_max = max(height[l],left_max)
            right_max = max(height[r],right_max)
            if height[l] < height[r]:
                res += max(0, min(left_max, right_max) - height[l])
                l += 1 
            else: 
                res += max(0, min(left_max, right_max) - height[r])
                r -= 1 

        return res
            
            
        