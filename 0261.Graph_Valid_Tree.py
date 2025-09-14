# 0261.Graph_Valid_Tree
# https://leetcode.com/problems/graph-valid-tree/

'''
Method1: BFS
* TC: O(n+e) | SC: O(n+e)
Method2: Union-Find
'''

from collections import defaultdict, deque
from typing import List

# Method1: BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        queue = deque()
        queue.append((0, -1))
        visited.add(0)

        while queue:
            node, parent = queue.popleft()
            for nei in graph[node]:   
                if nei == parent:
                    continue
                if nei in visited:  # cycle
                    return False  

                queue.append((nei, node))
                visited.add(nei)

        return len(visited) == n