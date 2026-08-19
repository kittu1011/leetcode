---
difficulty: Medium
pattern: Binary Search
misclassified: No
guessed_pattern: Binary Search
time_min: 22
revisit: 10/4/2026
---

## Key signal I should have caught
Order does matter in this case and can change your answer

## Brute force
Approach + complexity: Linearly Search from all possible capacities $[\max(weights),\sum(weights)]$
TC: $O(N*\sum(weights))$ SC: $O(1)$

## Optimized approach(es)

### 1. Binary Search
**Complexity:** TC: $O(N*\log(\sum(weights)))$ SC: $O(1)$
**Insight:** Do a binary search for feasible values $[\max(weights),\sum(weights)]$

## Mistakes made
- `l` should be equal to `min(weights)`

## Time to solve
22 min cold

## Revisit
Do it quicker