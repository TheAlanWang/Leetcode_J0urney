# https://leetcode.com/problems/merge-intervals/description/

# Time Complexity: O(n log n) due to sorting | Space Complexity: O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])

        res = []
        
        for start, end in intervals:
            if res and  start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end]) 
        
        return res
    

# intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
# intervals = sorted(intervals, key=lambda x: x[0])  # Sort intervals by start time