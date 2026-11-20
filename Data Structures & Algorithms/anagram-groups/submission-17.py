class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp = [0] * 26 
        dic = defaultdict(list)
        output = []
        
        for st in strs: 
            for i in range(len(st)):
                tmp[ord(st[i]) - ord('a')] += 1
            k = "#".join(map(str,tmp))
            dic[k].append(st)
            tmp = [0] * 26 
        for v in dic.values():
            output.append(v)

        return output 
        