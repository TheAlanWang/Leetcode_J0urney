# 0033.Search_in_Rotated_Sorted_Array

'''
Approach: binary search
Transitions:
    If target lies in the sorted half, move into it; otherwise go to the other half.

* TC: O(log n) | SC: O(1)
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
