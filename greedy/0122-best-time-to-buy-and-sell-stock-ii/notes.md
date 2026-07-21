---
difficulty: Medium
pattern: greedy
misclassified: Yes
guessed_pattern: DP
time_min: 40
revisit: 8/1/2026
---

## Key signal I should have caught
If you draw the prices as a graph the result is just the summation of all consecutive day price increases. This means a simple greedy approach works

## Brute force 
Approach + complexity: For each day do one of three things: skip the day, buy the stock today if possible, sell the stock today if possible and recursively calculate the answer for the rest of the days. TC: $O(2^N)$ SC: $O(N)$

## Optimized approach(es)
1.greedy
2.DP
### 1. Greedy
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** The result is the summation of all consecuitive day increases
### 2. DP
**Complexity:** TC: $O(N)$ SC: $O(1)$ *(optimized for space)*
**Insight:** You either skip, buy or sell on each day

## Mistakes made
Did a 1d DP approach that took $O(N^2)$ time which slowed down. The 2d dp approach worked by utilizing a 2nd variable expressing weather a stock is currently held or not

## Time to solve
40 mins with hint

## Revisit
Should be able to solve with greedy approach cold next time