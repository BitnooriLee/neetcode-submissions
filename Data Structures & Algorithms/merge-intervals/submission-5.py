class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) ==1:
            return intervals
        output = []
        intervals.sort()
        pre_s, pre_e = intervals[0]
        for s,e in intervals[1:]:
            if pre_e < s:
                output.append([pre_s, pre_e])
                pre_s, pre_e = s,e
            else:
                pre_e = max(pre_e, e)

        output.append([pre_s, pre_e])

        return output