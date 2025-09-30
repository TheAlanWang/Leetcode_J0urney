# 0047.Permutations_II

'''
Approach: Backtracking
* Skip:
    At the same depth, you must use the earlier one first before you can use the later one.
    `(i-1) not in used`: the earlier one is not used in this path, so skip the later one.

Time: O(N * N!) Space: O(N)
'''

from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if i in used:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in used:
                    continue

                path.append(nums[i])
                used.add(i)
                dfs(path, used)
                path.pop()
                used.remove(i)
        
        dfs([], set())
        return res