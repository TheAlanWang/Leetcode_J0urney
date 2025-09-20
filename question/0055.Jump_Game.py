# https://leetcode.com/problems/jump-game/description/
# time complexity: O(n) | space complexity: O(1)

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

        return True
