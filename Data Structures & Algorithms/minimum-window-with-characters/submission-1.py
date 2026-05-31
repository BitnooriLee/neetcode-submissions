class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        needDic = Counter(t)
        need = len(needDic)
        havDict = defaultdict(int)
        have = 0 
        res, resLen = [-1,-1], float("infinity")
        l= 0
        for r in range(len(s)):
            c = s[r]
            havDict[c] += 1  
            if c in needDic and needDic[c] == havDict[c]:
                    have += 1 
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = r - l +1 
                havDict[s[l]] -= 1 
                if s[l] in needDic and needDic[s[l]] > havDict[s[l]]:
                    have -= 1 
                l+=1 
        l,r = res
            
        return s[l:r+1] if resLen != float("infinity") else ""
        