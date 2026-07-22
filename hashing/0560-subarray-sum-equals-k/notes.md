---
difficulty: Medium
pattern: Prefix Sum
misclassified: No
guessed_pattern: Prefix Sum
time_min: 28 min
revisit: 8/9/2026
---

## Key signal I should have caught
You can consider any possible sub array by tracking culminating sum and culminating prefix sums

## Brute force
Approach + complexity: Loop through all possible subarray and compute their sum. TC:$ O(N^2)$ SC: $O(1)$

## Optimized approach(es)

### 1. Prefix Sum
**Complexity:** TC: $O(N)$ SC: $O(N)$
**Insight:** Track culiminating sum and hash prefix sums to their frequency

## Mistakes made
Was thinking of doing prefix sums in one pass and postfix sums in another. Then try to compute answer by looping through those hashes. Luckily you can consider all sub-arrays with prefix sums and one pass

## Time to solve
28 min cold with small hint on prefix sum frequency table

## Revisit
Figure out prefix sum freq. table trick cold