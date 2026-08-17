---
difficulty: Medium
pattern: Two Pointers
misclassified: Yes
guessed_pattern: Hashing
time_min: 16
revisit: 9/2/2026
---

## Key signal I should have caught
If I have two pointers and space them by $n$ nodes, the first pointer will point to the 1 minus the node to remove once the second pointer reaches the end

## Brute force Cacheing
Approach + complexity: Iterate throughout the list and cache the pointers into array. Just remove the $N$th from the end of array/cache TC: $O(N)$ SC: $O(N)$

## Optimized approach(es)

### 1. Two Pointers
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Use delay pointers and space them by $n$ nodes

## Mistakes made
Not using two pointers

## Time to solve
16 min cold

## Revisit