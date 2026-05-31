class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq, res = 1,0
        cnt = defaultdict(int)
        for r in range(len(s)):
            cnt[s[r]] += 1 
            maxFreq = max(maxFreq, cnt[s[r]])
            #len(window) - maxFreq <= k 
            while(r - l +1 - maxFreq > k):
                cnt[s[l]] -= 1 
                l += 1 
            res = max(res, r - l+1)

        return res

            



        