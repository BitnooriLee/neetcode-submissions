class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        for i, ch in enumerate(s):
            dic[ch] = i # right most 
        l = len(s)
        output = []

        start = 0
        cur_max = 0

        for i in range(l):
            cur_max = max(cur_max, dic[s[i]])
            if i == cur_max:
                output.append(cur_max - start +1)
                start = i+1 

        return output
        