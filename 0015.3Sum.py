# 0015. 3Sum
# https://leetcode.com/problems/3sum/
# Time Complexity: O(n^2) | Space Complexity: O(logn) for sorting

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []
        for idx in range(0, len(nums) - 2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            target = -nums[idx]
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right]
                
                if total == target:
                    res.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1


            
        return res