class Solution:
    def trap(self, height: List[int]) -> int:
        # current 
        # output += max(0, min(max_l, max_r) - current)

        # -> max_l < max_r, current = height[l], l += 1, max_l update
        l,r = 0, len(height)-1
        max_l, max_r = height[l], height[r]
        output = 0
        
        while(l<r):
            if max_l < max_r:
                
                l += 1 #updated l 
                output += max(0, max_l - height[l])
                max_l = max(max_l, height[l])
                
                
            else: 
                r -= 1 
                output += max(0, max_r - height[r])
                max_r = max(max_r, height[r])
                
                
                
        return output



        