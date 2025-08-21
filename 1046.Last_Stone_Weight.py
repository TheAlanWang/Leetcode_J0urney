# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/description/

# time complexity: O(n log n) | space complexity: O(n)

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)                 # O(n)

        while len(heap) > 1:                
            x = -heapq.heappop(heap)        # largest
            y = -heapq.heappop(heap)        # 2nd largest
            diff = x - y                    # x >= y
            if diff:                        # if not equal
                heapq.heappush(heap, -diff)

        return -heap[0] if heap else 0