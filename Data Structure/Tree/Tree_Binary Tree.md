---
date: 2025-02-03
tags:
  - ds/tree
pageorder: 6.1
---
## Type of Binary Tree
Type1: [[Tree_Binary Tree#Full Binary Tree|Full Binary Tree]]
Type2: [[Tree_Binary Tree#Complete Binary Tree|Complete Binary Tree]]
Binary Search Tree
	Type3: [[Tree_Binary Tree#Balanced Binary Search Tree|Balanced Binary Search Tree]]
	Type4: [[Tree_Binary Tree#Unbalance Binary Search Tree|Unbalance Binary Search Tree]]

### Full Binary Tree
A **full binary tree** (also called a **strict binary tree**) is a type of binary tree where **every node has either 0 or 2 children**—never just one.
node = $2^{levels}-1$

```
        1
       /  \
      2    3
     / \  / \
    4   5 6  7
```
### Complete Binary Tree
>1. All levels except the last level are completely filled.
>2. The last level is filled from left to right, with no gaps.
```
        1
       /  \
      2    3
     / \  /
    4   5 6
```

### Binary Search Tree
>- Left Subtree Property: The left subtree of a node contains only nodes with **values smaller** than the node’s value.
>- Right Subtree Property: The right subtree of a node contains only nodes with **values greater** than the node’s value.
> - No Duplicates: Typically, BSTs do not allow duplicate values (though variations exist that handle duplicates differently).

#### Balanced Binary Search Tree
>The absolute difference between the depths (or heights) of the left and right subtrees of any node is at most 1.
- Time Complexity:$O(logN)$

```
        8
       / \
      4   12
     / \  /  \
    2   6 10  14
```
#### Unbalance Binary Search Tree
- Time Complexity: $O(n)$
```
    1
     \
      2
       \
        3
```

## Storage
- Linked Storage
- Linear Storage
### Linked Storage
In linked storage, each node of the tree contains **data** and **references (or pointers)** to its children and possibly to its parent. This allows the tree to be dynamically structured, with each node directly pointing to its children (and sometimes to its parent).

**How Trees Are Stored in Linked Storage**:
- Each node is represented by an object or structure that contains:
    - **Data**: The value or information stored in the node.
    - **Left/Right Child**: Pointers or references to the left and right children (for binary trees).
    - **Parent (optional)**: In some trees (like binary trees with parent pointers), a reference to the parent node is stored.
### Linear Storage
In linear storage, trees can be represented as a **flat array** or list. This approach is often used in **complete binary trees**, where the tree is stored in a linear sequence, and the relationships between nodes are derived from the indices.

**How Trees Are Stored in Linear Storage**:
In a **complete binary tree**, the tree can be stored in an array where:
- **Left Child** of index `i: 2i + 1`
- **Right Child** of index `i: 2i + 2`
- **Parent** of index `i`: `(i - 1) // 2`

## Tree Traversal
DFS (Depth-First Search)
- Pre-order Traversal
- In-order Traversal
- Post-order Traversal

BFS (Breadth-First Search)
- **层序遍历 (Level-order Traversal)**

#### Traversal Output:
```
        1
       /  \
      2    3
     / \   / \
    4   5 6   7
```
- Pre-order Traversal: (mid-left-right)
	1, 2, 4, 5, 3, 6, 7

- In-order Traversal: (left-mid-right)
	4, 2, 5, 1, 6, 3, 7

- Post-order Traversal: (left-right-mid)
	4, 5, 2, 6, 7, 3, 1

## Structure Tree
```python
class TreeNode: 
	def __init__(self, value): 
		self.value = value 
		self.left = None 
		self.right = None
```
