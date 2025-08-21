# anagram:same characters, same frequency, different order
# TC: O(n) | SC: O(1) if 26 lowest case letters, O(n) otherwise

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check length first
            return False

        count = defaultdict(int)
        for ch in s:
            count[ch] += 1

        for ch in t:
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True