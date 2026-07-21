---
difficulty: Medium
pattern: Moore Voting Algorithm
misclassified: N/A
guessed_pattern: Moore Voting Algorithm
time_min: 40
revisit: 8/2/2026
---

## Key signal I should have caught
There can only be two elements at most in the result. The else statement retires 3 elements `(cand1,cand2,x)` which implies if $x$ is in result then it will either end up as `cand1` or `cand2`.

## Brute force
Approach + complexity: Count freq of each character then iterate through the freq map and add elements with count > $N / 3$ TC: $O(N)$ SC: $O(N)$

## Optimized approach(es)

### 1. Moore Voting Algorithm
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:**

## Mistakes made
Need to be better at tailoring an existing algorithm better

## Time to solve
40 min with solution

## Revisit
Solve problem cold