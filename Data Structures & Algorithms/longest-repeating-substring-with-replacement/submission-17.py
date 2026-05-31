class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        cnt = defaultdict(int)
        res = 0 
        maxFreq = 1
        #len(window) - maxFreq <= k 
        for r in range(len(s)):
            cnt[s[r]] +=1 
            maxFreq = max(maxFreq,cnt[s[r]])
            while(r-l+1 - maxFreq > k):
                cnt[s[l]]-=1
                l+=1 
            res = max(res, r-l+1)
        return res 



# maxFreq 1에서 시작 s[r]갯수와 비교. s[r]을 더했으니까. 
# s[l] s[r]이 같으면 애초에 while 안으로 안들어옴         