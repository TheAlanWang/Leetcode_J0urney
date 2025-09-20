# 0003.Longest_Substring_Without_Repeating_Characters
'''
Approach: Sliding Window
State: left, right, max_window, dic
Transitions:
    1. expand the window by moving 'right'
    2. shrink the window by moving 'left'
    3. update the window
* TC:O(n) | SC:O(n)
'''
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        dic = defaultdict(int)
        max_win = 0
        while right < len(s):
            dic[s[right]] += 1
            
            while dic[s[right]] > 1:
                dic[s[left]] -= 1
                left += 1
            
            max_win = max(max_win, right - left + 1)

            right += 1
        
        return max_win