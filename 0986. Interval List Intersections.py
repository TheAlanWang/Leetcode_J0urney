# https://leetcode.com/problems/interval-list-intersections/
# Time complexity: O(M + N) | Space complexity: O(M + N)

'''
two pointer - two sorted lists
1. find overlap parts
    start = max(l1.start, l2.start)
    end = min(l1.end, l2.end)
2. when l1.start > l2.end -> move l2
* Overlap check: maxStart <= minEnd
* mvoe the pointer of the interval which ends first
'''

from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        res = []
        while i < len(firstList) and j < len(secondList):
            l1_start, l1_end = firstList[i]
            l2_start, l2_end = secondList[j]

            cur_start = max(l1_start, l2_start)
            cur_end = min(l1_end, l2_end)
            
            if cur_start <= cur_end:
                res.append([cur_start, cur_end])
            
            if l1_end < l2_end:
                i += 1
            else:
                j += 1
            
        return res