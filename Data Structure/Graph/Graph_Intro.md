---
tags:
  - ds/graph
pageorder: 10.1
---
### Edges, Vertices

$Edges≤V^2$

The total number of edges is less than or equal to the square of the number of vertices.

- A directed graph can have at most V² edges (each node can connect to every other node, including itself).
- An undirected graph has a maximum of V × (V - 1) / 2 edges (no duplicate or self-edges).

|**Concept**|**Think of it like...**|
|---|---|
|Matrix|A general-purpose table/grid of values|
|**Adjacency Matrix**|A special matrix where values mean "connected or not"|
|**Adjacency List**|A contact list showing who each node is connected to|

### Matrix

<aside> 💡

A **matrix** is a rectangular arrangement of numbers, symbols, or expressions, organized in rows and columns.

</aside>

row, column

![image.png](attachment:89a44627-c9ae-43fd-bcdf-eee54f8666d7:image.png)

Undirected

```python
# Creating a 2x2 matrix in Python using a list of lists
matrix = [
    [1, 2],
    [3, 4]
]
print(matrix[0][1])  # Outputs: 2
```

### Adjacency Matrix

much less common

The dimension represents node

- For **unweighted graphs**: `matrix[i][j] = 1`
- For **weighted graphs**: `matrix[i][j] = weight`
- If there is **no edge**, `matrix[i][j] = 0`

![image.png](attachment:fb63db1a-25f0-4df1-b964-68196d28fe28:image.png)

### Adjacency List

```python
class GraphNode:
	def __init__(self, val):
		self.val = val
		self.neighbors = []
		
adj_list = {
    0: [1, 2],
    1: [0],
    2: [0]
}
```

This says:

- Node 0 connects to 1 and 2
- Node 1 connects to 0
- Node 2 connects to 0

|Feature|Adjacency Matrix|Adjacency List|
|---|---|---|
|Space|O(V²)|O(V + E)|
|Good for|Dense graphs|Sparse graphs|
|Check edge existence|O(1)|O(k), k = neighbors|
|Easy to iterate edges|❌|✅|