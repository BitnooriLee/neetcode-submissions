class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweeters = defaultdict(list)
        self.t_idx = 0 #이게 핵심

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweeters[userId].append((self.t_idx, tweetId))
        self.t_idx += 1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxh = []

        users = self.followers[userId]
        users.add(userId)

        for user in users:
            last = len(self.tweeters[user])
            if last > 0:
                idx, tId = self.tweeters[user][last-1]
                heapq.heappush(maxh, (-idx, tId, last-1, user))

        res = []
        while maxh and len(res) < 10:
            _idx, _tId, _last, _user = heapq.heappop(maxh)
            res.append(_tId)
            if _last > 0:
                idx, tId = self.tweeters[_user][_last-1]
                heapq.heappush(maxh, (-idx, tId , _last-1, _user))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
