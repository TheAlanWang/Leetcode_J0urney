# 0045.Jump_Game_II
# https://leetcode.com/problems/jump-game-ii/description/
# time complexity: O(n) | space complexity: O(1)

class Solution:
    def jump(self, nums):
        jumps = 0
        l = r = 0   # current level = [l, r]

        while r < len(nums) - 1:  # stop once last index is inside [l, r]
            farthest = 0
            # Explore all positions in the current level
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # Move to the next level
            l = r + 1
            r = farthest
            jumps += 1

        return jumps
