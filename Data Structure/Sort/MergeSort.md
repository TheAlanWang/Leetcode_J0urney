---
tags:
  - algorithm
pageorder: 1.1
mainpage:
  - "[[DV_DataStructure]]"
description: write
---
Time complexity: $O(nlogn)$
```python
'''
Write a function merge_sort(items: list) -> list that produces a sorted copy of the input
list using merge sort. (Merge sort splits its input list in half, recursively sorts each half, then merges
the two sorted lists into a full sorted list.)
'''
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        elif left[i] > right[j]:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def main():
    test = [5, 8, 3, 2, 1]
    print(merge_sort(test))

if __name__ == "__main__":
    main()
```