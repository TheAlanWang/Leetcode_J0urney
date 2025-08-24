# https://leetcode.com/problems/add-two-numbers/description/
# O(max(m, n)) O(n)

'''
* Remember to handle the None case
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        tail = dummy
        carry = 0

        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0    # get value or 0 if None
            l2_val = l2.val if l2 else 0

            val = l1_val + l2_val + carry
            carry = val // 10
            val = val % 10
            tail.next = ListNode(val)

            tail = tail.next
            l1 = l1.next if l1 else None  # move to next node or None if already None
            l2 = l2.next if l2 else None
        
        return dummy.next