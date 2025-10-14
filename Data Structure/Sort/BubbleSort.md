---
tags:
  - algorithm
pageorder: 1.4
mainpage:
  - "[[DV_DataStructure]]"
description: know
---
```python
def bubble_sort(nums: list):
    n = len(nums)
    for i in range(n):  
        for j in range(0, n - 1 - i): 
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def main():
    test = [5, 8, 3, 2, 1]
    print(bubble_sort(test))

if __name__ == "__main__":
    main()
```