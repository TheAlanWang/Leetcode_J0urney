---
tags:
  - ds/dp
pageorder: 11
---

### 1-Dimension-Fibonacci:

|Method|Approach|Technique|Time Complexity|Space Complexity|
|---|---|---|---|---|
|**Memoization**|Top-Down|Recursion|$O(n)$|$O(n) +$ recursion stack|
|**Tabulation/List**|Bottom-Up|Iteration|$O(n)$|$O(n)$|
|**Tabulation (Optimized)**|Bottom-Up|Iteration|$O(n)$|$O(1)$|

**Approach**
1. think in recursion
2. try memoization
3. dp

```python
# Brute Force
def bruteForce(n):
    if n <= 1:
        return n
    return bruteForce(n - 1) + bruteForce(n - 2)
 
# Memoization
def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
        return cache[n]
 
    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    return cache[n]
 
# Dynamic Programming
def dp(n):
    if n < 2:
        return n
 
    dp = [0, 1] # only use 2 element array
    i = 2
    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = tmp
        i += 1
    return dp[1]
```

- Q: In memoization, how the **`cache`** changes?
    
    > 1. `n = 5`, not in cache → calculate `memoization(4) + memoization(3)`
    > 
    > ### → `memoization(4, {})`
    > 
    > 2. `n = 4`, not in cache → calculate `memoization(3) + memoization(2)`
    > 
    > ### → `memoization(3, {})`
    > 
    > 3. `n = 3`, not in cache → calculate `memoization(2) + memoization(1)`
    > 
    > - → `memoization(2, {})`
    > 
    > 1. `n = 2`, not in cache → `memoization(1) + memoization(0)`
    >     - → `memoization(1)` → returns `1` (base case)
    >         
    >     - → `memoization(0)` → returns `0` (base case)
    >         
    >         ✅ So, `memoization(2)` = `1 + 0 = 1`
    >         
    >         🔁 **cache = {2: 1}**
    >         
    > 
    > - → `memoization(1)` → returns `1`
    >     
    >     ✅ So, `memoization(3)` = `1 (from 2) + 1 = 2`
    >     
    >     🔁 **cache = {2: 1, 3: 2}**
    >     
    > 
    > ### ← done with `memoization(3)`
    > 
    > - → `memoization(2)` → already in cache → return `1`
    >     
    >     ✅ So, `memoization(4)` = `2 (from 3) + 1 = 3`
    >     
    >     🔁 **cache = {2: 1, 3: 2, 4: 3}**
    >     
    > 
    > ### ← done with `memoization(4)`
    > 
    > → `memoization(3)` → already in cache → return `2`
    > 
    > ✅ So, `memoization(5)` = `3 (from 4) + 2 = 5`
    > 
    > 🔁 **cache = {2: 1, 3: 2, 4: 3, 5: 5}**
    

### 2-Dimension-Count paths:

Q: Count the number of unique paths from the top left to the bottom right. You are only allowed to move down or to the right.

![image.png](attachment:1ecf2eed-40e3-4da0-bd2b-69f0fb448877:215ef77f-67e1-4efb-9865-03f6f32fc7e8.png)

Only allowed move down to the right.

```python
# Brute Force - Time: O(2 ^ (n + m)), Space: O(n + m)
def bruteForce(r, c, rows, cols):
    if r == rows or c == cols:
        return 0
    if r == rows - 1 and c == cols - 1:
        return 1
     
    return (bruteForce(r + 1, c, rows, cols) +  
            bruteForce(r, c + 1, rows, cols))
 
print(bruteForce(0, 0, 4, 4))
 
# Memoization - Time and Space: O(n * m)
def memoization(r, c, rows, cols, cache):
    if r == rows or c == cols:
        return 0
    if cache[r][c] > 0:
        return cache[r][c]
    if r == rows - 1 and c == cols - 1:
        return 1
     
    cache[r][c] = (memoization(r + 1, c, rows, cols, cache) +  
        memoization(r, c + 1, rows, cols, cache))
    return cache[r][c]
 
print(memoization(0, 0, 4, 4, [[0] * 4 for i in range(4)]))
 
# Dynamic Programming - Time: O(n * m), Space: O(m), where m is num of cols
def dp(rows, cols):
    prevRow = [0] * cols
 
    for r in range(rows - 1, -1, -1):
        curRow = [0] * cols
        curRow[cols - 1] = 1
        for c in range(cols - 2, -1, -1):
            curRow[c] = curRow[c + 1] + prevRow[c]
        prevRow = curRow
    return prevRow[0]
```

- Q: How brute force function work?
    
    - This brute-force function **uses DFS to explore all paths**. It’s like DFS on a grid, trying every possible way to get to the bottom-right corner.
    - Time Complexity: $2^{m+n}$
- Q: Explain the memoization (bottom-up): $O(n * m)$
    
    cache: `[[0] * 4 for i in range(4)]` , store 4x4 matrix initialized
    
    ```python
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    [0, 0, 0, 0]
    ```
    
    ```python
    [ 0, 0, 0, 0 ]
    [ 0, 0, 0, 0 ]
    [ 4, 3, 2, 1 ]
    [ 1, 1, 1, 1 ]
    ```
    
    ```python
    [ 0, 0, 0, 0 ]
    [10, 6, 3, 1 ]
    [ 4, 3, 2, 1 ]
    [ 1, 1, 1, 1 ]
    ```
    
    ```python
    [20, 10, 4, 1]
    [10,  6, 3, 1]
    [ 4,  3, 2, 1]
    [ 1,  1, 1, 1]
    ```
    
    20 different ways
    
    **DP, Space Complexity**: O(cols)