import collections, heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.following = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        heap = []

        self.following[userId].add(userId)

        for followee in self.following[userId]:
            if followee in self.tweets:
                tweet_idx = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][tweet_idx]

                heapq.heappush(heap, (time, tweetId, followee, tweet_idx - 1))


        while heap and len(feed) < 10:
            time, tweetId, followee, tweet_idx = heapq.heappop(heap)
            feed.append(tweetId)

            if tweet_idx >= 0:
                next_time, next_tweetId = self.tweets[followee][tweet_idx]
                heapq.heappush(heap, (next_time, next_tweetId, followee, tweet_idx - 1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)