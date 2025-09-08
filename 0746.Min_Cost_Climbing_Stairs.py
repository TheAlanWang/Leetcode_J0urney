# 0746.Min_Cost_Climbing_Stairs

'''
Approach: Dynamic Programming
Transition:
    cost:  [10  15  20]
    dp:  [0, 0, 10, 15]
    idx:  0   1   2  3
* TC: O(n) | SC: O(n)
'''
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]