class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        mx = max(cnt.values())
        mx_cnt = 0 
        for val in cnt.values():
            if mx == val:
                mx_cnt += 1


        return max((mx-1)*(n+1)+mx_cnt, len(tasks))