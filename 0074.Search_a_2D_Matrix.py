# 0074.Search_a_2D_Matrix
'''
Approach: binary search
State: matrix, left = 0, right = rows * cols - 1
Transitions:
    row = idx // cols, col = idx % cols

* TC: O(log(mn)) SC: O(1)
'''
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]
            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False