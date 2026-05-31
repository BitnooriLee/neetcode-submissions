class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk = []
        res = 0 
        for i in range(len(heights)):
            start = i
            while stk and stk[-1][1] >= heights[i]:
                pre_idx, pre_h = stk.pop()
                res = max(res, (i-pre_idx)*pre_h)
                start = pre_idx 
            stk.append((start,heights[i]))

        return res

        