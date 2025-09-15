# 0005.Longest_Palindromic_Substring
'''
Approach: two pointers - Expand Around Center
Transitions:
    For each i, expand from:
    • odd center  (i, i)
    • even center (i-1, i)
Track the best inclusive range [L, R] and slice once at the end.

* TC: O(n^2) | SC: O(1)
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_center(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)

        max_len = 0
        for idx in range(len(s)):
            even_l, even_r = expand_center(idx, idx)    # odd
            if max_len < even_r - even_l + 1:
                res = s[even_l: even_r + 1]
                max_len = even_r - even_l + 1
            
            odd_l, odd_r = expand_center(idx, idx + 1)  # even
            if max_len < odd_r - odd_l + 1:
                res = s[odd_l: odd_r + 1]
                max_len = odd_r - odd_l + 1
        
        return res