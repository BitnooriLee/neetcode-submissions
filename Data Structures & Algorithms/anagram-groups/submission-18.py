class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        output = []
        
        for st in strs: 
            tmp = [0] * 26 
            for i in range(len(st)):
                tmp[ord(st[i]) - ord('a')] += 1
            #k = "#".join(map(str,tmp))
            dic[tuple(tmp)].append(st)
        for v in dic.values():
            output.append(v)

        return output 
        