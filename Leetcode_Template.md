## 1.Array&Hashing
### 1.1 List/Matrix Initialization
```python
# [0, 0, 0, ..., 0]
array = [0] * 26

# [[], [], [], []]
bucket_sort = [[] for _ in range(n)] 

# rows * cols
'''
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
'''
matrix = [[0 * len(column) for row in rows]

# Lists, dictionaries, and sets are mutable—avoid initializing them in a way that shares the same memory address.
```

## 2.Two Pointers (Sorted Array)
```python
left, right = 0, len(arr) - 1
while left < right:
    total = arr[left] + arr[right]
    if total == target: # Found a pair or valid condition
        # Do something with arr[left], arr[right]
        left += 1
        right -= 1
    elif total < target:
        left += 1
    else:  # total > target
        right -= 1
```

LC: [11.Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)
### Two Pointers (skip duplicate)
LC: [15.3Sum ](https://leetcode.com/problems/3sum/description/)
```python
def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate for i
        target = -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]: # compare to last one
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1
    return res
```
- TC: O($n^2$) | SC: O(1)
## 3.Sliding Window
### 1.1 Fixed Size
```python
left = right = 0

while right < n:
    # prcess the current window (right) Eg: cur_sum += nums[right]
    if right - left + 1 == fixed_window_size:
        # process the current window to get the result
        result = max(res, process_current_window)
        # process Eg: max_sum = max(max_sum, cur_sum)
        # shrink the window from the left Eg: cur_sum -= nums[left]
        left += 1
    
    right += 1
return result
```
### 1.2 Variable Size
- Time Complexity is O(n)
	- O(n + n), right increments up to n, left increments up to n. Each character is processed at most twice
- Space complexity: **O(1)** (if no extra data structures like hash maps or sets are used)

### 121. Best Time to Buy and Sell Stock
LC: [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
```python
def maxProfit(self, prices: List[int]) -> int:
    buy_price = float('inf')  # 初始化买入价格为无穷大
    max_profit = 0            # 初始化最大利润为 0
    
    for i in range(len(prices)):
        if prices[i] < buy_price:
            buy_price = prices[i]  # 找到更低的买入价
        
        cur_profit = prices[i] - buy_price  # 当前价格卖出所能获得的利润
        max_profit = max(max_profit, cur_profit)  # 更新最大利润
    
    return max_profit
```
TC: O(n) | SC:O(1)

### 3.Longest_Substring_Without_Repeating_Characters
LC:[3.Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)
```python
def lengthOfLongestSubstring(self, s: str) -> int:
    left = right = 0
    visited = set()
    res = 0
    while right < len(s):
        if s[right] not in visited:
            res = max(res, right - left + 1)
        while s[right] in visited:
            visited.remove(s[left])
            left += 1
        visited.add(s[right])
        right += 1
    return res
```
- TC: O(n) | SC: O(k)
### 567.Permutation in String
LC: [567.Permutation in String](https://leetcode.com/problems/permutation-in-string/description/)
```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False

        base = ord('a')
        need = [0] * 26
        win  = [0] * 26

        for ch in s1:
            need[ord(ch) - base] += 1
        for i in range(m):
            win[ord(s2[i]) - base] += 1

        matches = 0
        for i in range(26):
            if need[i] == win[i]:
                matches += 1
        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            r = ord(s2[i]) - base
            l = ord(s2[i - len(s1)]) - base

            # add right
            prev = win[r]
            win[r] += 1
            if win[r] == need[r]:
                matches += 1
            elif prev == need[r]:
                matches -= 1

            # remove left
            prev = win[l]
            win[l] -= 1
            if win[l] == need[l]:
                matches += 1
            elif prev == need[l]:
                matches -= 1

            if matches == 26:
                return True

        return False
```
- TC: O(n) | SC: O(1)

### 239. Sliding Window Maximum
LC: [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
```python
def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    queue = deque() # store idx
    res = []
    
    right = 0
    while right < len(nums):
        while queue and nums[right] > nums[queue[-1]]:
            queue.pop()
        queue.append(right)
        # idx should between [left, right]
        left = right - k + 1  # k = right - left + 1
        if queue[0] < left:   # when idx out of windows, pop
            queue.popleft()
        if left >= 0:
            res.append(nums[queue[0]]) 
        right += 1
    return res
```
- TC: O(n) | SC: O(n)
## 4.Binary Search
> [!note] Use binary search when your **search space has structure** (sorted, monotonic, or searchable by comparing mid with target) 
### 4.1 Exact Match
```python
left, right = 0, len(arr) - 1  # closed interval [left, right]
res = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        res = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return res
```
LC: [[0033.Search_in_Rotated_Sorted_Array]] [[0153.Find_Minimum_in_Rotated_Sorted_Array]]
### lower_bound
- binarysearch_left, 最左边 **≥ target**
```python
left, right = 0, len(arr) - 1
res = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] >= target:
	    res = mid
        right = mid -1
    else:
        left = mid + 1

return res
```
- `[1, 2, 2, 3]` : find 2, idx = 1
- `[1, 3]` : find2, idx =  1,  return 3
### higher_bound
- binary search_right, 最右边 **≤ target**
```python
left, right = 0, len(arr) - 1
res = -1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] <= target:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

return res
```
- `[1, 2, 2, 3]` : find 2, idx = 2
- `[1, 3]` : find 2, idx = 0, return 1
## 4.Median of Two Sorted Arrays
- LC: [Median of Two Sorted Arrays - LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/description/)
```python
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    long_num = nums1
    short_num = nums2
    
    if len(long_num) < len(short_num):
        long_num, short_num = short_num, long_num
    
    len_short, len_long = len(short_num), len(long_num)

    total_size = len_long + len_short
    half_size = (total_size + 1) // 2

    left_short_idx, right_short_idx = 0, len_short

    while left_short_idx <= right_short_idx:
        cut_short_idx = (left_short_idx + right_short_idx) // 2
        cut_long_idx = half_size - cut_short_idx

        min_short = short_num[cut_short_idx-1] if cut_short_idx > 0 else float('-inf')
        max_short = short_num[cut_short_idx] if cut_short_idx < len_short else float('inf')
        min_long = long_num[cut_long_idx-1] if cut_long_idx > 0 else float('-inf')
        max_long = long_num[cut_long_idx] if cut_long_idx < len_long else float('inf')

        if min_short <= max_long and min_long <= max_short:
            if total_size % 2 == 1: # odd
                return max(min_short, min_long)
            else:
                first = max(min_short, min_long)
                second = min(max_short, max_long)
                return (first + second) / 2.0
        
        if min_short > max_long:
            right_short_idx = cut_short_idx - 1
        else:
            left_short_idx = cut_short_idx + 1
    
    return 0.0

```
## 5.Stack
### 155.Min Stack
LC: [155.Min Stack](https://leetcode.com/problems/min-stack/description/)
```python
class MinStack
    def __init__(self): 
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None: # O(1)
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None: # O(1)
        val = self.stack.pop()
        if val == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int: # O(1)
        return self.stack[-1]

    def getMin(self) -> int:# O(1)
        return self.minstack[-1]
```
### 853.Min Stack
LC: [853. Car Fleet](https://leetcode.com/problems/car-fleet/)
```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x:x[0], reverse=True)

        stack = []
        for pos, spd in cars:
            t = (target - pos) / spd
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)
```
- TC: O(nlogn) | SC: O(n)
## 6.Linked List
### 19.Remove Nth Node From End of List
LC: [19.Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)
```python
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head:
        return []
    
    # Step 1: get length of linked list
    len_ll = 0
    cur = head
    while cur:
        cur = cur.next
        len_ll += 1
    
    # Step 2: use dummy node for edge cases (like deleting head)
    dummy = ListNode(0, head)
    tail = dummy
    for _ in range(len_ll - n):
        tail = tail.next

    # Step 3: skip the target node
    tail.next = tail.next.next

    return dummy.next
```
- TC: O(n) | SC: O(1)
### Merge Two Sorted Lists
```python
dummy = ListNode(-1)
tail = dummy  # Tail will point to the last node of the merged list

while list1 and list2:                 # Traverse both lists while both are not empty
    if list1.val <= list2.val:
        tail.next = list1             # Append list1 node
        list1 = list1.next            # Move list1 forward
    else:
        tail.next = list2             # Append list2 node
        list2 = list2.next            # Move list2 forward
    tail = tail.next                  # Move tail forward

tail.next = list1 if list1 else list2 # Attach the remaining nodes

return dummy.next # Return the head of the merged list (skipping the dummy node)
```
## 7.Trees
### Tree Traversal
#### DFS: Traversal
```python
def dfs(node):
    if not node:
        return
    # Preorder: process node before children: process(node)
    dfs(node.left)
    # Inorder: process node between left and right: process(node)
    dfs(node.right)
    # Postorder: process node after children: process(node)  
```
- Time complexity is O(n)
- Space complexity: **O(h)**
	- Best case: O(log n) – complete binary tree
	- Worst case: O(n) – tree sharp like a linked list
##### DFS: Use Pre&Inorder Traversal
```python
inorder_index = {val: idx for idx, val in enumerate(inorder)} # inorder convert to dic
self.pre_idx = 0  # Pointer to current root in preorder

def helper(left: int, right: int) -> Optional[TreeNode]:
    if left > right: # Base case: no elements to construct subtree
        return None

    root_val = preorder[self.pre_idx] # Step 2: Pick current root from preorder
    self.pre_idx += 1                 # move to the **next root node
    root = TreeNode(root_val)
    idx = inorder_index[root_val]     # Step 3: Split inorder into left and right parts
    root.left = helper(left, idx - 1) # Step 4: Build left and right subtrees recursively
    root.right = helper(idx + 1, right)
    return root
    
return helper(0, len(inorder) - 1) # Initial recursive call with full inorder range
```
LC: [105.Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
- Time complexity: O(n) | Space complexity: O(n)
#### BFS: Level Order Traversal
```python
if not root:
    return []
result = []
queue = deque([root])
while queue:
    level = []
    for _ in range(len(queue)):
        node = queue.popleft()
        level.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.append(level) 
return result 
```
LC: [102.Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
- Time complexity:O(n) | Space complexity: O(w), worst-case: O(n)
	- **w = maximum width** of the binary tree
---
### DFS: Max Depth
```python
def dfs(node):
    if not node:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)
    return max(left, right) + 1
```
LC: [104.Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) TC/PC: O(n)
### DFS: Invert binary Tree
```python
if not root:
    return None
queue = deque()
queue.append(root)
while queue:
    node = queue.popleft()
    node.left, node.right = node.right, node.left
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)

return root
```
LC: [226.Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)
TC/PC: On On
###  BFS + DFS: Subtree of Another Tree
```python
def is_same_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.val != tree2.val:
        return False
    return is_same_tree(tree1.left, tree2.left) and is_same_tree(tree1.right, tree2.right)

if not root:
    return False

queue = deque()
queue.append(root)
while queue:                               # Space complexity:O(m)
    node = queue.popleft()
    if node.val == subRoot.val:
        if is_same_tree(node, subRoot):    # Time Complexityis O(m*n)
            return True                    # call m times O(n)funtion
    
    if node.left:
        queue.append(node.left)
    if node.right:
        queue.append(node.right)
```

LC: [572.Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/) TC: O`(m*n)` SC: O(m)
### DFS: Lowest Common Ancestor
**LCA in Binary Search Tree**
```python
def dfs(node):
    if not node:
        return None
    if p.val < node.val and q.val < node.val:
        return dfs(node.left)
    elif p.val > node.val and q.val > node.val:
        return dfs(node.right)
    else:
        return node
```
LC: [235.Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/) TC: O(h) SC: O(h)

**LCA in Binary Tree**
```python
def dfs(node):
    if not node:
        return None
    if node == p or node == q:  # If we find either p or q, return the node
        return node
    left = dfs(node.left)       # Search left subtree
    right = dfs(node.right)     # Search right subtree
    if left and right:          # If both left and right return a node, this is the LCA
        return node
    return left if left else right # If one side returns a node, return that node 
```
LC: [236.Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/) TC: O(n) SC: O(h)
### DFS: Path Validity
```python
def dfs(node, cur_path):  # cur_path holds the current path state (e.g., sum, list, length)
    if not node:          # 1. Base case: null node means no further path
        return False

    cur_path += node.val  # 2. Update path state (e.g., add current node value to path sum)

    # 3. If it's a leaf node, check if the condition is satisfied
    if not node.left and not node.right:
        return cur_path == target

    # 4. Recurse on left and right children
    return dfs(node.left, cur_path) or dfs(node.right, cur_path)
```
### DFS: maxPathSum
```python
self.max_sum = float('-inf')  # Global maximum path sum

def dfs(node):
    if not node:
        return 0

    # Step 1: Get max gain from left and right (ignore negatives)
    left_gain = max(dfs(node.left), 0)
    right_gain = max(dfs(node.right), 0)

    # Step 2: Update max_sum if current path (split at node) is better
    current_path_sum = node.val + left_gain + right_gain
    self.max_sum = max(self.max_sum, current_path_sum)

    # Step 3: Return ONE-SIDE gain to parent (can't split at parent)
    return node.val + max(left_gain, right_gain)

dfs(root)
return self.max_sum
```
- LC: [124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)
### DFS: Path accumulation
##### DFS: Immutable
```python
def dfs(node, path_state):
    if not node:
        return 0

    # path_state = update(path_state, node.val)
    if not node.left and not node.right:       # is_leaf(node):
        return use_or_record(path_state)

    left_result = dfs(node.left, path_state)
    right_result = dfs(node.right, path_state)

   return left_result + right_result           # combine(left_result, right_result)
```
- Time complexity: O(n) | Space complexity: O(h)
##### DFS: Context Tracking
This DFS passes `parent` and `grandparent` as arguments (immutable state).
```python
def dfs(node, parent=None, grandparent=None):
    if not node:
        return base_case_value

    # Use context to compute this node’s contribution
    current_contribution = some_logic(node, parent, grandparent)
    
    left = dfs(node.left, node, parent)      # Recurse
    right = dfs(node.right, node, parent)    # Recurse

    return current_contribution + left + right
```
##### DFS: Backtracking
```python
def dfs(node, path, res):
    if not node:
        return

    path.append(node.val)

    if not node.left and not node.right:    # whether the current node is a leaf node
        res.append(list(path))              # record path

    dfs(node.left, path, res)
    dfs(node.right, path, res)

    path.pop()                              # Backtrack
```
- Time complexity is O(n)
- Space complexity: O(h)
LQ: [988.Smallest String Starting From Leaf - LeetCode](https://leetcode.com/problems/smallest-string-starting-from-leaf/)
##### BFS: Path Accumulation
```python
def bfs_with_path(root):
    if not root:
        return []

    res = []
    queue = deque()
    queue.append((root, [root.val]))
    while queue:
        node, path = queue.popleft()
        
        if not node.left and not node.right:      # Leaf node: store the path
            res.append(path)

        # Add children to queue with extended path
        if node.left:
            queue.append((node.left, path + [node.left.val]))
        if node.right:
            queue.append((node.right, path + [node.right.val]))

    return res

```
- Time complexity is O(n$^2$)
- Space complexity is O(n$^2$))
## 8.Heap / Priority Queue
```python
# heappush()
# heapq use the first element 'count' as primary key
heapq.heappush(heap, (count, num)) # TC: O(logk) k: size of heap

# heappop()
# pop the smallest
heapq.heappop(heap) # TC: O(logn)

# heapify
arr = [4, 10, 3, 5, 1]
heapify(arr)             # O(n)
```
### min-heap
```python
def topK(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)            # pop smallest
    return [num for freq, num in heap]     # contains K largest (not sorted)
```
- Time complexity: O(nlogk)
lc: [347.Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
### MedianFinder with Two Heaps
```python
def __init__(self):
    self.max_heap = []
    self.min_heap = []
def addNum(self, num: int) -> None:
    # Step 1: Always push to max_heap first
    heapq.heappush(self.max_heap, -num)
    # Step 2: Balance ordering — push max of max_heap to min_heap
    heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
    # Step 3: Maintain size property (max_heap >= min_heap)
    if len(self.min_heap) > len(self.max_heap):
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

def findMedian(self) -> float:
    if len(self.max_heap) > len(self.min_heap):
        return -self.max_heap[0]
    else:
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```
addNum: TC: O(logn)  SC: O(n)
lc: [295.Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/description/)
## 9.Backtracking
### 78.Subsets
LC: [78.Subsets](https://leetcode.com/problems/subsets/description/)
```python
def subsets(self, nums: List[int]) -> List[List[int]]:
    res = []
    def backtrack(idx, path):
        res.append(path[:])
        for i in range(idx, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    
    backtrack(0, [])
    return res
```
- TC:O($2^n * n$) | SC: O($2^n * n$)
### Combination Sum
```python
res = []
def backtrack(cur_sum, idx, path):
    if cur_sum > target:
        return
    
    if cur_sum == target:
        res.append(path[:])
        return
    
    for idx in range(idx, len(candidates)): # start idx
        cur_sum += candidates[idx]
        path.append(candidates[idx])
        backtrack(cur_sum, idx, path)
        
        cur_sum -= candidates[idx]
        path.pop()

backtrack(0, 0, [])
return res
```
- Time complexity is O(2$^{T/m}$) | Space complexity is O(T)
	- `T` = target
	- `m` = smallest number in candidates 
LC: [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

### DFS + Backtracking: Grid Search Template
```python
rows, cols = len(board), len(board[0])
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def backtrack(r: int, c: int, idx: int, visited: set) -> bool:
    if idx == len(word):
        return True

    if (
        not (0 <= r < rows and 0 <= c < cols)
        or board[r][c] != word[idx]
        or (r, c) in visited
    ):
        return False

    visited.add((r, c))            
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if backtrack(nr, nc, idx + 1, visited):
            return True

    visited.remove((r, c))  # 🔁 backtrack
    return False

for r in range(rows):
    for c in range(cols):
        if board[r][c] == word[0]:
            if backtrack(r, c, 0, set()):
                return True

return False
```
LC: [79. Word Search](https://leetcode.com/problems/word-search/description/) 
TC:O($N * M * 4^L$) | Space Complexity: O(L) -> L = length of the word

### 22. Generate Parentheses
LC: [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
```python
def generateParenthesis(self, n: int) -> List[str]:
    # backtracking
    res = []
    def backtrack(path, left, right):
        if left <= 0 and right <= 0:
            res.append("".join(path))
            return
        
        if left > 0:
            path.append("(")
            backtrack(path, left - 1, right)
            path.pop()
        
        if right > left:
            path.append(")")
            backtrack(path, left, right - 1)
            path.pop()
        
    
    backtrack([], n, n)
    return res
```

## 10.Trie (Prefix Tree)
> [!note] 
> **Trie**: a *tree-like* data structure, used to efficiently store and retrieve strings. 
> - TrieNode structure(By default): children = { }, end_of_word = False
> - Each node represents a single character.
### Implement Trie 
```python
class TrieNode:
    def __init__(self):
        self.children = {}            # key: char, value: TrieNode
        self.end_of_word = False      # marks the end of a complete word

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None

    def _traverse(self, string: str) -> TrieNode | None:
        node = self.root
        for ch in string:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```
LC: [208.Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)
Time Complexity:
- insert(word): O(L)
- search(word): O(L)
- startsWith(prefix): O(L)

### Trie: Design Add and Search Words Data Structure 
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
	
	### method 1
    def search(self, word: str) -> bool:
        def dfs(idx: int, node: TrieNode):
            for i in range(idx, len(word)): # continue where it left off
                if word[i] == '.':
                    for child in node.children.values(): # try every possible child node
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if word[i] not in node.children:
                        return False
                    node = node.children[word[i]]
            return node.end_of_word
        
        return dfs(0, self.root)
	### method 2
    def search(self, word: str) -> bool:
        cur = self.root
        def helper(cur, idx):
            if idx == len(word):
                return cur.end_of_word
            if word[idx] == '.':
                for node in cur.children.values():
                    if helper(node, idx + 1):
                        return True
                    return False
            else:
                if word[idx] not in cur.children:
                    return False
                return helper(cur.children[word[idx]], idx + 1)
        return helper(cur, 0)
```
LC: [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
- Time complexity: O(n) | Space complexity: O($t*n$) 
	- t: total words inserted
### Trie+DFS: Word Search II
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.full_word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def imple_trie(words: list): # Step 1: Build Trie O(W × L)
            root = TrieNode()
            for word in words:
                cur = root
                for c in word:
                    if c not in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.full_word = word
            return root
        
        root = imple_trie(words)

        res = []
        rows, cols = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        def dfs(r, c, node, visited):       # Step 2: DFS with visited set
            if (
                not(0 <= r < rows and 0 <= c < cols) or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return 
            
            visited.add((r, c))
            
            node = node.children[board[r][c]] # [r][c] in node.children, move to child, check
            if node.full_word:
                res.append(node.full_word)
                node.full_word = None         # Avoid duplicates

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, node, visited)

            visited.remove((r, c))

        for r in range(rows):                 # Step 3: Start DFS from each cell
            for c in range(cols):
                dfs(r, c, root, set())        # O(M × N × 4^L)
        
        return res
```
LC: [212.Word Search II](https://leetcode.com/problems/word-search-ii/)
- Time Complexity: O($w*l+m*n*4^L$)
	- `M`, `N` = number of rows and columns in `board`
	- `W` = number of words in `words`
	- `L` = average length of each word
- Space Complexity: O($w*l +l$)
## 11.Graphs
```
# Adjacency list:
	graph = {
	    0: [1, 2],
	    1: [0, 2],
	    2: [0, 1],
	}
```
### 133.Clone Graph
```python
def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    if not node:
        return None

    visited = {}  # Maps original node → cloned node
    queue = deque([node])
    visited[node] = Node(node.val)

    while queue:
        cur = queue.popleft()
        for nei in cur.neighbors:
            if nei not in visited:
                visited[nei] = Node(nei.val)  # Clone neighbor
                queue.append(nei)
            visited[cur].neighbors.append(visited[nei])  # **always Link clone

    return visited[node]
```
LC: [133.Clone Graph](https://leetcode.com/problems/clone-graph/description/)
- Time Complexity: O(n+e) | Space Complexity: O(n)
### 417.Pacific Atlantic Water Flow
> [!note]
> Instead of simulating water flow from each cell, use BFS to find all cells which water can reach that ocean.
> - use visited_set to record `nr, nc` that can reach the ocean from starting point (r, c)

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def bfs(queue: deque, visited: set):
            while queue:
                row, col = queue.popleft()
                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        heights[new_row][new_col] >= heights[row][col] and
                        (new_row, new_col) not in visited
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

        pacific_visited, atlantic_visited = set(), set()
        pacific_que, atlantic_que = deque(), deque()

        for r in range(rows):
            pacific_visited.add((r, 0))
            pacific_que.append((r, 0))
            atlantic_visited.add((r, cols - 1))
            atlantic_que.append((r, cols - 1))

        for c in range(cols):
            pacific_visited.add((0, c))
            pacific_que.append((0, c))
            atlantic_visited.add((rows - 1, c))
            atlantic_que.append((rows - 1, c))

        bfs(pacific_que, pacific_visited)
        bfs(atlantic_que, atlantic_visited)

        result = [[r, c] for (r, c) in pacific_visited & atlantic_visited]
        return result
```
LC: [Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/description/)
### Course Schedule
> [!note]
> - build graph as an adjacency list, and count the in_degree of each node
> - initialize the graph{pre:course} , for bfs to find the next course

```python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Step 1: Build the graph (adjacency list) and in-degree array
    dic = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prerequisite in prerequisites:
        dic[prerequisite].append(course)
        in_degree[course] += 1

    # Step 2: Initialize queue with courses that have no prerequisites
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)

    # Step 3: Process nodes using BFS
    completed_c = 0
    while queue:
        current_course = queue.popleft()
        completed_c += 1
        for nei in dic[current_course]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)

    return completed_c == numCourses
```
LC: [207.Course Schedule](https://leetcode.com/problems/course-schedule/)
### Graph Valid Tree
> [!note]
> def tree : A valid tree with `n` nodes must have **exactly `n - 1` edges** and be fully connected
> - No cycles
> - Fully connected

```python
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque()
        queue.append((0, -1)) # node, parent
        
        visited = set()
        while queue:
            node, parent = queue.popleft()
            if node in visited: # check for cycle
                return False
            visited.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                queue.append((nei, node))
        
        return len(visited) == n
```
[Neetcode: Problems](https://neetcode.io/problems/valid-tree?list=blind75)
TC: O(v + e) | SC: O(v + e)
### Number of Connected Components in an Undirected Graph
LC: [Neetcode: Problems](https://neetcode.io/problems/count-connected-components?list=blind75)

```python
def countComponents(self, n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list) # Undirected Graph
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    components = 0

    for node in range(n):
        if node in visited:
            continue

        # Start BFS
        queue = deque([node])
        visited.add(node)

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        components += 1  # one full connected component traversed

    return components
```

TC: O(v + e) | SC: O(v + e)
### Alien dictionary
LC: [NeetCode: Problems](https://neetcode.io/problems/foreign-dictionary?list=blind75)
> We **can compare words of different lengths**, but we only **use the first different character** to determine order.

```python
def foreignDictionary(self, words: List[str]) -> str:
    '''
    Step1: ini graph:defaultdict[set] and in_degree:{}
    Step2: implement graph:[a: set(b,c)]
    Step3: bfs: in_degree, priority from 0
    Step4: return in_degree == res
    ''' 
    graph = defaultdict(set)
    in_degree = {}
    
    for word in words:
        for c in word:
            in_degree[c] = 0
    
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]: # *prevents adding the same edge
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    queue = deque()
    for c in in_degree:
        if in_degree[c] == 0:
            queue.append(c)
    res = []
    while queue:
        c = queue.popleft()
        res.append(c)
        for nei in graph[c]:
            in_degree[nei] -= 1
            if in_degree[nei] == 0:
                queue.append(nei)
    
    return "".join(res) if len(res) == len(in_degree) else ""
```
TC: O(n) | SC: O(u + e)
## 12.DP
### 1D-DP
#### 70. Climbing Stairs
LC: [70.Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp = [0] * (n + 1)  # dp[0] ~ dp[n]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
# optimal 
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b # Space Complexity: O(1)
        
        return b
```
- TC: O(n) | SC: O(n)
#### 198.House Robber
LC: [House Robber - LeetCode](https://leetcode.com/problems/house-robber/description/)
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]
```
Optimal:
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        prev1 = 0 # dp[i-1]
        prev2 = 0 # dp[i-2]
        
        for num in nums:
            temp = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = temp
        
        return prev1
```
#### 213.House Robber II
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def houseRob(nums):
            prev1 = 0 # dp[i-1]
            prev2 = 0 # dp[i-2]

            for num in nums:
                temp = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = temp
            
            return prev1
        return max(houseRob(nums[:-1]), houseRob(nums[1:]))
```
#### 5.Longest Palindromic Substring
>[!note]
> A palindrome expands symmetrically from its center.

LC: [Longest Palindromic Substring - LeetCode](https://leetcode.com/problems/longest-palindromic-substring/description/)
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return s
        
        # two scenario
        def expand_center(left, right):
            while (
                left >= 0 and 
                right <= (len(s) - 1) and 
                s[left] == s[right]
            ):
                left -= 1
                right += 1
            return left + 1, right - 1 # Include the correct window
        
        max_length = 0
        for idx in range(0, len(s)):
            l1, r1 = expand_center(idx, idx) # odd
            l2, r2 = expand_center(idx, idx + 1) # even
        
            if r1 - l1 + 1 > max_length:
                max_length = r1 - l1 + 1
                res = s[l1 : r1 + 1] 

            if r2 - l2 + 1 > max_length:
                max_length = r2 - l2 + 1
                res = s[l2 : r2 + 1]
        
        return res
```
- TC: O($n^2$) | SC: O(1)

#### 647.Palindromic Substrings
LC: [647.Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/)
```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        def expend_center(left, right):
            nonlocal count
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
        
        for idx in range(len(s)):
            expend_center(idx, idx)
            expend_center(idx, idx + 1)
        
        return count
```
- TC: O($n^2$) | SC: O(1)

#### 91.Decode Ways
LC: [91. Decode Ways - LeetCode](https://leetcode.com/problems/decode-ways/description/)

> 一个数字字符串的解码方法数 = 它最后一位单独解码的方式数量 + 它最后两位组合解码的方式数量（如果合法）
> decode("226") = decode("22") + decode("2")

`dp[i]` means: how many ways to decode the  `i` characters of `s`
- `0X` is illegal, 10 <=`X0 or 0X`  <= 26 is legal
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        s_len = len(s)
        dp = [0] * (s_len + 1) # 0 to n
        dp[0] = 1
        dp[1] = 1

        for idx in range(2, s_len + 1): # 1, n
            if s[idx - 1] != '0':
                dp[idx] += dp[idx - 1]
            if 10 <= int(s[idx - 2: idx]) <= 26:
                dp[idx] += dp[idx - 2]
        return dp[s_len]
```
- TC: O(n) | SC: O(n)
#### 322.Coin Change
LC: [322. Coin Change](https://leetcode.com/problems/coin-change/)
Unbounded Knapsack - coin can be used unlimited time
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)  # dp[i] = min coins to make i
        dp[0] = 0  # base case: 0 coins to make amount 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
```
- TC: O(n * amount) | SC: O(amount)
#### 153. Maximum Product Subarray
LC: [152. Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
> - Because **multiplying by a negative number flips signs**, you must track both the **maximum and minimum product ending at each position** — and at each step, decide whether to **extend the previous product** or **start fresh**.
> - max(num, num * prev_max, num * prev_min)

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_num = max_num = res = nums[0]
        for num in nums[1:]:
            if num < 0:
                min_num, max_num = max_num, min_num
            
            max_num = max(num, max_num * num)
            min_num = min(num, min_num * num)

            res = max(res, max_num)
        return res
```
- TC: O(n ) | SC: O(1)
#### 139.Word Break
LC: [139. Word Break](https://leetcode.com/problems/word-break/)
> Because there are **multiple ways** to segment the string — and we need to try **all possible partitions**, not just one.
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1) # 8
        dp[0] = True

        for i in range(len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        
        return dp[len(s)]
```
- TC: O(n$^2$) | SC: O(n)
#### 300.Longest Increasing Subsequence
LC: [300.Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/)
```python

def lengthOfLIS(self, nums: List[int]) -> int:
    """
    Patience sorting + binary search (闭区间写法)
    res[k] = 长度为 k+1 的递增子序列的最小结尾
    """
    
    def lower_bound(arr: List[int], target: int) -> int:
        """返回第一个 >= target 的索引"""
        left, right = 0, len(arr) - 1
        pos = len(arr)  # 默认插在末尾
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                pos = mid
                right = mid - 1
            else:
                left = mid + 1
        return pos
    
    tails = []
    for num in nums:
        idx = lower_bound(tails, num)
        if idx == len(tails):
            tails.append(num)    # 比所有尾巴大 → 新长度
        else:
            tails[idx] = num     # 替换，更小结尾
    return len(tails)
```
- TC: O(nlogn) | SC: O(n)
### 2D-DP
#### 62. Unique Path
LC: [62.Unique Paths](https://leetcode.com/problems/unique-paths/)
> The number of unique paths to reach: path cell above + cell to its left.

```python
def uniquePaths(self, m: int, n: int) -> int:
    rows, cols = m, n
    dp = [[1] * cols for _ in range(rows)]
    
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
    return dp[rows - 1][cols - 1]
```
- TC: O(`m * n`) | SC: O(`m * n`)

#### 1143.Longest Common Subsequence
LC: [1143.Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/description/)
> Implement 2-D DP table
> - When comparing two sequences, 
> 	- if the current characters match,  extend the longest common subsequence 
> 	- If  don't match,  explore both possibilities (skipping a character from either string) and take longer

```python
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    rows = len(text1) + 1
    cols = len(text2) + 1

    dp = [[0] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
    
    return dp[rows - 1][cols - 1]
```
- TC: O(`m * n`) | SC: O(`m * n`)
## 13.Greedy
### 53.Maximum Subarray
LC: [53.Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
```python
def maxSubArray(self, nums: List[int]) -> int:
    current_sum = max_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
```
- TC: O(n) | SC: O(1)
### 55.Jump Game
LC: [55. Jump Game](https://leetcode.com/problems/jump-game/)
```python
def canJump(self, nums: List[int]) -> bool:
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True
```
- TC: O(n) | SC: O(1)
## 14.Intervals
### 57.Insert Interval
LC: [57.Insert Interval](https://leetcode.com/problems/insert-interval/description/)
```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    i = 0
    res = []
    n = len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    res.append(newInterval)

    while i < n:
        res.append(intervals[i])
        i += 1
    return res
```
- TC: O(n) | SC: O(n)
### 56.Merge Intervals
LC: [56.Merge Intervals](https://leetcode.com/problems/merge-intervals/description/)
> **Walk from left to right**
> If the next start ≤ previous end → they overlap → merge them
> 	if `current[0] <= prev[1]`: 

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merge = [intervals[0]]
        
        for cur in intervals[1:]:
            prev = merge[-1]
            if cur[0] <= prev[1]:
                prev[1] = max(cur[1], prev[1])
            else:
                merge.append(cur)
        return merge
```
- TC: O(n log n) | SC: O(n)
### 435.Non-overlapping Intervals
LC: [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
> To minimize the number of intervals to remove, always keep the interval that **ends earliest** — this leaves the most room for the next one.

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x:x[1])
    prev_end = intervals[0][1]
    count = 0
    for cur in intervals[1:]:
        if cur[0] < prev_end:
            count += 1
        else:
            prev_end = cur[1]
    
    return count
```
- TC: O(n log n) | SC: O(1)
### Meeting Rooms
LC: [Meeting Rooms](https://neetcode.io/problems/meeting-schedule?list=blind75)
```python
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0].end
        for cur in intervals[1:]:
            if cur.start < prev:
                return False
            else:
                prev = cur.end
        
        return True
```
- TC: O(n log n) | SC: O(1)
### Meeting Rooms II
LC: [Meeting Rooms II](https://neetcode.io/problems/meeting-schedule-ii?list=blind75)
> min-heap
> - To find the minimum number of meeting rooms required, track how many meetings are happening at the same time.

```python
def minMeetingRooms(self, intervals: List[Interval]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x:x.start)
    heap = []
    heapq.heappush(heap, intervals[0].end)
    
    for cur in intervals[1:]:
        if cur.start < heap[0]: # cur.start < prev.end
            heapq.heappush(heap, cur.end)
        else: # cur.start > heap[0]
            heapq.heappop(heap)
            heapq.heappush(heap, cur.end)
    
    return len(heap)
```
- TC: O(n log n) | SC: O(n)
## 15.Math & Geometry
### 48.Rotate Image
LC: [48. Rotate Image](https://leetcode.com/problems/rotate-image/)
> 1. Transpose
> 2. Reverse 
> **A 90° clockwise rotation of a square matrix = transpose + reverse each row.**
> `(i, j) → (j, n - 1 - i)`

```python
def rotate(self, matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    # 对角线翻转（Transpose）
    for r in range(rows): 
        for c in range(r + 1, cols):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    for row in matrix:
        row.reverse()
```
- TC: O(n²) | SC: O(1)
### 54.Spiral Matrix
LC: [54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)
```python
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    rows = len(matrix)
    cols = len(matrix[0])

    res = []
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            res.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom + 1):
            res.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1
    
    return res
```
### 73.Set Matrix Zeroes
LC: [73. Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # record first row or first col has zero
        rows, cols = len(matrix), len(matrix[0])
        row_flag, col_flag = False, False
        
        
        for col in range(cols):     # row flag
            if matrix[0][col] == 0:
                row_flag = True
                break
        
        for row in range(rows):     # col flag
            if matrix[row][0] == 0:
                col_flag = True
                break
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
        
        if row_flag:
            for col in range(cols):
                matrix[0][col] = 0
        
        if col_flag:
            for row in range(rows):
                matrix[row][0] = 0
```
- TC: O(mn) | SC: O(1)
## 16. Bit manpulation
### 191. Number of 1 Bits
LC: [Number of 1 Bits - LeetCode](https://leetcode.com/problems/number-of-1-bits/description/)
> `&`: `and`

```python
def hammingWeight(self, n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    
    return count
```
### 338.Counting Bits
LC: [338.Counting Bits](https://leetcode.com/problems/counting-bits/description/)
```python
def countBits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp
```
### 190.Reverse Bits
LC: [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/)
```python
def reverseBits(self, n: int) -> int:
    res = 0
    for _ in range(32):
        res <<= 1
        res = res | (n & 1)
        n >>= 1
    
    return res
```

### 268. Missing Number
LC: [268. Missing Number](https://leetcode.com/problems/missing-number/)
> 如果两个集合完全相同 → 异或后是 `0`

```python
def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    res = n
    for i in range(len(nums)):
        res ^= i
        res ^= nums[i]
    return res
```
- TC: O(n) | SC: O(1)
### 371.Sum of Two Integers
```python
def getSum(self, a: int, b: int) -> int:
    MAX =  0x7FFFFFFF   # 0xFFFFFFFF // 2
    MASK = 0xFFFFFFFF
    while b:
        carry = (a & b) & MASK
        a = (a ^ b) & MASK # XOR (^) performs addition without carry.
        b = (carry << 1) & MASK
    return a if a <= MAX else ~ (a ^ MASK)
```
- TC: O(1) | SC: O(1)
## 17.Sort
### Bucket sort
```python
def bucket_sort(data,  , max_key_value):
    """
    Parameters:
    - data: list of items (numbers, strings, etc.)
    - key_fn: function to extract key for bucketing (e.g., frequency, score)
    - max_key_value: the maximum value key_fn(item) can return
    Returns: List of buckets (bucket[i] contains all items with key i)
    """
    buckets = [[] for _ in range(max_key_value + 1)] # Step 1: Create empty buckets
    
    for item in data:               # Step 2: Distribute data into buckets
        key = key_fn(item)
        buckets[key].append(item)
    return buckets
```
- Time complexity is O(n) | Space complexity is O(n)

