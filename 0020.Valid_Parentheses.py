# 0020.Valid_Parentheses
'''
Approach: Stack
State: stack(track opening brackets), dic={closing:opening}
Transition:
    - use a dictionary to map closing -> opening brackets
    - if char is opening brackets, append
    - if char is closing brackets: 
        check stack and stack[-1], return False
        stack.pop
    - return len(stack)
* TC: O(n) | SC: O(n)
'''

class Solution:
    def isValid(self, s: str) -> bool:

        dic = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            
            if char not in dic:
                stack.append(char)
            
            if char in dic:
                if not stack or stack[-1] != dic[char]:
                    return False
                stack.pop()

        return len(stack) == 0