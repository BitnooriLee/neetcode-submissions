class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dic = defaultdict(int)
        sorted_intervals = sorted(intervals, key=lambda interval: interval[1]-interval[0])
    
        for interval in sorted_intervals:
            s,e = interval
            for i in range(s,e+1):
                if i not in dic:
                    dic[i] = e - s +1 
        output = []
        for query in queries:
            if query in dic:
                output.append(dic[query])
            else: 
                output.append(-1)


        return output