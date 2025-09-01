# 0090.Subsets_II
'''
Approach: Backtracking

State: (start, path)
    start - control where the loop begin
    path - the current recursion depth
Base Case: start == len(nums)
Choice:  for i in [start, end], skip duplicate

Time: O(N * 2^N) | Space: O(N)
'''
from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()                                  # duplicate numbers are adjacent
        self.backtrack(0, [], nums, res)             # (start from 0, path, nums, res)
        return res

    def backtrack(self, start, path, nums, res):
        res.append(path[:])
        if start == len(nums):
            return        
        for i in range(start, len(nums)):            # i is decision point
            if i > start and nums[i] == nums[i-1]:   # only include the first occureence
                continue
            path.append(nums[i])
            self.backtrack(i + 1, path, nums, res) 
            path.pop()


'''
dry run [1,2,2]
                            []
        ┌───────────────────┼───────────────────┐
        │                   │                   │
      pick 1              pick 2            skip (dup 2)     start = 0
        │                   │
       [1]                 [2]
        │                   │
   ┌────┴────┐              │
   │         │              │
pick 2   skip (dup 2)     pick 2                             start = 1
   │                        │
 [1,2]                    [2,2]
   │
   │
 pick 2                                                      start = 2
   │
 [1,2,2]

'''