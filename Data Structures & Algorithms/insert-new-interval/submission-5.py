class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        q= deque()
        for s,e in intervals:
            q.append((s,e))

        output = []
        cur_s, cur_e = q[0]
        while q:
            ns,ne = q.popleft()
            if cur_e < ns:
                output.append([cur_s,cur_e])
                cur_s = ns
                cur_e = ne 
            else:
                cur_e = max(cur_e, ne)
                cur_s = min(cur_s, ns)

        output.append([cur_s, cur_e])

        return output
            


        