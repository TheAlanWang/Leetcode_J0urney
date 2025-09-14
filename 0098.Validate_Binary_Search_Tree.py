# 0098.Validate_Binary_Search_Tree.py

'''
Only comparing parent-child is insufficient; Must carry global bounds.

Approach: Tree DFS (top down)
Transitions:
    left < node.val < right
    - for every val in right subtree, low < v < node.val
    - for every val in left subtree, node.val < v < high

* TC: O(n) | SC: O(h)
'''
from typing import Optional

class Solution:
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        def valid_binary(node, low, high):
            if not node:
                return True
            
            if not(low < node.val < high):
                return False

            return valid_binary(node.left, low, node.val) and valid_binary(node.right, node.val, high)
        
        return valid_binary(root, float('-inf'), float('inf'))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right