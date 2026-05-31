class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0 
        ln = len(s1)
        cnt = Counter(s1)
        need = len(cnt)
        have = 0 
        tmp = defaultdict(int)
        for r in range(len(s2)):
            tmp[s2[r]]+= 1
            if tmp[s2[r]] == cnt[s2[r]]:
                have += 1
                while(r-l+1 > ln):
                    if tmp[s2[l]] == cnt[s2[l]]:
                        have -=1 
                    tmp[s2[l]]-=1 
                    l+= 1 
                if need == have:
                    return True

        return False
                    
                
        