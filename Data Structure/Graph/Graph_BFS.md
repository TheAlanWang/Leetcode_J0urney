---
tags:
  - ds/graph
pageorder: 10.3
---

Q: Find the length of the shortest path from the top left of the grid to the bottom right.

![image.png](attachment:5c83e849-1bfc-4b2c-8e22-93ed51c8b913:image.png)

```python
from collections import deque
 
# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]
 
# Shortest path from top left to bottom right
def bfs(grid):
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))
 
    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length
 
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1
```

### Why does BFS find the shortest path?

> BFS explores the graph layer by layer, starting from the source.
> 
> The first time it reaches the destination, it's guaranteed to be via the **shortest possible path** (in terms of number of steps or edges).
> 
> - never go though the same position twice

### Time Complexity

| Time complexity  | **O(m × n)** (each cell visited once) |
| ---------------- | ------------------------------------- |
| Space complexity | **O(m × n)** (queue and visit set)    |