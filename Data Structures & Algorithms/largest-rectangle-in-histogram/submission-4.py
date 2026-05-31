class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stk = []
        res = 0
        for i,h in enumerate(heights):
            start = i 
            while (stk and stk[-1][0]>= h):
                prev_h, prev_i = stk.pop()
                res = max(res, prev_h*(i - prev_i))
                start = prev_i
            stk.append((h,start))

        return res


        