---
tags:
  - ds/tree
pageorder: 6.4
mainpage:
  - "[[DV_DataStructure]]"
---

- & **Breadth-First Search (BFS)** is a tree traversal algorithm that explores the tree level by level (layer by layer), visiting all nodes at the current level before moving to the next level.

It explores the breadth (or width) of the tree rather than its depth, which is the opposite of Depth-First Search (DFS).

### Time Complexity:
| Method | Time Complexity |
| ------ | --------------- |
| BFS    | $O(n)$          |
| DFS    | $O(n)$          |

### **Logic:**

Purpose: process layer by layer, use iterative more fit

1. Use a queue (FIFO)
2. Put root into queue
3. Pop root, add children(node) into queue
4. Continue Popping and Adding

### Code:

```python
from collections import deque
 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def bfs(root):
    queue = deque()
 
    if root:
        queue.append(root)
     
    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.popleft()
            print(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
```