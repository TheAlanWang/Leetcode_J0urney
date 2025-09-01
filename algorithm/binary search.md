# Binary Search

```
Binary Search
├── 1. Classic search in sorted array
│   ├── LC 704  Binary Search
│   ├── LC 35   Search Insert Position
│   ├── LC 34   Find First and Last Position
│   └── LC 69   Sqrt(x) / LC 367 Valid Perfect Square
│   Idea: "while lo <= hi, mid=(lo+hi)//2, check arr[mid]"
│
├── 2. Search in rotated/shifted arrays
│   ├── LC 33   Search in Rotated Sorted Array
│   ├── LC 81   Search in Rotated Sorted Array II
│   Idea: array is sorted in 2 halves, decide which half is ordered.
│
├── 3. Binary Search on Answer (a.k.a. Parametric Search)
│   ├── LC 875  Koko Eating Bananas
│   ├── LC 410  Split Array Largest Sum
│   ├── LC 1482 Minimum Number of Days to Make m Bouquets
│   ├── *LC 1891 Cutting Ribbons
│   └── LC 1552 Magnetic Force Between Balls
│   Idea: search on feasible "value" (speed, length, days, capacity).
│
├── 4. Minimize/Maximize boundary problems
│   ├── LC 278  First Bad Version
│   ├── LC 162  Find Peak Element
│   ├── LC 852  Peak Index in a Mountain Array
│   └── LC 1095 Find in Mountain Array
│   Idea: find boundary or local peak by checking mid and neighbors.
│
├── 5. Matrix/Grid search
│   ├── *LC 74   Search a 2D Matrix
│   ├── LC 240  Search a 2D Matrix II
│   Idea: treat as sorted 1D array or eliminate rows/cols.
│
├── 6. Special data structures
│   ├── LC 4    Median of Two Sorted Arrays
│   ├── LC 378  Kth Smallest Element in a Sorted Matrix
│   ├── LC 287  Find the Duplicate Number (binary search on value)
│   Idea: binary search on indices, partitions, or value range.
```