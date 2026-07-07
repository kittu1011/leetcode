---
difficulty: Medium
pattern: Hashing
misclassified: No
guessed_pattern:
time_min: 16
revisit: 7/21/2026
---

## Key signal I should have caught
Two pass of O(N) is still O(N)

## Brute force
Approach + complexity: Sort the array and find the max consecutive window TC: $O(N\cdot\logN)$ SC: $O(N)$

## Optimized approach(es)

### 1. Hash-Map approach
**Complexity:** TC: $O(N)$ SC: $O(N)$
**Insight:** Map num in arr to longest sequence at that element
### 2. Set approach
**Complexity:** TC: $O(N)$ SC: $O(N)$
**Insight:** Sequence can only have one starting point, so just calculate longest sequence from every possible starting point
## Mistakes made
Did not fully account for repeated elements in approach 1 leading to bug

## Time to solve
16 min cold

## Revisit
Do approach 2 cold