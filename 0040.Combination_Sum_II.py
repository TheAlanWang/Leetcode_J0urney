# 0040.Combination_Sum_II

'''
time complexity: O(2^n) | space complexity: O(n)
* Use the first occurrence at a level; skip later equals at the same level.
'''
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(idx, path, total):
            if total == target:
                res.append(path[:])
                return
            
            if total > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
        
        backtrack(0, [], 0)
        return res