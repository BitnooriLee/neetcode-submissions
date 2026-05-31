class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    

        dic = defaultdict(list)
    
        for i in range(len(strs)):
            keys = [0]*26
            for ch in strs[i]:
                keys[ord(ch)-ord('a')] += 1 
            dic[tuple(keys)].append(strs[i])

        return list(dic.values())
            

        


#Counter 는 dic key로 쓸 수 없음, list 도 마찬가지 -> str으로 변환후 조인
# tuple(count)
#O(mn)
#O(n) -> output list 출력 O(mn)
        