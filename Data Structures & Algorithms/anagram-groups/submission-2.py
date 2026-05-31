class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        output = []
        for st in strs:
            tmp = "".join(sorted(st))
            if tmp in dic:
                dic[tmp].append(st)
            else:
                dic[tmp] = [st]
        for val in dic.values():
            output.append(val)
        
        return output