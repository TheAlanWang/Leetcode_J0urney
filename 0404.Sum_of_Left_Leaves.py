# 0404.Sum_of_Left_Leaves

'''
Method1: Bottom-up DFS time: O(n) space: O(h)
Method2: Top-down DFS time: O(n) space: O(h) 
Method3: BFS Iterative  time: O(n) space: O(w)
'''
from typing import Optional

### Method1: DFS - top-down
class Solution:
    def sumOfLeftLeaves(self, root: Optional['TreeNode']) -> int:
        
        def dfs(node, is_left):
            if not node:
                return 0
            if is_left and not node.left and not node.right:
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        
        return dfs(root, False)

### Method2: DFS - bottom-up
class Solution:
    def sumOfLeftLeaves(self, root: Optional['TreeNode']) -> int:
        if not root: 
            return 0
        
        ans = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        
        if root.left and not root.left.left and not root.left.right:
            ans += root.left.val

        return ans
    
### Method3: BFS - Iterative
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional['TreeNode']) -> int:
        if root.left == None and root.right == None:
            return 0

        queue = deque()
        queue.append((root, False))
        total = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                node, flag = queue.popleft()

                if flag and not node.left and not node.right:
                    total += node.val

                if node.left:
                    queue.append((node.left, True))
                if node.right:
                    queue.append((node.right, False))
        
        return total
    


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right