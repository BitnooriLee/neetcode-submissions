class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets_by_user = defaultdict(list)
        self.tweet_idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets_by_user[userId].append((self.tweet_idx, tweetId))
        self.tweet_idx += 1 
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        users = self.followers[userId]
        users.add(userId)

        h = []
        for user in users:
            if self.tweets_by_user[user]:
                heapq.heappush(h, (-self.tweets_by_user[user][-1][0], self.tweets_by_user[user][-1][1], len(self.tweets_by_user[user])-1, user))
        
        while h and len(res) < 10:
            ct_idx, ct_id, l, u = heapq.heappop(h)
            res.append(ct_id)
            if l > 0:
                heapq.heappush(h, (-self.tweets_by_user[u][l-1][0], self.tweets_by_user[u][l-1][1], l-1, u))
                
        return res

        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

        
