## Heap
- heapq.heappush(h, x) → O(log n)
- heapq.heappop(h) → O(log n)
    - read heap[0] → O(1)
- heapq.heapify(a) → O(n)
- heapq.heapreplace(h, x) → O(log n) 
    - Pop the smallest, then push x
- heapq.heappushpop(h, x) → O(log n) (best case O(1))
    - Push x, then pop and return the smallest.