### Q: When to use a `for` loop in backtracking, and when not?
1. Does the result require considering **every element** in order?
	- Yes → Each element must make a decision
	    - ✅ Use **recursion branching** (no `for`).
	    - Every element must make a *fixed decision* (usually two choices: yes/no, +/−, take/skip).
	    - Since every element must be considered, recursion simply branches on those fixed choices.
	    - Example: Target Sum (494), 0/1 Knapsack.
	- No → You can freely choose some elements, skip others.
	    - ✅ Use a **`for` loop** to iterate through candidates.
	    - At each recursion level, you freely choose from *multiple candidates* in the remaining elements.
	    - A `for` loop is used to iterate through these possible candidates.
	    - Example: Subsets (78), Permutations (46), Combination Sum (39), N-Queens.
2. At this recursion step, do I have a fixed set of choices, or do I need to explore many candidates?
	- Fixed small choices → **branch**.
	- Variable candidates → **loop**.

Whether you need a `for` loop in backtracking depends on **how many choices exist at each recursion step**.
if use `for`, means that result can start from the element, like subset.
# Backtracking
```
Backtracking
├── 1. Subsets / Combinations
│   ├── *LC 78  Subsets
│   ├── *LC 90  Subsets II (with duplicates)
│   ├── LC 39  Combination Sum
│   └── LC 40  Combination Sum II
│   Skill: decide “take or not take”, handle duplicates
│
├── 2. Permutations
│   ├── *LC 46  Permutations
│   ├── *LC 47  Permutations II (with duplicates)
│   └── LC 784 Letter Case Permutation (string version)
│   Skill: use `visited` to avoid reusing elements
│
├── 3. Partitioning / Splitting
│   ├── *LC 131 Palindrome Partitioning
│   ├── LC 93  Restore IP Addresses
│   └── LC 282 Expression Add Operators (harder)
│   Skill: cut input into segments, check validity
│
├── 4. Constraint Satisfaction Problems (CSP)
│   ├── LC 22  Generate Parentheses
│   ├── LC 51  N-Queens
│   ├── LC 37  Sudoku Solver
│   Skill: prune invalid branches early (constraints!)
```

## Framework:
1. Understand the problem
2. State
    - What information do I need to track at each step?
3. Choices (letters for current digit)
    - What options do I have at the current step?
4. Base case (when index == len(digits))
    - When should recursion stop?
5. Transition (append, recurse, pop)
    - How do I move to the next state?

## Permutation
### Leetcode:
- 0784.Letter_Case_Permutation