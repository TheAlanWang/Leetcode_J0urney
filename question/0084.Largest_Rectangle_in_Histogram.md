# 0084.Largest_Rectangle_in_Histogram.py

'''
Approach: monotonic stack, store idx(increasing height)
State: height add dummy
Transition:
    high: mid
    width: (right - left + 1)
        right = i - 1 -> cur_height_idx is lower, so right - 1
        left = (after pop mid) stack[-1] + 1 -> left is lower, so left + 1
        (i - 1) + (stack[-1] + 1) + 1
    max_area = high * width
* TC: O(n) | SC: O(n)
'''
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [-1]
        max_area = 0
        heights.append(0)
        for idx, height in enumerate(heights):

            while stack[-1] != -1 and heights[stack[-1]] >= height: # 6 >= 2
                mid = stack.pop()
                hi = heights[mid]
                left = stack[-1]
                width = (idx - 1) - (left + 1) + 1
                max_area = max(max_area, hi * width)

            stack.append(idx)
        
        heights.pop()

        return max_area