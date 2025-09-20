# 0743.Network_Delay_Time
'''

* TC: O(E+V)LogV| SC: O(V+E)
'''
from typing import List
from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        heap = [(0, k)]  # (distance, node)
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        while heap:
            cur_dist, node = heapq.heappop(heap)
            if cur_dist > dist[node]:
                continue
            for nei, w in graph[node]:
                nd = cur_dist + w
                if nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(heap, (nd, nei))
        
        res = max(dist.values())
        return -1 if res == float('inf') else res