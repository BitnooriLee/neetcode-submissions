class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        output = []
        for st in strs:
            tmp = "".join(sorted(st))
            dic[tmp].append(st)
        
        return dic.values()