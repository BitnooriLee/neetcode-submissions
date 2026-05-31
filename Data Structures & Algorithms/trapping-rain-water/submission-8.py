class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        res = 0 
        left_max, right_max = float("-inf"),float("-inf")
        while(l<r):
            if height[l] < height[r]: #오른쪽이 충분히 높다고 가정? 
                res += max(0,left_max-height[l])
                left_max = max(left_max,height[l])
                l+=1 
            else:
                res += max(0,right_max-height[r])
                right_max = max(right_max,height[r])
                r-=1 

        return res