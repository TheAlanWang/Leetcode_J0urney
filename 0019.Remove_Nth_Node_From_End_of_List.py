# 0019.Remove_Nth_Node_From_End_of_List.py

'''
Approach: Linked list
Transitions:
    1. Compute length
    2. Removing the n-th node (length-n+1)
    3. Only need to move (length-n) steps from the dummy node to land at the node right before the target.
    4. Use tail.next = tail.next.next to remive
'''
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional['ListNode'], n: int) -> Optional['ListNode']:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        dummy = ListNode(-1, head)
        tail = dummy
        for _ in range(length - n):
            tail = tail.next
        
        tail.next = tail.next.next
        return dummy.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next