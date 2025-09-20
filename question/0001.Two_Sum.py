# 0001.Two_Sum.md

'''
Approach: Hash Map
State:
    dic[num] = index of num
Transition:
    For each num:
        - Check if (target - num) is in dic
        - If yes, return [dic[target - num], current index]
        - Otherwise, store num in dic

* TC: O(n) | SC: O(n)
'''
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dic = {}
        for idx, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], idx]
            dic[num] = idx