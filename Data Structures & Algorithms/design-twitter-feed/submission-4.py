class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list) # userId, (time, tweetId)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1 
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        people = self.following[userId]
        people.add(userId)
        maxHeap = []
        res = []
        for uid in people:
            arr = self.tweets[uid]
            if arr:
                idx = len(arr)-1
                t, tid = arr[idx] 
                heapq.heappush(maxHeap, (-t, tid, uid, idx))
        
        while maxHeap and len(res) < 10:
            neg_t, twid, userid, indx = heapq.heappop(maxHeap)
            res.append(twid)
            indx -= 1 
            if indx >=0 :
                t2, twid2 = self.tweets[userid][indx]
                heapq.heappush(maxHeap, (-t2, twid2, userid, indx))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId) # remove 는 없으면 key error
        
