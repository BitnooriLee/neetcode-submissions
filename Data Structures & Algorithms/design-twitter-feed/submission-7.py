class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets_t = 0 
        self.usertweets = defaultdict(list)
    
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.usertweets[userId].append((self.tweets_t, tweetId))
        self.tweets_t+= 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        followees = self.followers[userId]
        followees.add(userId)
        h = []

        for followee in followees:
            if self.usertweets[followee]:
                heapq.heappush(h,(-self.usertweets[followee][-1][0],self.usertweets[followee][-1][1],len(self.usertweets[followee])-1,followee))
        while(h and len(feed)<10):
            time, t_id, last_idx,last_followee = heapq.heappop(h)
            feed.append(t_id)
            if last_idx > 0:
                heapq.heappush(h,(-self.usertweets[last_followee][last_idx-1][0],self.usertweets[last_followee][last_idx-1][1],last_idx-1,last_followee))

        return feed 

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
