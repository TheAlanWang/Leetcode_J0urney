# 0208.Implement_Trie(Prefix_Tree).py

'''
Approach: Trie

    dictionary.setdefault()
    - If there's already a node for c, use it; otherwise create a new TrieNode for c and use that
'''
class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children.setdefault(c, TrieNode())
        cur.is_end = True

    def _traverse(self, word: str) -> TrieNode | None:
        """Helper to traverse the trie. Returns last node if found, else None."""
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node.is_end if node else False

    def startsWith(self, prefix: str) -> bool:
        return self._traverse(prefix) is not None