# 0019.Remove_Nth_Node_From_End_of_List.py

'''
Approach: Linked list
Transitions:
    only need to move (length – n) steps from the dummy node to land at the node right before the target.
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