# 0875.Koko_Eating_Bananas.py

'''
Clarifications: 
    - we need the minimum speed k so Koko finished within h hours

Approach: binary search (find minimum speed) `times(k) <= h`
Key insight:
    - As spd increase, time decrease
Transitions:
    def the function: eat_time = (pile + spd - 1) // spd
    use lower bound, find the first k where a monotone predicate becomes True
    
* TC: O(nlogn) | SC: O(1)
'''
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def get_time(spd):
            times = 0
            for pile in piles:
                times += (pile + spd - 1) // spd
            return times
        
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2   # mid = eat speed
            
            eat_time = get_time(mid)
            if eat_time <= h:           # find min k, most left
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res