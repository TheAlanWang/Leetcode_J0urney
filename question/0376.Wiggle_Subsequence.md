# 0376.Wiggle_Subsequence
# https://leetcode.com/problems/wiggle-subsequence/

# time complexity: O(n) | space complexity: O(1)
"""
Approach: Greedy
1. Choice: 
    Compare current and previous elements.
        up wiggle: current > previous
        down wiggle: current < previous
2. State: 
    Maintain two variables, `pos` and `neg`
        pos: length of longest wiggle subsequence ending with a positive difference
        neg: length of longest wiggle subsequence ending with a negative difference
3. Greedy Update:
    if up wiggle, update pos
    if down wiggle, update neg
"""

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pos = 1
        neg = 1

        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx - 1]:
                pos = max(neg + 1, pos)
            elif nums[idx] < nums[idx - 1]:
                neg = max(pos + 1, neg)
        
        return max(neg, pos)