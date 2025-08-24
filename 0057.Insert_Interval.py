# https://leetcode.com/problems/insert-interval/description/
# O(n) O(1)

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        start, end = newInterval
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:  # next.start ≤ cur_end
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start, end])

        while i < n:
            res.append(intervals[i])
            i += 1
        return res