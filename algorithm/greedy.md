# Greedy Algorithm
- **Greedy Algorithm** is a problem-solving strategy where:
    - At each step, you choose the *locally optimal* option (the best choice at that moment)
    - With the hope that this will lead to a globally optimal solution (best overall answer).

```
Greedy
├── 1. Interval Scheduling / Ranges
│   ├── LC 435  Non-overlapping Intervals
│   ├── LC 452  Minimum Number of Arrows to Burst Balloons
│   ├── LC 56   Merge Intervals
│   ├── LC 763  Partition Labels
│   Idea: Sort by endpoint; always pick earliest finishing / valid split.
│
├── 2. Jump Game / Reachability
│   ├── LC 55   Jump Game
│   ├── LC 45   Jump Game II
│   Idea: Track farthest reachable index; expand window step by step.
│
├── 3. String / Lexicographic Choice
│   ├── LC 316  Remove Duplicate Letters
│   ├── LC 402  Remove K Digits
│   ├── LC 321  Create Maximum Number
│   Idea: Stack + greedy removal to maintain lexicographic order.
│
├── 4. Scheduling with Deadlines
│   ├── LC 630  Course Schedule III
│   ├── LC 871  Minimum Number of Refueling Stops
│   ├── LC 1353 Maximum Events Attended
│   Idea: Sort by deadline; use heap to keep feasible tasks/refuels.
│
├── 5. Coin Change / Resource Allocation
│   ├── LC 455  Assign Cookies
│   ├── LC 860  Lemonade Change
│   ├── LC 1005 Maximize Sum After K Negations
│   Idea: Match largest supply with largest demand; greedy exchange.
│
├── 6. Greedy with Sorting
│   ├── LC 406  Queue Reconstruction by Height
│   ├── LC 1029 Two City Scheduling
│   ├── LC 135  Candy
│   Idea: Sort array; assign greedily while respecting constraints.
│
├── 7. Greedy + Heap (Priority Queue)
│   ├── LC 502  IPO
│   ├── LC 857  Minimum Cost to Hire K Workers
│   ├── LC 621  Task Scheduler
│   Idea: Heap lets us always pick the best available option.
│
├── 8. Greedy + Prefix/Suffix
│   ├── LC 122  Best Time to Buy and Sell Stock II
│   ├── LC 605  Can Place Flowers
│   ├── LC 678  Valid Parenthesis String
│   Idea: Use prefix/suffix balance to validate local decisions.

```
Solving Template:
1. Choice (local decision)
    - The action/decision you take at each step using only the info you have now

2. State (compact tracker)
    - The minimal variables that summarize all past info you need to make the next choice

3. Greedy update
    - The rule that immediately updates the state from the current choice so far, without backtracking.


## Leetcode:
- 0045.Jump_Game_II
- 0300.Longest_Increasing_Subsequence
- 0376.Wiggle_Subsequence