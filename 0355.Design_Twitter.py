# 0355.Design_Twitter.py
# https://leetcode.com/problems/design-twitter/description/

'''
getNewsFeed: O(N log k) k is the number of followees, N is the number of tweets
'''

from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.follow_dic = defaultdict(set) # {follwer: {followee} }
        self.twitte_dic = defaultdict(list) # {userID: [(time1, twitteid1), (time2, twitteid2)]}

        self.tw_time = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tw_time += 1
        self.twitte_dic[userId].append((self.tw_time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.follow_dic[userId].add(userId)
        for followeeId in self.follow_dic[userId]:
            if followeeId in self.twitte_dic:
                idx = len(self.twitte_dic[followeeId]) - 1
                tw_time = self.twitte_dic[followeeId][idx][0]
                twitterid = self.twitte_dic[followeeId][idx][1]
                heapq.heappush(heap, (-tw_time, followeeId, twitterid, idx - 1))
        
        res = []
        while len(res) < 10 and heap:
            tw_time, followeeId, twitterid, idx = heapq.heappop(heap)
        
            res.append(twitterid)
            if idx >= 0:
                tw_time = self.twitte_dic[followeeId][idx][0]
                twitterid = self.twitte_dic[followeeId][idx][1]
                heapq.heappush(heap, (-tw_time, followeeId, twitterid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dic[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_dic[followerId]:
            self.follow_dic[followerId].remove(followeeId)