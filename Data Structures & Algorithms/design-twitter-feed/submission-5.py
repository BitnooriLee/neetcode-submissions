class Twitter:

    def __init__(self):
        self.t = 0 
        self.followers = defaultdict(set) # follower: followee
        self.feeds = [] # timestamp, (userid, tweetid)
        self.postlist = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postlist[userId].append((self.t,tweetId))
        self.t += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        people = self.followers[userId]
        people.add(userId)
        maxh = []
        res = []

        for uid in people:
            arr = self.postlist[uid]
            if arr:
                idx = len(arr)-1
                t, tid = arr[idx]
                heapq.heappush(maxh, (-t, tid, uid, idx))
        
        while maxh and len(res) < 10:
            neg_t, twid, userid, indx = heapq.heappop(maxh)
            res.append(twid)
            indx -= 1 
            if indx >= 0:
                t2, twid2 = self.postlist[userid][indx]
                heapq.heappush(maxh, (-t2, twid2, userid, indx))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)

        
