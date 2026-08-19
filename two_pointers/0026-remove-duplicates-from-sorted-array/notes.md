---
difficulty: Easy
pattern: Two Pointers
misclassified: No
guessed_pattern: Two Pointers
time_min: 3
revisit: 10/1/2026
---

## Key signal I should have caught
We can start from `i=1` as first element in array is always unique

## Brute force Sorted Set
Approach + complexity: Convert array into a set of distinct elements, then sort that set into an array
TC: $O(N\log N)$ SC: $O(N)$

## Optimized approach(es)

### 1. Two Pointers
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Write to `output` ptr iff `nums[i] != nums[i-1]`

## Mistakes made
Started at `i=0` which made if conditional slightly longer

## Time to solve
3 min cold

## Revisit
Remember first element in array is always unique
