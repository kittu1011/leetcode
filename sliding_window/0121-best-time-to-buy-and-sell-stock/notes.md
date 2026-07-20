---
difficulty: Easy
pattern: sliding window
misclassified: No
guessed_pattern: sliding window
time_min: 9
revisit: 9/14/2026
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity: Compute all $(i,j)$ pairs where $i < j$ and return the maximum difference. TC: $O(N^2)$ SC: $O(1)$

## Optimized approach(es)
1. Sliding Window
### 1.
**Complexity:** TC: $O(N^2)$ SC: $O(1)$
**Insight:** The maximum difference was between a rolling minimum of the array and some element j. Therefore you should track the rolling minimum and compute it's difference with current elements

## Mistakes made
N/A

## Time to solve
9 min cold

## Revisit
N/A