# 0261.Graph_Valid_Tree
# https://leetcode.com/problems/graph-valid-tree/
# time complexity: O(n+e) | space complexity: O(n+e)

from collections import defaultdict, deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        queue = deque()
        queue.append((0, -1))
        visited.add(0)
        while queue:
            node, parent = queue.popleft()
            for nei in graph[node]:
                if nei != parent and nei in visited:
                    return False
                if nei not in visited:
                    queue.append((nei, node))
                    visited.add(nei)
        return len(visited) == n