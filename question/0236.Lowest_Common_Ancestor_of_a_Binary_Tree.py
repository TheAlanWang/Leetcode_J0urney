# 0236.Lowest_Common_Ancestor_of_a_Binary_Tree.py

'''
Approach: DFS Bottom-up (postorder) DFS
Transitions:
    Use postorder traversal
    1. if a subtree constains p or q, return node
    2. if both left and right, return node
    3. if only one side, propagate the node upward
* TC: O(n) | SC: O(h)
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