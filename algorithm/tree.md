# Tree
```
Tree
├── 1. Traversal
│   ├── LC 94   Binary Tree Inorder Traversal
│   ├── LC 144  Binary Tree Preorder Traversal
│   ├── LC 145  Binary Tree Postorder Traversal
│   ├── *LC 102  Binary Tree Level Order Traversal
│   └── LC 103  Binary Tree Zigzag Level Order Traversal
│   Idea: DFS (recursion/stack) and BFS (queue) are fundamental building blocks.
│
├── 2. Binary Search Tree (BST)
│   ├── LC 700  Search in a BST
│   ├── LC 98   Validate Binary Search Tree
│   ├── LC 701  Insert into a BST
│   ├── LC 450  Delete Node in a BST
│   ├── LC 235  Lowest Common Ancestor of BST
│   └── LC 530 / LC 783  Minimum Absolute Difference in BST
│   Idea: Exploit BST property `left < root < right`.
│
├── 3. Tree Construction
│   ├── LC 105  Construct Binary Tree from Preorder & Inorder
│   ├── LC 106  Construct Binary Tree from Inorder & Postorder
│   ├── LC 889  Construct Binary Tree from Preorder & Postorder
│   ├── LC 654  Maximum Binary Tree
│   └── LC 297  Serialize and Deserialize Binary Tree
│   Idea: Use traversal splits + recursion/hashmap.
│
├── 4. Depth / Height / Diameter
│   ├── LC 104  Maximum Depth of Binary Tree
│   ├── LC 111  Minimum Depth of Binary Tree
│   ├── LC 543  Diameter of Binary Tree
│   ├── LC 110  Balanced Binary Tree
│   └── LC 222  Count Complete Tree Nodes
│   Idea: Bottom-up recursion with height info.
│
├── 5. Path Problems
│   ├── LC 112  Path Sum
│   ├── LC 113  Path Sum II
│   ├── LC 437  Path Sum III
│   ├── LC 257  Binary Tree Paths
│   ├── *LC 404  Sum of Left Leaves
│   └── LC 124  Binary Tree Maximum Path Sum
│   Idea: DFS with path state (sum or list). Handle global max carefully.
│
├── 6. Lowest Common Ancestor (LCA)
│   ├── *LC 235  LCA of BST
│   └── *LC 236  LCA of Binary Tree
│   Idea: BST → compare values; General tree → recursion divide & conquer.
│
├── 7. Tree DP
│   ├── LC 96   Unique Binary Search Trees
│   ├── LC 95   Unique Binary Search Trees II
│   └── LC 337  House Robber III
│   Idea: Subtree DP, Catalan numbers, or DP with states on children.
│
└── 8. Advanced Trees
    ├── Trie
    │   ├── LC 208 Implement Trie (Prefix Tree)
    │   ├── LC 211 Design Add and Search Words Data Structure
    │   └── LC 212 Word Search II (Trie + DFS)
    │   Idea: Trie is useful for prefix/dictionary problems.
    │
    └── Segment/Fenwick Tree
        ├── LC 307 Range Sum Query – Mutable
        ├── LC 308 Range Sum Query 2D – Mutable
        └── LC 315 Count of Smaller Numbers After Self
        Idea: Specialized trees for range query & updates.
```