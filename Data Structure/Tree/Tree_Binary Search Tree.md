---
tags:
  - ds/tree
pageorder: 6.2
---


> [!note]
A **Binary Search Tree (or BST)** is a data structure used in computer science for organizing and storing data in a sorted manner.

- Each node in a **Binary Search Tree** has at most two children, a **left** child and a **right** child.
    - **Left** child < parent node
    - **right** child > parent node
- This hierarchical structure allows for efficient **searching**, **insertion**, and **deletion** operations on the data stored in the tree.

**Time Complexity**

|                   | Time Complexity  |                                                                     |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| Search            | $O(logn)/O(h)$   | if tree is balanced, and it can be O(h), h is the high of the tree. |
| Insert and remove | $O(logn)/O(h)$\| |                                                                     |

### Code

```python
	class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
def search(root, target):
    if not root:
        return False
     
    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True
```

### Sample:

7 < 8, wrong position

### Q: If we already have arrays, why do we still need **Binary Search Trees (BSTs)?**
- Array: Insertions and deletions require shifting elements, which takes $O(n)$ time.
- BST: Insertions and deletions take $O(log⁡n)$ time in a balanced BST (e.g., AVL Tree, Red-Black Tree) since we only traverse the tree down one path.

### BST - Insert and remove
```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
 
# Insert a new node and return the root of the BST.
def insert(root, val):
    if not root:          # if root in None
        return TreeNode(val)
     
    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root
 
# Return the minimum value node of the BST.
def minValueNode(root):
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr
 
# Remove a node and return the root of the BST.
def remove(root, val):
    if not root:
        return None
     
    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            minNode = minValueNode(root.right) # use the samllest value replace the removed node
            root.val = minNode.val
            root.right = remove(root.right, minNode.val)
    return root
```