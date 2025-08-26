## Heap

| Operation                 |  Time Complexity  | Notes                                   |
| ------------------------- | :---------------: | --------------------------------------- |
| `heapq.heappush(h, x)`.   | **O(log n)**      | Insert and bubble up (`n` = heap size). |
| `heapq.heappop(h)`        | **O(log n)**      | Pop smallest and sift down.             |
| `h[0]` (peek)             | **O(1)**          | Read smallest without removing.         |
| `heapq.heapify(a)`        | **O(n)**          | In-place build from a list.             |
| `heapq.heapreplace(h, x)` | **O(log n)**      | Pop smallest, then push `x` (size unchanged). |
| `heapq.heappushpop(h, x)` | **O(log n)** *(best **O(1)** if `x <= h[0]`)* | Push `x`, then pop and return the smallest.   |

