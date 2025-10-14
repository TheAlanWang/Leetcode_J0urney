| Operation                 |                Time Complexity                | Notes                                         |
| ------------------------- | :-------------------------------------------: | --------------------------------------------- |
| `heapq.heappush(h, x)`.   |                 **O(log n)**                  | Insert and bubble up (`n` = heap size).       |
| `heapq.heappop(h)`        |                 **O(log n)**                  | Pop smallest and sift down.                   |
| `h[0]` (peek)             |                   **O(1)**                    | Read smallest without removing.               |
| `heapq.heapify(a)`        |                   **O(n)**                    | In-place build from a list.                   |
| `heapq.heapreplace(h, x)` |                 **O(log n)**                  | Pop smallest, then push `x` (size unchanged). |
| `heapq.heappushpop(h, x)` | **O(log n)** *(best **O(1)** if `x <= h[0]`)* | Push `x`, then pop and return the smallest.   |
## Heap
```
Heap
├── 1. Core Top-K / Order Statistics
│   ├── LC 215  Kth Largest Element in an Array
│   ├── LC 703  Kth Largest in a Stream
│   ├── LC 347  Top K Frequent Elements
│   └── LC 692  Top K Frequent Words
│   Idea: min-heap of size K for “largest”; freq map + (count, key) heap; custom tie-breakers.
│
├── 2. K-way Merge & Pairwise Sums
│   ├── LC 23   Merge k Sorted Lists
│   ├── LC 373  Find K Pairs with Smallest Sums
│   ├── LC 378  Kth Smallest in a Sorted Matrix
│   └── LC 632  Smallest Range Covering Elements from K Lists
│   Idea: push the “head” from each list/row; pop min, then push its neighbor.
│
├── 3. Nearest / Closest Points
│   ├── LC 973  K Closest Points to Origin
│   └── LC 658  Find K Closest Elements
│   Idea: max-heap of size K (keep best K); or two-pointer alternative for LC 658.
│
├── 4. Two-Heaps (Median / Quantiles)
│   ├── LC 295  Find Median from Data Stream ⭐
│   └── LC 480  Sliding Window Median
│   Idea: max-heap for lower half, min-heap for upper; rebalance; lazy deletion for windows.
│
├── 5. Greedy + Heap (Scheduling / Resources)
│   ├── LC 253  Meeting Rooms II (min-heap of end times)
│   ├── LC 630  Course Schedule III (max-heap of durations)
│   ├── LC 502  IPO (capital min-heap + profit max-heap)
│   ├── LC 621  Task Scheduler (max-heap counts + cooldown)
│   ├── LC 767  Reorganize String (max-heap counts)
│   ├── LC 1642 Furthest Building You Can Reach (min-heap climbs)
│   ├── LC 1705 Maximum Number of Eaten Apples (min-heap by expiry)
│   └── LC 1167 Minimum Cost to Connect Sticks (min-heap combine)
│   Idea: pick best available by a criterion; heap maintains current frontier/stock.
│
├── 6. Graph + Priority Queue
│   ├── LC 743  Network Delay Time (Dijkstra)
│   ├── LC 1631 Path With Minimum Effort (Dijkstra)
│   ├── LC 1514 Path with Maximum Probability (max-heap Dijkstra)
│   └── LC 1584 Min Cost to Connect Points (Prim’s MST)
│   Idea: PQ of (dist, node) or (weight, edge); relax edges / grow MST.
│
├── 7. Sweep Line / Heap with Lazy Deletion
│   ├── LC 218  The Skyline Problem
│   └── LC 2402 Meeting Rooms III / variants
│   Idea: process events in order; heap tracks active items; remove expired lazily.
│
└── 8. Design / Simulation with Heaps
    ├── *LC 355  Design Twitter (k-way merge via heap)
    └── LC 1845 Seat Reservation Manager (min-heap of free seats)
    Idea: heap maintains the “next” element to return (smallest ID / latest tweet, etc.).

```



