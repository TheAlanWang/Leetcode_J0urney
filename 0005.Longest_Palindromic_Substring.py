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
        def expand_center(l, r):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (l + 1, r - 1)

        max_len = 0
        for i in range(1, len(s)):
            l1, r1 = expand_center(i - 1, i)
            l2, r2 = expand_center(i, i)

            if r1 - l1 > max_len:
                max_len = r1 - l1
                max_range = (l1, r1)
            if r2 - l2 > max_len:
                max_len = r2 - l2
                max_range = (l2, r2)
        
        return s[max_range[0]: max_range[1] + 1]