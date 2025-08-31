# Graph
```
Graph
├── 1. Traversal / Connectivity
│   ├── LC 200  Number of Islands
│   ├── LC 133  Clone Graph
│   ├── LC 417  Pacific Atlantic Water Flow
│   ├── LC 261  Graph Valid Tree
│   └── LC 684  Redundant Connection
│   Idea: DFS / BFS to explore components; detect cycle with parent check or Union-Find.
│
├── 2. Shortest Path
│   ├── BFS (unweighted graphs)
│   │   ├── LC 127   Word Ladder
│   │   └── LC 1091  Shortest Path in Binary Matrix
│   ├── Dijkstra (non-negative weights)
│   │   ├── LC 743   Network Delay Time
│   │   └── LC 1631  Path With Minimum Effort
│   ├── Bellman-Ford (allows negative weights)
│   │   └── LC 787   Cheapest Flights Within K Stops
│   └── Floyd-Warshall (all-pairs shortest path)
│       └── LC 1334  Find the City With the Smallest Number of Neighbors
│   Idea: choose algorithm based on edge weights & graph size.
│
├── 3. Topological Ordering (DAG only)
│   ├── LC 207  Course Schedule I
│   ├── LC 210  Course Schedule II
│   └── LC 269  Alien Dictionary
│   Idea: use indegree + queue (Kahn’s algorithm) or DFS finishing order.
│
├── 4. Union-Find / Disjoint Set
│   ├── LC 323  Number of Connected Components
│   ├── LC 684  Redundant Connection
│   └── LC 1584 Min Cost to Connect All Points
│   Idea: DSU supports find + union; use for cycle detection & MST.
│
├── 5. Minimum Spanning Tree (MST)
│   ├── Kruskal → LC 1584 Min Cost to Connect All Points
│   └── Prim   → LC 1135 Connecting Cities With Minimum Cost
│   Idea: Kruskal = sort edges + Union-Find; Prim = grow tree with PQ.
│
├── 6. Flow / Matching (advanced)
│   ├── Max Flow (Ford-Fulkerson, Edmonds-Karp)
│   └── Bipartite Graph Check → LC 785 Is Graph Bipartite?
│   Idea: model as capacity graph; used in matching / scheduling problems.
│
├── 7. Tree-specific (Tree is Graph)
│   ├── LC 236  Lowest Common Ancestor
│   ├── LC 543  Diameter of Binary Tree
│   └── LC 297  Serialize and Deserialize Binary Tree
│   Idea: Tree = special graph; DFS recursion is natural tool.
│
└── 8. Special Graph Structures
    ├── Grids as Graphs
    │   ├── LC 994  Rotting Oranges
    │   └── LC 542  01 Matrix
    └── State Graphs
        ├── LC 127  Word Ladder
        ├── LC 773  Sliding Puzzle
        └── LC 37   Sudoku Solver
    Idea: Convert problem state → nodes; neighbors = valid moves.
```
# Graph
A **graph** is a data structure composed of nodes(vertices) connected by edges.

## BFS

### Leetcode:
- 0261.Graph_Valid_Tree
- 0695.Max_Area_of_Island

## Topological sort
**Topological sort** is defined only for DAGs (Directed Acyclic Graphs)

### Leetcode:
- 0210.CourseSchedule_II

