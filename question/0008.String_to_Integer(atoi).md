# 0008.String_to_Integer(atoi)
'''
* TC: O(n) | SC: O(1)
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        idx = 0
        if s[0] in '-+':
            sign = -1 if s[0] == '-' else 1
            idx += 1
        
        res = 0
        while idx < len(s) and s[idx].isdigit():
            res = res * 10 + int(s[idx])
            idx += 1
        
        res *= sign
        min_val, max_val = -2 ** 31, 2 ** 31 -1
        if res < min_val:
            return min_val
        elif res > max_val:
            return max_val
        
        return res