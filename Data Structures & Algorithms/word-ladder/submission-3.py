class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        dic = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                k = word[:i] + "*" + word[i+1:]
                dic[k].append(word)
       
        visited = set([beginWord])
        q = deque([(beginWord,1)])


        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            

            for i in range(len(word)):
                k = word[:i] + "*" + word[i+1:]
                for nxt in dic[k]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, depth+1))
                dic[k] = []
            

 
    
                
        return 0
