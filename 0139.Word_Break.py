# https://leetcode.com/problems/word-break/description/
# 
# Method 1: dp TC: O(n^2) | SC: O(n)
# Method 2: dp by using dic_len
#   Time Complexity: O(n*U*L) Space: O(n)
#       U = how many different lengths appear in wordDict
#       L = the cost of slicing/ hashing s[j:i]


# Method 1
'''
Approach: Dynamic Programming
State: 
    dp[i] = True: if s[:i] can be segmented
Transitions:
    dp[i] = True if there exists j < i such that:
            dp[j] == True and s[j:i] in dict

* TC: O(n^2) | SC: O(n)
'''
from typing import List  
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i): 
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]

# Method 2
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
