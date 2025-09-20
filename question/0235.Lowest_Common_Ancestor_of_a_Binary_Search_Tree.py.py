# 0235.Lowest_Common_Ancestor_of_a_Binary_Search_Tree.py

'''
Top-down DFS
'''

from typing import Optional

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return
            
            if p.val <= node.val <= q.val or q.val <= node.val <= p.val:
                return node

            if p.val < node.val and q.val < node.val:
                return dfs(node.left)
            
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)

        return dfs(root)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None