class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1 
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        maxh = [] 
        users = self.following[userId]
        users.add(userId)

        for writer in users:
            if len(self.tweets[writer]) > 0:
                idx = len(self.tweets[writer])-1
                t, tId = self.tweets[writer][idx]
                maxh.append((-t, writer, tId, idx))
        heapq.heapify(maxh)
        
        while maxh and len(feed) < 10:
            _t, _uId, _tId, _idx = heapq.heappop(maxh)
            feed.append(_tId)
            if _idx > 0:
                t, tId = self.tweets[_uId][_idx-1]
                heapq.heappush(maxh, (-t, _uId, tId, _idx-1))


        return feed 

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
