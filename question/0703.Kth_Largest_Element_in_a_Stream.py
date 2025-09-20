# 703.Kth_Largest_Element_in_a_Stream.py
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

# time complexity: O(m log k) for add | space complexity: O(k)
#   m is the number of elements in the stream, k is the size of the min-heap


from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k

        heapq.heapify(self.minheap) # min_heap
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        
        return self.minheap[0]
