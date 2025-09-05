# 0739.Daily_Temperatures

'''
Approach: Stack - Monotonic Stack
Status:
    - Stack: store idx from low to high
    - res: [0] * n (default 0s)
Transitions:
    - iterative idx temp:
        while stack and temperatures[stack[-1]] < temp, pop and update res
        push idx onto stack

* TC: O(n) | SC: O(n)
'''
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] # store indices
        n = len(temperatures)
        res = [0] * n
        for idx, temp in enumerate(temperatures):
            
            while stack and temperatures[stack[-1]] < temp:
                pre_idx = stack.pop()
                res[pre_idx] = idx - pre_idx
            
            stack.append(idx)
        return res
        
