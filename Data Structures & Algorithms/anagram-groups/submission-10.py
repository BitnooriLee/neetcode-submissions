class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}
        for st in strs:
            cnt = [0] * 26
            for ch in st:
                cnt[ord(ch) - ord('a')] += 1
            if tuple(cnt) in dic:
                dic[tuple(cnt)].append(st)
            else:
                dic[tuple(cnt)] = [st]

        return [val for val in dic.values()]