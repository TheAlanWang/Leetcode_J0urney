---
tags:
  - algorithm
pageorder: 1.3
description: know
mainpage:
  - "[[DV_DataStructure]]"
---
```python
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]  
        j = i - 1

        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]   # more index to next, so nums[j] for replacement
            j -= 1
        
        nums[j + 1] = key
    return nums

def main():
    test = [5, 8, 3, 2, 1]
    print(insertion_sort(test))

if __name__ == "__main__":
    main()

```