---
difficulty: Easy
pattern: Two Pointers
misclassified: No
guessed_pattern: Two Pointers
time_min: 7
revisit: 9/4/2026
---

## Key signal I should have caught
Don't repeat code, make a function

## Brute force
Approach + complexity: Remove each element from list(or no element from list) and see if the modification is palindrome.
TC: $O(N^2)$ SC: $O(N)$

## Optimized approach(es)

### 1. Two Pointers
**Complexity:** TC: $O(N)$ SC: $O(1)$
**Insight:** Check if string is valid palindrome without deletion criteria. On the first mismatch check if s[l+1:r+1] or s[l:r] is a palindrome

## Mistakes made
Didn't write another function take took in two pointers to check if palindrome. Causing uneeded repetition

## Time to solve
7 min cold

## Revisit
Solve it clean next time