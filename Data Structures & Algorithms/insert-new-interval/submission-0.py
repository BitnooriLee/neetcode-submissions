class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        s2,e2 = newInterval[0], newInterval[1]
        i = 0 
        while(i<len(intervals)):
            s1,e1 = intervals[i][0], intervals[i][1]
            if e2 < s1:
                output.append([s2,e2])
                return output + intervals[i:]
            elif e1 < s2:
                output.append([s1,e1])
            else:
                s2 = min(s1,s2)
                e2 = max(e1,e2)
            i += 1 
        output.append([s2,e2])

        return output
             




        