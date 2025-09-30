# 0695.Max_Area_of_Island
# Time Complexity: O(m*n) | Space Complexity: O(m*n)

from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        max_area = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            cur_area = 1
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        (0 <= nr < rows and 0 <= nc < cols) and
                        grid[nr][nc] == 1 and
                        (nr, nc) not in visited
                    ):
                        cur_area += 1
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            return cur_area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area