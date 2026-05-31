class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        s1,e1 = intervals[0][0], intervals[0][1]
        output = []
        for i in range(1,len(intervals)):
            s2,e2 = intervals[i][0], intervals[i][1]
            if e1 < s2:
                output.append([s1,e1])
                s1,e1 = s2,e2
            else:
                s1 = min(s1,s2)
                e1 = max(e1,e2)

        output.append([s1,e1])
        return output
            

        