class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = [[0]*26 for _ in range(len(strs))]

        for i in range(len(strs)):
            for ch in strs[i]:
                keys[i][ord(ch)-ord('a')] += 1 

        dic = defaultdict(list)
    
        for i in range(len(strs)):
            
            dic["".join(str(keys[i]))].append(strs[i])

        res = []

        for v in dic.values():
            res.append(v)

        return res
            

        


#Counter 는 dic key로 쓸 수 없음 
        