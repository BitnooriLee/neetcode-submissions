class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        maxfreq,res = 0,0
        cnt = defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]]+=1 
            maxfreq = max(maxfreq, cnt[s[r]])
            while(r-l+1 - maxfreq > k):
                cnt[s[l]]-= 1
                l += 1 
            res = max(res, r-l+1)
        return res
                

        