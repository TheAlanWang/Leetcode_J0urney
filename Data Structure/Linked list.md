---
tags:
  - ds/linkedlist
pageorder: 3
---

- $ LinkedList = Nodes (data + address)
- Nodes are in non-consecutive memory locations

### Types of Linked Lists:
- Singly Linked List
- Doubly Linked List

### Reverse Singly linked list
Use recursive way:
Time complexity: O(n) Space complexity: O(n)

```python
'''
Recursively reverses a singly linked list.
Args: head (ListNode): The head of the linked list.
Returns: ListNode: The new head of the reversed linked list.
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        # Base case: If the list is empty or reaches the last node, return it
        if not head or not head.next:
            return head

        # Recursively reverse the rest of the list
        newHead = self.reverseList(head.next)

        # Reverse the current node's pointer
        head.next.next = head  # Point next node's next to current node
        head.next = None  # Set current node's next to None

        return newHead
```

```python
"""
Recursively reverses a singly linked list.
Args: head (ListNode): The head of the linked list.
Returns: ListNode: The new head of the reversed linked list.
"""
def reverseList(self, head):
        # Base case: If the list is empty, return None
        if not head:
            return None

        # Assume the new head is the current node
        newHead = head

        # If there is a next node, recursively reverse the rest of the list
        if head.next:
            newHead = self.reverseList(head.next)

            # Reverse the current node's link
            head.next.next = head

        # Set the next pointer of the current node to None to avoid cycles
        head.next = None

        # Return the new head of the reversed list
        return newHead
```

Time Complexity: O(n) Space Complexity: O(n)