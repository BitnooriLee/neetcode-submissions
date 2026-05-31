class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        res = 0 
        stk = []
        for i in range(len(heights)):
            start = i 
            while stk and stk[-1][1]>= heights[i]:
                idx, h = stk.pop()
                res = max(res, (i - idx) * h)
                start = idx
            stk.append((start, heights[i]))
        return res 



        