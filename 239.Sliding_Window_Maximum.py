# https://leetcode.com/problems/sliding-window-maximum/
# O(n) O(n)
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums[:]

        left = right = 0
        queue = deque() # store idx, nums[dp[idx]] decrease
        res = []
        
        while right < len(nums):
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()
            queue.append(right)
            
            if queue[0] < left:
                queue.popleft()
            
            if right - left + 1 == k:
                res.append(nums[queue[0]])
                left += 1

            right += 1

        return res