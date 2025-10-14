---
tags:
  - ds/set
pageorder: 2
---

> [!NOTE]
A set is an **unordered collection** of **unique** elements in Python. It is similar to a mathematical set and does **not allow duplicate values**.

### Set Operations

```python
# Creating a set
my_set = set()

# Adding elements
my_set.add(1)

# Removing elements
my_set.remove(1)  # raises error if not found
my_set.discard(1) # no error if not found

# Set operations
set1.union(set2)        # union
set1.intersection(set2) # intersection
set1.difference(set2)   # difference
```
