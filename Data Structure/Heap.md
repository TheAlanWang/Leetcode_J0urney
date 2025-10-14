---
tags:
  - ds/heap
pageorder: 8
mainpage: "[[DV_DataStructure]]"
---
## Heap/Priority Queue
> [!note] A Heap is a  [[Tree_Binary Tree#Complete Binary Tree|Complete Binary Tree structure]].
> 1. All levels except the last level are completely filled.
> 2. The last level is filled from left to right, with no gaps.

**Heap Structure property:**
- In a Min Heap, the parent node is always smaller than or equal to its child nodes.
- In a Max Heap, the parent node is always greater than or equal to its child nodes.
This structure allows for efficient retrieval of the smallest (Min Heap) or largest (Max Heap) element.

> [!note] A **Priority Queue** is an **abstract data structure** similar to a regular queue but with prioritized elements. Instead of following the First-In-First-Out (FIFO) rule like a normal queue, elements are dequeued based on their priority (e.g., highest priority first).

A Heap is a common way to implement a Priority Queue because:
### Heap Operations
- Push: Insertion: $O(log n)$
- Pop: Removal of the highest/lowest priority element: $O(logn)$
- Getting the highest/lowest priority element: $O(1)$
- Heapify: $O(n)$

```python
import heapq

# Min heap operations
heap = []
heapq.heappush(heap, item)    # Push
smallest = heapq.heappop(heap) # Pop
smallest = heap[0]            # Peek

# Convert list to heap
heapq.heapify(list)          # O(n)
```

### Push & Pop
Push
- **Add the element** at the next available position in the heap (usually the last position, i.e., the next open spot in the tree structure).
- **Perform a "heapify-up" operation** to maintain the heap property. This means comparing the inserted element with its parent and swapping them if the heap property is violated (i.e., if a min-heap property is violated for a smaller value or a max-heap property is violated for a larger value).
- **Repeat the heapify-up process** until the heap property is restored or the element reaches the root.

Pop
1. Swap Root with Last Element:
- The root (self.heap[1]) is swapped with the last element in the heap (self.heap.pop()).
- After the swap, the last element is now at the root, which might violate the heap property (in this case, the min-heap property).

1. Percolate Down:
- The process begins at the new root (i = 1).
- The code checks if the current element (self.heap[i]) is greater than its left child (self.heap[2 * i]) or right child (self.heap[2 * i + 1]).
    - If the right child exists and is smaller than the left child, it checks if the current element is greater than the right child and swaps them.
    - Otherwise, if the left child is smaller, it swaps the current element with the left child.
- After each swap, the index (i) is updated to the index of the child that was swapped with, and the loop continues to percolate down the tree.
- If no swap is needed (meaning the heap property is satisfied), the loop breaks.

Purpose of Percolate Down:

- The goal of percolate down is to **restore the heap property** after the root element is removed. This ensures that the heap remains a valid min-heap.
- Percolate down works by comparing the current element with its children and moving it down the tree to its correct position.

### Complete Binary Tree (CBT)
- Every level is completely filled, except possibly the last one.
- If the last level is not full, nodes are added from left to right.
- It can be perfectly balanced or nearly balanced.
- A complete binary tree ensures efficient use of space.

Order Property:
> left child = 2 * index
> _right_ _child_ = 2 * _index_ + 1
> _parent_ = _index_


```python
def heapify(arr, i, n):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is smaller
    if left < n and arr[left] < arr[smallest]:
        smallest = left

    # Check if right child is smaller
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # If smallest is not the current index
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]  # swap
        heapify(arr, smallest, n)  # recursively heapify the affected subtree

```
