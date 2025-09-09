# 0252.Meeting_Rooms.py
# https://leetcode.com/problems/meeting-rooms/description/
'''
Approach: Intervals
* TC: O(nlogn) | SC: O(n)
'''
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:


        intervals = sorted(intervals, key = lambda x:x[0])
        cur_end = 0
        for start, end in intervals:
            if cur_end > start:
                return False
            cur_end = end
        
        return True