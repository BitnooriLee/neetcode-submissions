class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        s1,e1 = intervals[0]
        output = []
        i = 1 
        while (i<len(intervals)):
            s2,e2 = intervals[i]
            if e1 < s2:
                output.append([s1,e1])
                s1,e1 = s2,e2
                i+= 1 
            else:
                s1,e1 = min(s1,s2), max(e1,e2)
                i+=1 
        output.append([s1,e1])

        return output