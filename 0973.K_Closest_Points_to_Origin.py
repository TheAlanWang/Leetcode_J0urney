# 0973.K_Closest_Points_to_Origin
# https://leetcode.com/problems/k-closest-points-to-origin/description/
# time complexity: O(n log n) | space complexity: O(n)


from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minheap.append((dist, x, y))
        
        heapq.heapify(minheap)
        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(minheap)
            res.append([x, y])
        
        return res