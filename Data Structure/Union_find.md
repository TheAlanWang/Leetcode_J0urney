Two different `union` way:
1. by size
2. by rank

## DSU: Disjoint Set Union
```python
class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n   # or rank if you prefer

    def find(self, x: int) -> int:
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False  # already in the same set (merged earlier)

        # Union by size
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
        return True       # successfully merged
```
### Complexity
- Time Complexity: O(E · α(n))
- Space Complexity: O(n)