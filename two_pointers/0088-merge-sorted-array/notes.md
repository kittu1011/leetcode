---
difficulty: Easy
pattern: Two Pointers
misclassified: N/A
guessed_pattern: Two Pointers
time_min: 20
revisit: 9/10/2026
---

## Key signal I should have caught
- Iterating backwards through both lists prevents clobbering data
- If `write_index > read_index`, iterate **back-to-front**. If `write_index < read_index`, iterate **front-to-back**.

## Brute force
Approach + complexity: Merge both lists by using an auxillary list to store output temporarily
TC: $O(N)$ SC: $O(N)$

## Optimized approach(es)

### 1. Three Pointers
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Iterate backwards through both lists and merging from largest elements first prevents clobbering data

## Mistakes made
I tried merging the list forward which required shifting the elements of `nums1` to the back.

## Time to solve
20 min cold

## Revisit
Merge the list backwards. Starting with the back of the output array