# 0090.Subsets_II
'''
Approach: Backtracking
        
i: the index you are trying at this level
start: control where the loop begin
len(path): the current recursion depth
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