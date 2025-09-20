# 0017.Letter_Combinations_of_a_Phone_Number

'''
Approach: Backtracking
1. State: idx( which char), path( current combination)
2. Choices: the characters mapped to the current digit
3. Transition Logic: choose one char, move to the next digit
4. Base case

Time Complexity: O(n*4^n) | Space Complexity: O(n*4^n) -recursion space only O(N)
'''
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2":"abc", "3":"def", 
            "4":"ghi", "5":"jkl", "6":"mno",
            "7":"pqrs", "8":"tuv", "9":"wxyz"}

        res = []
        def dfs(idx, path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            
            for char in phone_map[digits[idx]]:
                path.append(char)
                dfs(idx + 1, path)
                path.pop()

        dfs(0, [])
        return res 