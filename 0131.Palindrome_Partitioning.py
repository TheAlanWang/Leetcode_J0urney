# 0131.Palindrome_Partitioning
'''
Approach: Backtracking

'for' loop: branching over every *possible substring* starting at start.
'dfs(i+1, path)': recursing on the remaining suffix.

Time Complexity: O(N * 2^N) | Space Complexity: O(N)
'''

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        def dfs(start, path, s):
            if start == len(s):
                res.append(path[:])
                return res
        
            for i in range(start, len(s)):
                if self.is_palin(s, start, i):
                    path.append(s[start: i + 1])
                    dfs(i + 1, path, s)
                    path.pop()
        
        dfs(0, [], s)    
        return res
    
    def is_palin(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False    
            left += 1
            right -= 1
        
        return True