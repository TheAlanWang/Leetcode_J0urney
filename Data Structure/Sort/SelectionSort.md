---
tags:
  - algorithm
pageorder: 1.5
mainpage:
  - "[[DV_DataStructure]]"
description: know
---
```python
def selection_sort(nums: list):
    n = len(nums)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


def main():
    test = [5, 8, 3, 2, 1]
    print(selection_sort(test))

if __name__ == "__main__":
    main()

```