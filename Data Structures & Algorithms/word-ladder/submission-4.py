class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        dic = defaultdict(list)
        visited = set()
        l = len(wordList)
        #dictionary 만듬, beginword도 들어가 있음   
        for word in wordList:
            for i in range(l):
                key = word[:i] + "*" + word[i+1:]
                dic[key].append(word)

        q = deque([(beginWord, 1)])
        visited.add(beginWord)

        while q:
            cur, d = q.popleft()
            if cur == endWord:
                return d
            for i in range(l):
                new_key = cur[:i] + "*" + cur[i+1:]
                for nei in dic[new_key]:
                    if nei not in visited:
                        q.append((nei,d+1))
                        visited.add(nei)


        return 0



        


        
        
        