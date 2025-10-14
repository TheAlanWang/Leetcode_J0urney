---
tags:
  - algorithm
pageorder: 1.2
mainpage:
  - "[[DV_DataStructure]]"
description: write
---
Time complexity: $O(nlogn)$
Unstable

```python
'''
Write a function quicksort(items: list) that sorts its input list in place using quicksort.
(Quicksort chooses one of the items as a pivot, places all items smaller than the pivot at the beginning and all items larger than the pivot at the end, places the pivot right between them, then recursively sorts both chunks.)
'''
def quicksort(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low >= high:
        return arr

    pivot = arr[high]
    
    i = low # track the position where the next smaller-than-pivot element should go
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i] #swap pivot to i-th

    quicksort(arr, low, i - 1)
    quicksort(arr, i + 1, high)

    if low == 0 and high == len(arr) - 1:
        return arr
        
def main():
    test = [5, 8, 3, 2, 1]
    print(quicksort(test))

if __name__ == "__main__":
    main()
```

### Step 1: Initial Setup
- If `low` and `high` are not given, they are set to the start and end of the array.
- This prepares for recursive calls and ensures the full array is sorted initially.
### Step 2: Base Case Check
- If `low >= high`, it means the current subarray has 0 or 1 elements, which is already sorted.
- The function returns immediately without doing anything.
### Step 3: Choose Pivot
- The pivot is typically chosen as the element at `arr[high]`.
- This value is used to divide the array into elements less than the pivot and greater than or equal to it.
### Step 4: Partitioning Loop
- A pointer `i` is used to track where the next smaller-than-pivot element should go.
- Another pointer `j` scans from `low` to `high - 1`:
    - If `arr[j]` is less than the pivot, it's swapped with `arr[i]`, and `i` is incremented.
- This process ensures all elements before `i` are less than the pivot.
### Step 5: Swap Pivot Into Place
- After the loop, the pivot is swapped with `arr[i]`.
- This puts the pivot into its correct sorted position in the array.
###  Step 6: Recursive Calls
- The algorithm recursively calls `quicksort` on the left subarray (`low` to `i - 1`) and the right subarray (`i + 1` to `high`).
- This process repeats for each subarray until the base case is reached.
### Step 7: Return Final Result
- Only in the outermost call (when `low == 0` and `high == len(arr) - 1`), the sorted array is returned.
- This allows the user to see the sorted result without returning from every recursive layer.