class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0 
        stk = []
        for i,h in enumerate(heights):
            start = i
            while stk and stk[-1][1] > h:
                idx, height = stk.pop()
                res = max(res, height*(i - idx))
                start = idx
            stk.append((start, h))

        for idx, height in stk:
            res = max(res, height*(len(heights)-idx))
                
        return res

        