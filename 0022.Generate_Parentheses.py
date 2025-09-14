# 0022.Generate_Parentheses.py
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(path, left, right):
            if left == n and right == n:
                res.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(path, left + 1, right)
                path.pop()
            
            if left > right and right < n:
                path.append(")")
                dfs(path, left, right + 1)
                path.pop()
        
        dfs([], 0, 0)
        return res