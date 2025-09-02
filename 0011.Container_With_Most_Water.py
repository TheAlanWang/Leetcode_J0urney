# 0011.Container_With_Most_Water
'''
Approach: Two Pointers
State:
    left = 0, right = n-1, max_area
Transition:
    At each step:
        - width  = right - left
        - height = min(height[left], height[right])
        - area   = width * height
    Move the pointer at the shorter line inward.

* TC: O(n) | SC: O(1)
'''
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            if height[left] <= height[right]:
                area = width * height[left]
                max_area = max(max_area, area)
                left += 1
            else:
                area = width * height[right]
                max_area = max(max_area, area)
                right -= 1

        return max_area
