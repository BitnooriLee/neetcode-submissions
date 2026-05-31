class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_window = defaultdict(int)

        l = 0 
        max_f = 0 

        for r in range(len(s)):
            count_window[s[r]] = count_window.get(s[r],0) +1 
            max_f = max(max_f, count_window[s[r]])

            if r - l + 1 - max_f > k:
                count_window[s[l]] -=1 
                l += 1 

        return r - l +1 

