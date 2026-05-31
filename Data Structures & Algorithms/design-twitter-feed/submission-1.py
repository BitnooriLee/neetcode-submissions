class Twitter:

    def __init__(self):
        self.dic = defaultdict(set) # userid, follwing 
        self.feed_que = [] #[userid, tweetid]
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed_que.append([userId,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        #cnt # from i 
        cnt, i = 10, len(self.feed_que)-1
        output = []
        while(cnt > 0 and i >=0):
            if (self.feed_que[i][0] in self.dic[userId]) or (self.feed_que[i][0] == userId):
                output.append(self.feed_que[i][1])
                cnt -= 1 
            i -= 1 
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.dic[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.dic[followerId]:
            self.dic[followerId].remove(followeeId)
        
