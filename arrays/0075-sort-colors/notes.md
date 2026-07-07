---
difficulty: Medium
pattern: 3 way Dutch Flag
misclassified: No
guessed_pattern: N/A
time_min: 32
revisit: 8/1/2026
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity: Just bubble sort the array TC: $O(N^2)$ SC: $O(1)$

## Optimized approach(es)

### 1.
**Complexity:** TC: O(N) SC: O(1)
**Insight:** Partition the array into three segments

## Mistakes made
In the elif branch I decremented i before the swap, causing a bug I couldn't even read as my brain skimmed over it.
Loop conditional was i < r instead i <= r

## Time to solve
32 min cold, but I solved it last year

## Revisit