# Dynamic Programming
```
Dynamic Programming
├── 0. Essentials / Patterns
│   ├── State = what to remember; Transition = choice/cost; Base = trivial case
│   ├── Top-down (memo) ↔ Bottom-up (tabulation)
│   ├── Rolling array; Prefix/Gap DP
│   └── Idea: substructure & overlap, order of fill, dedup states
│
├── 1. 1D DP (Linear / Knapsack)
│   ├── *LC 70  Climbing Stairs
│   ├── *LC 198/213/337 House Robber I/II/III
│   ├── *LC 322  Coin Change                        [x]
│   ├── LC 518  Coin Change II
│   ├── *LC 300  Longest Increasing Subsequence
│   ├── LC 139  Word Break
│   ├── LC 279  Perfect Squares
│   └── Idea: iterate index i, try options; 0-1 vs Unbounded knapsack
│
├── Gap / Interval Scheduling
│   ├── LC 435  Non-overlapping Intervals
│   ├── LC 646  Maximum Length of Pair Chain
│   └── Idea: Sort by endpoint; always pick earliest finishing / valid split
│
├── 2. Jump Game / Reachability
│   ├── *LC 55  Jump Game
│   ├── *LC 45  Jump Game II
│   ├── LC 1306 Jump Game III
│   └── Idea: greedy max reach (or dp[i]=can reach); expand interval step by step
│
├── 3. 2D Grid DP (Paths / Costs)
│   ├── *LC 62/63  Unique Paths I/II
│   ├── *LC 64  Minimum Path Sum
│   ├── LC 120  Triangle
│   ├── LC 221  Maximal Square
│   ├── LC 174  Dungeon Game
│   └── Idea: dp[r][c] from top/left; obstacles; reduce to 1D
│
├── 4. String DP (Subsequence / Substring)
│   ├── *LC 1143  Longest Common Subsequence
│   ├── LC 583  Delete Operation for Two Strings
│   ├── *LC 72  Edit Distance
│   ├── *LC 5  Longest Palindromic Substring
│   ├── *LC 516  Longest Palindromic Subsequence
│   ├── LC 1312  Min Insertions to Palindrome
│   └── Idea: dp[i][j] on substrings/prefixes; match vs skip
│
├── 5. Partition / Subset DP
│   ├── *LC 416  Partition Equal Subset Sum
│   ├── *LC 494  Target Sum
│   ├── LC 474  Ones and Zeroes (2D knapsack)
│   └── Idea: subset reachability; boolean or capacity dp
│
├── 6. Interval / Range DP
│   ├── *LC 312  Burst Balloons
│   ├── *LC 1547  Min Cost to Cut a Stick
│   ├── *LC 486 / 877 Predict the Winner / Stone Game
│   └── Idea: loop by length/gap; split k between (i,k) & (k,j)
│
├── 7. Palindrome Partitioning / Parsing
│   ├── *LC 132  Palindrome Partitioning II (min cuts)
│   ├── LC 131  Palindrome Partitioning I (all partitions)
│   └── Idea: precompute palindrome table; dp[i] = min cuts to i
│
├── 8. DP on Trees
│   ├── *LC 337  House Robber III
│   ├── LC 124  Binary Tree Max Path Sum
│   ├── LC 968  Binary Tree Cameras
│   └── Idea: postorder; return tuple (include/exclude/state)
│
├── 9. Bitmask DP (Subsets / TSP-style)
│   ├── *LC 698  Partition to K Equal Sum Subsets
│   ├── *LC 847  Shortest Path Visiting All Nodes
│   ├── LC 1125  Smallest Sufficient Team
│   └── Idea: dp[mask] = best for subset; combine by adding element
```