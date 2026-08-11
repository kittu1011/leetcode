---
difficulty: Medium
pattern: Sorting
misclassified: No
guessed_pattern: Sorting
time_min: 10
revisit: 10/1/2026
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity:

## Optimized approach(es)

### 1.
**Complexity:** TC: $O(N\log(N))$ SC: $O(1)$
**Insight:** Sort the original interval arrays by start times. This way if two intervals will be merged they must be contigous in the sorted array

## Mistakes made
No need to sort array by both start and end time(tie-breaker) of interval. Just take the max of both intervals ending times

## Time to solve
12 min cold

## Revisit