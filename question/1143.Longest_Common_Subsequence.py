# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/description/
# Time Complexity: O(mn)  asymptotically | Space Complexity: O(mn) 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
          0 a b c d e
        0 0 0 0 0 0 0
        a 0 1 1 1 1 1
        c 0 1 1 2 2 2
        e 0 1 1 1 1 3
        '''
        rows = len(text1) + 1 # n + 1
        cols = len(text2) + 1

        dp = [[0] * cols for _ in range(rows)]

        for r in range(1, rows): # n
            for c in range(1, cols):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        
        return dp[-1][-1]
