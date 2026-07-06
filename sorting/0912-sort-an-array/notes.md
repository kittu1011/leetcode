---
difficulty: Medium
pattern: Quick Sort
misclassified: true
guessed_pattern: Merge Sort
time_min: 40
revisit: 7/20/2026
---

## Key signal I should have caught
Forgot how to do quick sort so just did merge sort implementation

## Brute force
Approach + complexity: TC: O($n^2$) SC: O(1)

## Optimized approach(es): 2

### 1.
**Complexity:** TC: O($n^2$) SC: O(n)
**Insight:** Textbook merge sort so nothing really new there. Just use pointers and do it in-place as much as possible. However it's important to know that `arr[l:r]` creates a shallow copy. This is fine when the list contians immutable objects like ints, as modifiying the shallow copy does not modify the original.

### 2.
**Complexity:** TC: O($n^2$) SC: O(1)
**Insight:** Quick sort was buggier to implement due to the edge cases of partitioning function. If l did not point to something >= pivot_val it's important to swap `nums[pivot]` with something that is >= nums[r+1]

## Mistakes made
Passing shallow copies of the array into recursive helpers args. Better to use indirection with some l,r pointers and save space/time. 

## Time to solve
40 min cold for appr. 1 with some help to clean up code

## Revisit
Should be able to do quicksort cold in revisit