class Twitter:

    def __init__(self):
        # 2 dict
        # userid -> followers
        self.followers = defaultdict(set) # can we have o(1) search
        # userid -> tweets (stack)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweets[userId].insert(0,(self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        res.extend(self.tweets[userId][:10])
        for i in self.followers[userId]:
            res.extend(self.tweets[i][:10])
        res.sort(key=lambda x: x[0], reverse=True)
        res = res[:10]
        return [tweet for _, tweet in res]
    def follow(self, followerId: int, followeeId: int) -> None:
        # relationship 1 follows 2
        # 1 tweet: [6,5]
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)