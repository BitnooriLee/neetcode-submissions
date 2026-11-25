class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        dic = defaultdict(int)
        start = 0
        max_f = 0 
        for end in range(len(s)):
            dic[s[end]]+=1
            max_f = max(max_f, dic[s[end]])
            if (end-start+1) - max_f > k:
                dic[s[start]] -= 1
                start += 1
            res = max(res, end-start+1)
        
        return res



        