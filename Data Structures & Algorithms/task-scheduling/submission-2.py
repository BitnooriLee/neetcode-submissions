class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        cnt = collections.Counter(tasks)
        print(cnt.values())
        mx = max(cnt.values())
        c = 0 
        for val in cnt.values():
            if val == mx:
                c+=1 
        print(mx,c)
        return max((n+1)*(mx-1)+c, len(tasks))

            
            