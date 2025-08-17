# https://leetcode.com/problems/word-break/description/
# Time Complexity: O(n*U*L) Space: O(n)
#   U = how many different lengths appear in wordDict
#   L = the cost of slicing/ hashing s[j:i]

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        lens = {len(w) for w in words}  # distinct lengths

        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True

        for i in range(1, n+1):
            for L in lens:
                j = i - L
                if j >= 0 and dp[j] and s[j:i] in words:  # ← use set
                    dp[i] = True
                    break
        return dp[n]
