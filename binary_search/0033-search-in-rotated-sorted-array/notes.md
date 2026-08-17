---
difficulty: Medium
pattern: Binary Search
misclassified: No
guessed_pattern: Binary Search
time_min: 12
revisit: 11/11/2026
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity: Simple linear search through array
TC: $O(N)$ SC: $O(1)$

## Optimized approach(es)

### 1. Binary Search
**Complexity:** $O(\log N)$ SC: $O(1)$
**Insight:** A rotated sorted array can be seen as two concatenated sorted arrays where one of the arrays is $\le$ than the smallest element in the other array. Every time the array is split in two halves at least one of these halves are guaranteed to be sorted. Make a decision weather or not continue searching it 

## Mistakes made
N/A

## Time to solve
12 min cold

## Revisit