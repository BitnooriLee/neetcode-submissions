class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] = i 

        start = 0 
        cur_max = 0
        res = []
        for i in range(len(s)):
            cur_max = max(cur_max, dic[s[i]])
            if i == cur_max:
                res.append(cur_max-start+1)
                start = i + 1
        return res


        
        