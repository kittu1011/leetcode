---
difficulty: Easy
pattern: direct hashing, seperate chaining
misclassified: N/A
guessed_pattern: direct hashing, seperate chaining
time_min: 15
revisit: 7/12/2026
---

## Key signal I should have caught
N/A as this is exact same problem as 705

## Brute force
Approach + complexity:
Just append and remove from an array of pairs. Each operation will be linear w.r.t array size

## Optimized approach(es)
N/A

### 1.
**Complexity:** TC: O(1) SC: O(10000)
**Insight:** Doing this without dummy node made me appreciate it much more
### 2.
**Complexity:** TC: O(1) SC: O($10^6+1$)
**Insight:** Direct hashing to an array of integers that represent values (not keys). Easy to code\

## Mistakes made
When doing appr 1. remove, if prev == None then I set the arr[idx] to None which essentially deleted all elements of the linked list

## Time to solve
15 mins cold for appr. 1. Appr 2. was done in 2 mins

## Revisit
Do Appr 1. with dummy node