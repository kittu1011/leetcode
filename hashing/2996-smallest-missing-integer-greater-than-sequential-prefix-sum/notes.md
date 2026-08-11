---
difficulty: Easy
pattern: Hashing
misclassified: No
guessed_pattern: Hashing
time_min: 7
revisit: 1-12-2027
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity: Iterate until longest contigous prefix breaks and linearly search if it's sum exists. If sum exists return, otherwise increment count until it does.
TC: $O(N^2)$ SC: $O(1)$

## Optimized approach(es)

### 1. Hash array
**Complexity:** TC: $O(N)$ SC: $O(N)$
**Insight:** Hash the array so you don't waste time linearly searching for `prefix_sum + x`

## Mistakes made
N/A

## Time to solve
7 min cold

## Revisit
N/A