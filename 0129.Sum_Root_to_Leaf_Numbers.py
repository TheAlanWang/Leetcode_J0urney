# 0129.Sum_Root_to_Leaf_Numbers

'''
Approach: DFS Top-Down

Time Complexity: O(N) | Space Complexity: O(H)
'''
from typing import Optional

class Solution:
    def sumNumbers(self, root: Optional['TreeNode']) -> int:
        
        def dfs(node, total):
            if not node:
                return 0
            
            total = total * 10 + node.val
            if not node.left and not node.right:
                return total
            
            return dfs(node.left, total) + dfs(node.right, total)
        
        return dfs(root, 0)
    

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right