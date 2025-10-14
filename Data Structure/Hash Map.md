---
tags:
  - ds
pageorder: 9
---
> [!NOTE]
A **HashMap** is a data structure that stores key-value pairs and allows for fast retrieval, insertion, and deletion. It is commonly used in programming to efficiently store and access data.
## Time Complexity
|         | TreeMap   | HashMap    |
| ------- | --------- | ---------- |
| Insert  | $O(logn)$ | $O(1)$     |
| Remove  | $O(logn)$ | $O(1)$     |
| Search  | $O(logn)$ | $O(1)$     |
| Inorder | $O(n)$    | $O(nlogn)$ |


### Code
```python
names = ["alice", "brad", "collin", "brad", "dylan", "kim"] 
countMap = {}
for name in names:
	# If countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1
```
### Hash implementation
- convert key into integer,
- take integer mod `%` by the size of array
- when insert, if half-full, resize the hashmap, after resize, recompute the index
    - size number would be prime number
- Hash collision
    - Chaining: multiple keys hash
    - Open Addressing: search for the next available spot

### code
```python
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val
 
class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]
     
    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity
 
    def get(self, key):
        index = self.hash(key)
         
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None
 
    def put(self, key, val):
        index = self.hash(key)
 
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return
             
            index += 1
            index = index % self.capacity
     
    def remove(self, key):
        if not self.get(key):
            return
         
        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                # Removing an element using open-addressing actually causes a bug,
                # because we may create a hole in the list, and our get() may 
                # stop searching early when it reaches this hole.
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity
 
    def rehash(self):
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)
 
        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)
     
    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)
```