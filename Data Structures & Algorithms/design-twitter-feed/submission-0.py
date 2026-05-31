class Twitter:

    def __init__(self):
        self.follow_dict = defaultdict(set) # follower: followee 
        self.feed_queue = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        #add
        self.feed_queue.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        #post by recent
        # 10 most recent tweet ID 
        # by userID's followee 
        cnt,i = 0, len(self.feed_queue)-1
        tmp = [] 
        while(cnt < 10 and i >=0):
            if self.feed_queue[i][0] in self.follow_dict[userId] or userId == self.feed_queue[i][0] :
                tmp.append(self.feed_queue[i][1])
                cnt += 1 
            i -= 1 
        return tmp
        
    def follow(self, followerId: int, followeeId: int) -> None:
        # add follower -> followee order x 
        if followeeId not in self.follow_dict[followerId]:
            self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_dict[followerId]:
            self.follow_dict[followerId].remove(followeeId)

        # remove order x 
        
