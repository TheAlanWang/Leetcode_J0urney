# 749. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# Time Complexity: O(n) Space Complexity: O(n)

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # store idx 
        res = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[idx]:
                prev_idx = stack.pop()
                res[prev_idx] = idx - prev_idx
            
            stack.append(idx)
        
        return res