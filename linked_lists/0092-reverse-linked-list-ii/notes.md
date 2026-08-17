---
difficulty: Medium
pattern: Iteration
misclassified: No
guessed_pattern: Iteration
time_min: 15
revisit: 12/12/2026
---

## Key signal I should have caught
N/A

## Brute force
Approach + complexity: Find the sublist to reverse, detach it, and then reattach it TC: $O(N)$ SC: $O(1)$
## Optimized approach(es)

### 1. Iteration
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Find the first node in sublist to reverse, reverse right - left + 1 nodes, correctly reattach reversed sublist

## Mistakes made
N/A

## Time to solve
15 min cold

## Revisit