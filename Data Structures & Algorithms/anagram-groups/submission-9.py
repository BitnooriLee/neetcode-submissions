class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
       
        for st in strs:
            cnt = [0]*26
            for ch in st:
                cnt[ord(ch)-ord('a')] += 1 
            dic[tuple(cnt)].append(st)
            
        return [val for val in dic.values()]


    #O(n * k)
    #O(1)
        