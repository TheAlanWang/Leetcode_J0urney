# 0236.Lowest_Common_Ancestor_of_a_Binary_Tree.py

'''
Bottom-up (postorder) DFS
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            if left:
                return left
            if right:
                return right

        return dfs(root)
    
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None