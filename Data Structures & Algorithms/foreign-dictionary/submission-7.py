class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n =len(words)
        dic = defaultdict(set)
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            k = 0
            while(k<min(len(w1),len(w2))):
                if w1[k] != w2[k]:
                    dic[w1[k]].add(w2[k])
                    break 
                else:
                    k+=1 
            if len(w1) > len(w2) and k == len(w2):
                return ""

        res = []

        def dfs(cur):
            if state[ord(cur)-ord('a')] == 1:
                return False
            if state[ord(cur)-ord('a')] == 2:
                return True
            state[ord(cur)-ord('a')] = 1 
            for nxt in dic[cur]:
                if not dfs(nxt):
                    return False
            res.append(cur)
            state[ord(cur)-ord('a')] = 2
            return True

                
            
        ch_set = set()
        state = [0]*26
        for word in words:
            for ch in word:
                ch_set.add(ch)


        for ch in ch_set:
            if state[ord(ch)-ord('a')] == 0:
                if not dfs(ch):
                    return ""
        return "".join(res[::-1])


                