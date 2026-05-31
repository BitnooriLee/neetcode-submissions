class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)

        dic = defaultdict(set)

        for i in range(n-1):
            first = words[i]
            second = words[i+1]
            k = 0 
            while(k<min(len(first),len(second))):
                if first[k] != second[k]:
                    dic[first[k]].add(second[k])
                    break
                else:
                    k+=1 
            if len(first) > len(second) and k == len(second):
                return ""
        order = []

        def dfs(cur):
            if state[ord(cur)-ord('a')] == 1:
                return False
            if state[ord(cur)-ord('a')] == 2:
                return True
            state[ord(cur)-ord('a')] = 1 
            for nei in dic[cur]:
                if not dfs(nei):
                    return False

            state[ord(cur)-ord('a')] = 2
            order.append(cur)
            return True 
            
        state = [0]*26
        ch_set = set()

        for word in words:
            for ch in word:
                ch_set.add(ch)

        for ch in ch_set:
            if state[ord(ch) - ord('a')] == 0:
                if not dfs(ch):
                    return ""
        return "".join(order[::-1])

                   