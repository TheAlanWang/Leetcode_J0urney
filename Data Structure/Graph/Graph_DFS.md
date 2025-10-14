---
tags:
  - ds/graph
pageorder: 10.2
---

Q: Count the unique paths from the top left to the bottom right. A single path may only move along O's and can't visit the same cell more than once.

![image.png](attachment:e22919db-3c69-426e-9f94-5bbb0c900696:0b4eaad9-5792-45bd-984b-361f7c3ffc4f.png)

```python
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
 
# Count paths (backtracking)
def dfs(grid, r, c, visit):
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1
 
    visit.add((r, c))
 
    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)
 
    visit.remove((r, c))
    return count
```

Time Complexity: $O(4^{m*n})$

Space Complexity: $O(m*n)$

Q: When `visit.add((r, c))` and `visit.remove((r, c))` ?

|Step|Action||
|---|---|---|
|`visit.add()`|Mark current cell|Prevent revisiting in current path|
|DFS calls|Explore all directions|Build different paths|
|`visit.remove()`|Unmark cell after DFS ends|Let other paths try it|