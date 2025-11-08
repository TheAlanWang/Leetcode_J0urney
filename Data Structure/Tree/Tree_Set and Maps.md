---
tags:
  - ds/tree
pageorder: 6.5
---

**Set and Map:**

are often implemented using **Binary Search Trees** because they allow for efficient **logarithmic** time complexity for insertion, deletion, and search operations.

**Set:**

- **Set** only stores **unique elements**.
- **Set implementation using Binary Search Trees (BSTs)**:
    - The **Binary Search Tree** (or its balanced variants like **Red-Black Trees** or **AVL Trees**) is often used to implement sets.
    - This ensures that each element can be **searched**, **inserted**, and **removed** in **O(log n)** time on average.

**Map:**

- Map (also known as a Dictionary) is a collection of key-value pairs where each key is unique.
- Map implementation using Binary Search Trees (BSTs):
    - BST is an efficient structure for mapping keys to values.
    - Searching for a key, inserting a key-value pair, and removing a key-value pair in a BST are all operations that take O(log n) time in a balanced tree.
    - The keys in a BST-based Map are stored in a sorted order, and you can efficiently search for values by looking up the keys.

|x|Package|
|---|---|
|python:|SortedDict|
|JavaScript:|Treemap-js|
|Java:|TreeMap|
|C++:|map|