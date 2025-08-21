from collections import defaultdict
# O(n) O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need_dic = {}
        win_dic = {}
        
        for char in s1:
            need_dic[char] = need_dic.get(char, 0) + 1

        need_count = len(need_dic)
        win_count = 0
        left = right = 0

        while right < len(s2):
            if s2[right] in need_dic:
                win_dic[s2[right]] = win_dic.get(s2[right], 0) + 1
                if win_dic[s2[right]] == need_dic[s2[right]]:
                    win_count += 1

            while right - left + 1 > len(s1):
                if s2[left] in need_dic:
                    if win_dic[s2[left]] == need_dic[s2[left]]:
                        win_count -= 1
                    win_dic[s2[left]] = win_dic.get(s2[left], 0) - 1
                left += 1

            if win_count == need_count:
                return True

            right += 1
        
        return False