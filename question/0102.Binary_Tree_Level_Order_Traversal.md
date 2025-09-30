# 0102.Binary_Tree_Level_Order_Traversal
'''
Approach: Lever order traversal
* deque([None]) has value, deque([]) does not have value
'''

from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        res = []
        if not root:
            return res
            
        queue = deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        
        return res

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right