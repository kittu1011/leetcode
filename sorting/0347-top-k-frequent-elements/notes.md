---
difficulty: Medium
pattern: Bucket Sort
misclassified: Yes
guessed_pattern: N/A
time_min: 31
revisit: 7/20/2026
---

## Key signal I should have caught
This was a bucket sort problem. I wanted a clean way to sort frequencies in $O(N)$ time. This is possible by knowing the frequency of an element ranges from $[1,n]$

## Brute force
Approach + complexity:
Create a frequency map of elements and then create a list of $[count, element]$ pairs and sort them by count. Then just get k pairs with largest count
TC: $O(N \cdot \log(N))$ SC: $O(N)$
## Optimized approach(es)

### 1.
**Complexity:** TC: $O(N)$ SC: $O(N)$
**Insight:** We need to sort by count which we can bucket sort in $O(N)$ due to its value constraints
**Complexity:** TC: $O(N \cdot \log(K))$ SC: $O(N)$
**Insight:** We keep a min heap of $[count,n]$ pairs ordered by count of size k.

## Mistakes made
Doing [[]] * N + 1 to initialize a nested list. This is just wrongs as it makes shallow copies of the same list as [] is mutable 

## Time to solve
31 min cold with NC hint for apprch 1. 5 mins after seeing solution for appr 2.

## Revisit
Do it cold without hint. Just know it's bucket sort