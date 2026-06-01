class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        besti, bestj = 0, float("inf")
        c_t = Counter(t)
        need = len(c_t)
        s_t = defaultdict(int)
        
        l = 0 
        have = 0 
        for r in range(len(s)):
            s_t[s[r]] += 1
            if s_t[s[r]] == c_t[s[r]]:
                have += 1 
            while(have == need):
                #best 값을 업데이트 
                if (bestj - besti) > (r-l):
                    besti, bestj = l,r
                #windowㅎ하나 줄임 
                s_t[s[l]]-=1
                # s_t의 갯수가 더 작아졌을때만 while 종료 
                if s_t[s[l]] < c_t[s[l]]:
                    have -=1
                l+=1 
            
        return s[besti:bestj+1] if bestj != float("inf") else ""