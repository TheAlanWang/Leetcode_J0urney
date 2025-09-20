# 0300.Longest_Increasing_Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# time complexity: O(n log n) | space complexity: O(n)

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [] # dp[i] = smallest tail value of an increasing subsequence of length i+1
        
        def binarysearch(arr, target):
            left = 0
            right = len(arr) - 1
            ans = len(arr)
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        for idx, num in enumerate(nums):
            idx = binarysearch(dp, num)
            if idx == len(dp):
                dp.append(num)
            else:
                dp[idx] = num
        
        return len(dp)

'''
BinarySearch_Left (lower_bound):
ex1:
    arr=[1, 2, 4] target = 3
    return idx 2, mid >= target
ex2: 
    arr=[1, 2, 3, 3, 4] target = 3
    return idx 2
'''