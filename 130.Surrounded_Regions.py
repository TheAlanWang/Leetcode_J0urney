# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/description/
# time complexity: O(m * n) | space complexity: O(m * n)


from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        visited = set()
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def bfs(r, c):
            flip_flag = True
            regions = set()
            queue = deque()
            queue.append((r, c))
            
            regions.add((r, c))
            visited.add((r, c))
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        flip_flag = False
                    if (
                        (0 <= nr < rows and 0 <= nc < cols) and
                        (nr, nc) not in visited and
                        board[nr][nc] == "O"
                    ):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        regions.add((nr, nc))
            
            if flip_flag:
                for r, c in regions:
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    bfs(r, c) 