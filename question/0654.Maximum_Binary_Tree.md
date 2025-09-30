# 654.Maximum_Binary_Tree
# Time complexity: O(n^2) | Space Complexity: O(n)

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def dfs(arr):
            if not arr:
                return
            
            num = max(arr)
            node = TreeNode(num)
            idx = arr.index(num)
            node.left = dfs(arr[:idx])
            node.right = dfs(arr[idx + 1:])
            return node
        
        
        return dfs(nums)