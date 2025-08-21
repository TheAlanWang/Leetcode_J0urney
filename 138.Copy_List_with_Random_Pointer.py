# https://leetcode.com/problems/copy-list-with-random-pointer/description/
# O(n) O(n) \ space complexity could imporve to O(1) 

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        clones = {None: None}           # map original -> clone; None maps to None
        cur = head
        while cur:
            clones[cur] = Node(cur.val)  # 1) make all nodes
            cur = cur.next

        cur = head
        while cur:
            node = clones[cur]           # 2) wire next & random via the map
            node.next = clones[cur.next]
            node.random = clones[cur.random]
            cur = cur.next

        return clones[head]