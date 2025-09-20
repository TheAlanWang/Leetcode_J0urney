# 0253.Meeting_Rooms_II

'''
Approach: heap
State: minheap (store interval.end)
Trasition:
    1. sorted by start
    2. loop intervals (start, end)
        if heap[end] <= new_intervals.start, pop
        heappush end

* TC: O(nlog) | SC: O(n)
'''
from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x: x[0])
        heap = []
        
        for start, end in intervals:
            if heap and heap[0] <= start:
                heapq.heappop(heap)
        
            heapq.heappush(heap, end)
        
        return len(heap)