# 0853.Car Fleet
# https://leetcode.com/problems/car-fleet/description/

'''
Approach: Monotonic Stack on arrival times
Transitions:
    - Pair cars by (position, speed) and sort by position DESC (closest to target first).
    - Compute each car's arrival time: t = (target - pos) / speed.
    - Scan from closest → farthest:
        * If current time > top of stack, it can't catch the fleet ahead → starts a NEW fleet → push.
        * Else (<=), it catches up (or arrives same time) → merges with the fleet ahead → do nothing.

    * Time Complexity: O(n log n) | Space Complexity: O(n)
'''

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