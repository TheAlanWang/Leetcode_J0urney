---
tags:
  - ds/backtracking
pageorder: 7
---
> [!NOTE]
    > Backtracking is a **recursive algorithmic technique** used to solve problems by exploring all possible solutions and discarding those that fail to satisfy constraints.
### Sample:

Q: Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes.

### Solution 1: return True or False

Logic:
- purpose: need go through each possibility, brute force
1. try left, if has zero, return to node
2. try right

```python
def canReachLeaf(root):
    if not root or root.val == 0:
        return False
    if not root.left and not root.right: # if reach the leafnode, return True
        return True
        
    if canReachLeaf(root.left): 
        return True
    if canReachLeaf(root.right):
        return True
    return False
```

### Solution 2: return Path
Logic:
1. Base case: If the node is `None` or has a value of `0`, return `False`.
2. Create Global variable `path`, add Node to Path: Append the current node's value to the `path` list.
3. If it is a leaf node (no left or right children), return `True`, as we found a valid path.
4. **Recursive Exploration**:
    1. Try **left subtree** (`leafPath(root.left, path)`)
    2. If left fails, try **right subtree** (`leafPath(root.right, path)`)
5. **Backtracking**: If both left and right subtrees fail, remove the last element from `path` and return `False`.
### code
```python
 def leafPath(root, path):
    if not root or root.val == 0:
        return False
    path.append(root.val)
 
    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False
```