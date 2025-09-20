# 0424.Longest_Repeating_Character_Replacement

'''
Approach: Sliding window
State:
    top_freq=#  highest frequency char
    dic = {}    {char: count} in window
    left, right, win_size = right - left + 1
    max_size
Transitions:
    while right < len(s):
        move left: shrink window while win_size - top_freq > k,
        move right: extend window
* TC: O(n) | SC: O(n)
'''
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = right = 0
        top_freq = 0
        dic = defaultdict(int)
        max_size = 0
        while right < len(s):
            dic[s[right]] += 1
            top_freq = max(top_freq, dic[s[right]])
            while (right - left + 1) - top_freq > k:
                dic[s[left]] -= 1
                left += 1

            max_size = max(max_size, right - left + 1)
            right += 1
        
        return max_size