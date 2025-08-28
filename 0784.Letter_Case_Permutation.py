# 0784.Letter_Case_Permutation
# time complexity: O(2^k*n) | space complexity: O(2^k*n)
'''
Approach: DFS + Backtracking
1. Use DFS to explore all possible letter case permutations of the input string.
2. At each character, if it's a digit, we can only add it as is. If it's a letter, we have two choices: add the uppercase version or the lowercase version.
3. Use backtracking to explore both choices for letters.
4. When we reach the end of the string, we add the current permutation to the result list. 
'''
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        
        def dfs(idx, path):
            if idx == len(s):
                res.append("".join(path))
                return
            
            if s[idx].isdigit():
                path.append(s[idx])
                dfs(idx + 1, path)
                path.pop()
            else:
                path.append(s[idx].upper())
                dfs(idx + 1, path)
                path.pop()
                path.append(s[idx].lower())
                dfs(idx + 1, path)
                path.pop()
        
        dfs(0, [])
        return res