# 1891.Cutting_Ribbons
# https://leetcode.com/problems/cutting-ribbons/description/
# Time complexity is O(n logm) | space complexity is O(1)
#   - max(arr) time compleixty is O(n)

'''
Approach: Binary Search (Binary Search on Answer)
1. Montonic feasibility: As required length ↑, count ↓
2. Search space
3. Decision function
'''
from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)
        ans = 0

        def count_ribbons(r):
            count = 0
            for ribbon in ribbons:
                count += ribbon // r
            return count

        while left <= right:
            mid = (left + right) // 2
            count = count_ribbons(mid)

            if count >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
