# 0355.Design_Twitter.py
# https://leetcode.com/problems/design-twitter/description/

# getNewsFeed: O(N log k) k is the number of followees, N is the number of tweets


from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)   # { userID: [(time, tweetId1), (time, tweetId2)] }
        self.followMap = defaultdict(set)   # { follower: {followee1, followee2} }

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweetMap[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minheap = []
        res = []
        
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]: # put followee's laster twitter
            if followee in self.tweetMap:
                idx = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][idx]
                heapq.heappush(minheap, (-time, tweetId, followee, idx - 1))
        
        while minheap and len(res) < 10:
            time, tweetId, followee, idx = heapq.heappop(minheap)
            res.append(tweetId)
            if idx >= 0:
                time, tweetId = self.tweetMap[followee][idx] # push previous tweetid
                heapq.heappush(minheap, (-time, tweetId, followee, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)