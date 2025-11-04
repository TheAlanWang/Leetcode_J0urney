```python
class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
            
        dummy = Node(-1, None, None)
        prev = dummy
        cur = root
        stack = []
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            node = stack.pop()
            
            # mid
            prev.right = node
            node.left = prev
            prev = node

            cur = node.right
        
        dummy.right.left = prev
        prev.right = dummy.right
        return dummy.right
```

def inorder(root):
    stack = []
    cur = root

    while stack or cur:
        # 1. Go all the way left
        while cur:
            stack.append(cur)
            cur = cur.left

        # 2. Visit the node
        cur = stack.pop()
        print(cur.val)      # <-- inorder output

        # 3. Go right
        cur = cur.right
