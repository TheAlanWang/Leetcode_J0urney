# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# O(n) O(h)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        ans = float('inf')

        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal prev, ans
            if not node:
                return
            inorder(node.left)
            if prev is not None:
                ans = min(ans, node.val - prev) 
            prev = node.val
            inorder(node.right)

        inorder(root)
        return ans
