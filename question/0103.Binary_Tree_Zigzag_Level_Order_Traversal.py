# 0103.Binary_Tree_Zigzag_Level_Order_Traversal

'''
Approach: BFS level order traversal
State: queue, level, reverse_flag
Transitions:
    if reverse_flag: level.reverse()

* TC: O(n) | SC: O(W)
'''
from collections import deque
from typing import Optional, List

class Solution:
    def zigzagLevelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        reverse_flag = False
        res = []
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
            
            if reverse_flag:
                level.reverse()

            res.append(level)
            reverse_flag = not reverse_flag
        
        return res

    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right