class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1:
            return t if t in s else ""
        cnt = Counter(t)
        target = len(cnt)
        end = len(s) 
        dic = defaultdict(int)
        have = 0 
        resl,resr = 0, float("inf") #나중에 체크 
        l = 0 
        for r in range(end):
            dic[s[r]]+= 1 
            if s[r] in cnt and cnt[s[r]] == dic[s[r]]:
                have += 1 
            while have == target:
                if r - l < resr - resl:
                    resr, resl = r,l
                dic[s[l]] -= 1 
                if s[l] in cnt and cnt[s[l]] > dic[s[l]] :
                    have -= 1 
                l+= 1
        return s[resl:resr+1] if resr != float("inf") else ""
                    
                



