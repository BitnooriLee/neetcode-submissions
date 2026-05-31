from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # start 기준 정렬
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        res = [-1] * len(queries)
        heap = []  # (interval_length, end)
        j = 0
        n = len(intervals)

        for q, idx in sorted_queries:
            # 현재 query보다 시작점이 작거나 같은 interval들을 heap에 추가
            while j < n and intervals[j][0] <= q:
                s, e = intervals[j]
                heapq.heappush(heap, (e - s + 1, e))
                j += 1

            # 현재 query를 포함할 수 없는 interval 제거
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # heap top이 가장 짧은 유효 interval
            if heap:
                res[idx] = heap[0][0]

        return res