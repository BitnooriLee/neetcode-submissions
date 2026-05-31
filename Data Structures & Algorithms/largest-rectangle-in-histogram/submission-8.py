class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)

        res = 0 
        stk = [] # (idx, h)

        for i, h in enumerate(heights):
            start = i 
            while stk and stk[-1][1] >= heights[i]:
                idx, height = stk.pop()
                res = max(res, (i-idx)*height)
                start = idx
            stk.append((start, h))
        
        return res 




        