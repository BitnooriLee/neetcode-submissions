class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        output = []

        for st in strs:
            k = tuple(sorted(st))
            dic[k].append(st)

        for v in dic.values():
            output.append(v)

        return output
        