---
difficulty: Hard
pattern: Binary Search
misclassified: No
guessed_pattern: Binary Search
time_min: ∞
revisit: 9/12/2026
---

## Key signal I should have caught
- Median will be at index `(m + n) // 2`. `k` of those elements will be in `nums1` and the `(m + n) // 2` - `k` elements will be in `nums2`
- Binary Search to find the right value of `k`
- Need to calculate 4 values: 
    - max value of left partition in `nums1`
    - max value of left partition in `nums2`
    - min value of right partition in `nums1`
    - min value of right partition in `nums1`

## Brute force
Approach + complexity: Merge two arrays and calculate median from merged array
TC: $O(M + N)$ SC: $O(M + N)$

## Optimized approach(es)

### 1. Binary Search
**Complexity:** TC: $O(\log (M + N))$ SC: $O(1)$
**Insight:** Binary search to remove the correct `k` elements from the smaller array

## Mistakes made
- Do binary search on smaller array as this guarantees `idx` will never be less than `0`, which causes weird edge cases
- Calculate all four values inside the while loop itself and use them as the conditionals to adjust `l` and `r` pointers
- Do `l <= r` in while loop condition as `m` is not an out of bounds value for `mid`  

## Time to solve
∞ min needed help

## Revisit
Just solve it first try