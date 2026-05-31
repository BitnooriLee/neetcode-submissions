class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [] 
        maxArea = 0
        for cur_i, cur_h in enumerate(heights):
            start = cur_i
            while stk and stk[-1][1] > cur_h:
                index, height = stk.pop()
                maxArea = max(maxArea, height * (cur_i - index))
                start = index
            stk.append((start, cur_h))
        
        for i, h in stk:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
