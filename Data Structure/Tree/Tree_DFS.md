---
tags:
  - ds/tree
pageorder: 6.3
mainpage:
  - "[[DV_DataStructure]]"
---
>[!note]
**Depth-First Search (DFS)** explores the **depth** of the tree before exploring its breadth.

Three main types of DFS traversal in a tree:
1. **Pre-order Traversal**
2. **In-order Traversal**
3. **Post-order Traversal**
# Traversal
| Time Complexity              | Order  |                     |
| ---------------------------- | ------ | ------------------- |
| In order                     | $O(N)$ | Left → Node → Right |
| Pre order                    | $O(N)$ | Node → Left → Right |
| Postorder                    | $O(N)$ | Left → Right → Node |
| Build BST binary search tree | $O(N)$ |                     |
### Code
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def inorder(root):
    if not root:
        return    
    inorder(root.left)
    print(root.val)
    inorder(root.right)
 
def preorder(root):
    if not root:
        return    
    print(root.val)
    preorder(root.left)
    preorder(root.right)
 
def postorder(root):
    if not root:
        return    
    postorder(root.left)
    postorder(root.right)
    print(root.val)
```

<aside> 💡

Each recursive function call is stored in the **call stack** (LIFO - Last In, First Out).

</aside>