class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}

        for i in range(len(s)):
            dic[s[i]] = i 
        res = []
        start = 0 
        cur_max = 0 
     
        for i in range(len(s)):
            cur_max = max(cur_max, dic[s[i]])
            if i == cur_max:
                res.append(cur_max - start +1)
                start = i + 1 
        return res
        
            
        