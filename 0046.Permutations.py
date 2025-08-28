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
                if nums[i] in used:
                    continue
                
                path.append(nums[i])
                used.add(nums[i])
                dfs(path, used)
                path.pop()
                used.remove(nums[i])
            

        dfs([], set())
        return res