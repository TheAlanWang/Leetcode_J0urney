# 0146.LRU_Cache
# https://leetcode.com/problems/lru-cache/description/

'''
Approach: Double linked list
State:
    Node(key, value, prev, next) 
    cache = {key: Double_linked_list} 
Transitions:
    initial: head <-> tail
    def _remove(node)
    def _add(node)
* Time Complexity: O(1) Space Complexity: O(n)
'''
class Node:
    def __init__(self, key, val):
        # double linked list
        self.key = key
        self.val = val
        
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # dummy: MRU=head.next, LRU=tail.prev
        self.head = Node(0, 0)      # head.next = most recent
        self.tail = Node(0, 0)      # tail.prev = store least recent
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):        # remove from cache
        prev = node.prev            
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):           # add to head.next
        node.next = self.head.next  # connect new node
        node.prev = self.head       # connect new node

        self.head.next.prev = node  # link old first node
        self.head.next = node       # link head forward to the new node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]      # return DLL node
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node      # add to cache

        if len(self.cache) > self.cap:
            node = self.tail.prev
            self._remove(node)
            del self.cache[node.key] # remove from cache