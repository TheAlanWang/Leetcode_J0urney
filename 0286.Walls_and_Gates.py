# 0286.Walls_and_Gates.py

'''
* TC: O(mn) | SC: O(mn)
'''
from collections import deque
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:

        if not rooms or not rooms[0]:
            return
        rows, cols = len(rooms), len(rooms[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))