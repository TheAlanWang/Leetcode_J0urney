# 322.Coin_Change

'''
Approach: DP 1-D bottom-up
State:
    dp[i] = min #coins to form sum i (INF if impossible)
Transitions:
    dp[i] = min(dp[i - coin] + 1, dp[i])

* TC: O(len(coins) * amount) | SC: O(amount)
'''
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        
        return dp[-1] if dp[-1] != float('inf') else -1