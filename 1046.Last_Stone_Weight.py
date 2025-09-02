# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/description/

'''
Approach: heap - maxheap
state:
    maxheap: stores stone weights as negatives so that heapq gives us the largest stone first
Transitions:
    1. Build the heap from all stones (negated).
    2. While len(heap) > 1:
        - Pop the two heaviest stones (heappop twice).
        - If their weights differ, push the difference back (still negated).
    3. If heap is empty, return 0; otherwise return -heap[0].

* time complexity: O(n log n) | space complexity: O(n)
'''
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