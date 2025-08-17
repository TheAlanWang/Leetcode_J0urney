from collections import defaultdict
# O(n) O(1)

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need_dic = defaultdict(int)
        win_dic = defaultdict(int)
        matches = 0
        for c in s1:
            need_dic[c] += 1
        
        for idx in range(len(s1)):
            char = s2[idx]
            if char in need_dic:                 
                win_dic[char] += 1

        for ch, cnt in need_dic.items():
            if win_dic[ch] == cnt: 
                matches += 1           
        
        if matches == len(need_dic):
            return True

        for idx in range(len(s1), len(s2)):
            add_char = s2[idx]
            remove_char = s2[idx - len(s1)]

            if add_char in need_dic:
                before_add = win_dic[add_char]
                win_dic[add_char] += 1
                if win_dic[add_char] == need_dic[add_char]:
                    matches += 1
                elif before_add == need_dic[add_char]:
                    matches -= 1
            
            if remove_char in need_dic:
                before_remove = win_dic[remove_char]
                win_dic[remove_char] -= 1
                if  win_dic[remove_char] == need_dic[remove_char]:
                    matches += 1
                elif before_remove == need_dic[remove_char]:
                    matches -= 1
            
            if matches == len(need_dic):
                return True
        
        return False