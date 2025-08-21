# https://leetcode.com/problems/find-the-duplicate-number/description/
# O(n) O(1)
# fast and slow pointer approach
'''
"We can model the problem as cycle detection. 
Each number points to the next index, and because a number repeats, it creates a cycle. 
Using Floyd’s Tortoise and Hare, we detect the cycle entry, which is the duplicate. 
This gives us O(n) time and O(1) space."
'''

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow