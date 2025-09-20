## 0046.Permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:                 # check index, not value
                    continue
                
                used.add(i)                   # mark index as used
                path.append(nums[i])
                dfs(path, used)
                path.pop()
                used.remove(i)                # backtrack index
        
        dfs([], set())
        return res