# 853.Car Fleet
# https://leetcode.com/problems/car-fleet/description/

# Time Complexity: O(n log n) | Space Complexity: O(n)

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_spd = sorted(zip(position, speed), key=lambda x:x[0], reverse = -1)
        
        stack = [] # store time
        for pos, spd in pos_spd:
            time = (target - pos) / spd
            if not stack or time > stack[-1]:
                stack.append(time)
        
        return len(stack)