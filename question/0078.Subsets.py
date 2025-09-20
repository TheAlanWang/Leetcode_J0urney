# 0078.Subsets
'''
Subset: order inside a subset does not matter
'''
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, path):
            res.append(path[:])
            if len(path) > len(nums):
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res