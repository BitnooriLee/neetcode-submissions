class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = float("-inf"), float("-inf") 

        l,r = 0, len(height)-1 
        res = 0 
        while(l < r):
            left_max = max(left_max,height[l])
            right_max = max(right_max,height[r])
            if left_max < right_max:
                res += max(0, left_max-height[l])
                l += 1 
            else:
                res += max(0, right_max-height[r])
                r -= 1 

        return res 

                
                
        