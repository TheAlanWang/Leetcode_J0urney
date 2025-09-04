# 0039.Combination_Sum

'''
Approach: Backtracking
State: dfs(idx, path, total)
Base Case: 
    - if total > target
    - if total == target
Transitions:
    For each candidate starting from idx:
        choose candidate
        recurse with updated total
        backtrack
        
* TC: O(n^(T/M)) | SC: O(T/M))
'''
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx, path, total):
            if total > target:
                return
            if total == target:
                res.append(path[:])
                return
            
            for i in range(idx, len(candidates)):
                path.append(candidates[i])
                dfs(i, path, total+candidates[i])
                path.pop()
        
        dfs(0, [], 0)
        return res

'''
Mistake:
    - forget to range(idx, n), range start from idx to avoid replication
'''