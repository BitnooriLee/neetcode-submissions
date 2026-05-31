class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights.append(0)

        l= len(heights)
        stk = [(0,heights[0])]
        for i in range(1,l):
            start = i
            while(stk and stk[-1][1] > heights[i]): #같은경우 중복으로 더해짐? 
                j,h = stk.pop()
                res = max(res, h*(i-j))
                start = j
            stk.append((start,heights[i])) #계속 왼쪽으로 들어가야함 
        return res


            

        