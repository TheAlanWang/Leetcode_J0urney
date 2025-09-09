# 0211.Design_Add_and_Search_Words_Data_Structure

'''
Trie = {'a': TrieNode, 'b': TrieNode, 'c': TrieNode}
(root)
  └── 'c'
        └── 'a'
              └── 't'
'''

'''
Approach: Trie

Search part:
    State: dfs(idx, node)
    Base Case: if idx == len(word)
    Transitions: 
        if char == ".", iterative char in node.children.values();
        if char in node.children, dfs(idx+1, node.children[char])
* TC: O(L)| SC: O(L)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root

        def dfs(idx, node):
            if idx == len(word):
                return node.end_of_word

            if word[idx] == '.':
                for child in node.children.values():
                    if dfs(idx + 1, child):
                        return True
                return False
            else:
                if word[idx] not in node.children:
                    return False
                return dfs(idx + 1, node.children[word[idx]])
        
        return dfs(0, cur)