---
tags:
  - ds/graph
pageorder: 10.4
---

```python
from collections import deque
 
# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []
 
# Or use a HashMap
adjList = { "A": [], "B": [] }
 
# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]
 
adjList = {}
 
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)
 
 
# Count paths (backtracking)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
     
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
 
    return count
 
# Shortest path from node to target
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)
 
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
 
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length
```

|Feature|**DFS**|**BFS**|
|---|---|---|
|**Search Strategy**|Go as deep as possible along a path first|Explore level by level (like ripples)|
|**Data Structure**|**Stack / Recursion (LIFO)**|**Queue (FIFO)**|
|**Shortest Path?**|❌ No guarantee (may find a longer path)|✅ Yes (in unweighted graphs/grids)|
|**Time Complexity**|O(V + E)|O(V + E)|
|**Space Complexity**|O(V) (call stack and visited set)|O(V) (queue and visited set)|
|**Use Cases**|Topological sort, path enumeration, maze|Shortest path, level order, peer discovery|
|**Path Finding**|Finds **all paths** (if needed, with backtracking)|Finds **shortest path**|
|**Typical Pattern**|Deep dive, then backtrack|Layer-by-layer|
