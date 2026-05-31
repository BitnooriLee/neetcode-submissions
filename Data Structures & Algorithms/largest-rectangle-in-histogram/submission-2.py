class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0,heights[0]]]
        maxArea = heights[0]

        for i in range(1, len(heights)):
            start = i 
            while(stack and stack[-1][1] > heights[i]):
                idx, h = stack.pop()
                maxArea = max(maxArea, (i-idx)*h)
                start = idx
            stack.append([start, heights[i]])
        for i,h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))

        return maxArea
        